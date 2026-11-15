"""Builds an editable Word version of the chapter: eco_project.docx.

Steps
1. Renders every TikZ diagram to PNG (figures/docx/), by compiling each one
   alone with fxstyle and cropping to the drawing.
2. Converts the LaTeX sections (in main.tex order) to pandoc Markdown:
   boxes become shaded Word paragraph styles, answers become Word footnotes
   (marked *, †, ‡), citations become superscript numbers, margin key terms
   become small 'Key Term' paragraphs under the paragraph that uses them.
3. Runs pandoc with a reference document (styles: fonts, colours, boxes),
   then sets footnote marks to symbols restarting on each page.

Run after compiling the PDF (it reads main.aux for figure/section numbers):
    python source/build_docx.py
"""
import io
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pymupdf
import pypandoc

BOOK = Path(__file__).resolve().parent.parent
SECTIONS = BOOK / "sections"
IMG = BOOK / "figures" / "docx"
BUILD = BOOK / "source" / "_docx_build"
OUT = BOOK / "eco_project.docx"
PANDOC = pypandoc.get_pandoc_path()

# --------------------------------------------------------------------------
# 1. TikZ diagrams -> PNG
# --------------------------------------------------------------------------
TIKZ = {  # png name: (LaTeX to place on the page)
    "fx_flow": r"\resizebox{\linewidth}{!}{\input{figures/fx_flow.tex}}",
    "ds_basic": r"\resizebox{\linewidth}{!}{\input{figures/ds_basic.tex}}",
    "ds_intervention": r"\input{figures/ds_intervention.tex}",
    "ds_shocks": r"\resizebox{0.92\linewidth}{!}{\input{figures/ds_shocks.tex}}",
    "imported_inflation": r"\resizebox{\linewidth}{!}{\input{figures/imported_inflation.tex}}",
}


def timeline_code():
    s06 = (SECTIONS / "s06_systems.tex").read_text(encoding="utf-8")
    m = re.search(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", s06, flags=re.S)
    return r"\resizebox{\linewidth}{!}{%" + "\n" + m.group(0) + "}"


def render_tikz():
    IMG.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    jobs = dict(TIKZ, timeline=timeline_code())
    for name, body in jobs.items():
        tex = BUILD / f"fig_{name}.tex"
        tex.write_text("\\documentclass[11pt]{article}\n\\usepackage{fxstyle}\n\\pagestyle{empty}\n"
                       "\\begin{document}\n\\noindent " + body + "\n\\end{document}\n", encoding="utf-8")
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                            f"-output-directory={BUILD}", str(tex)],
                           cwd=BOOK, capture_output=True, text=True, encoding="utf-8", errors="replace")
        pdf = BUILD / f"fig_{name}.pdf"
        if r.returncode or not pdf.exists():
            sys.exit(f"TikZ render failed for {name}:\n{r.stdout[-1500:]}")
        page = pymupdf.open(pdf)[0]
        box = pymupdf.Rect()
        for d in page.get_drawings():
            box |= d["rect"]
        for b in page.get_text("blocks"):
            box |= pymupdf.Rect(b[:4])
        box = (box + (-4, -4, 4, 4)) & page.rect
        page.get_pixmap(dpi=250, clip=box).save(IMG / f"{name}.png")
        print("rendered", name)


# --------------------------------------------------------------------------
# 2. LaTeX -> pandoc Markdown
# --------------------------------------------------------------------------
AUX = (BOOK / "main.aux").read_text(encoding="utf-8")
LABELS = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", AUX))
BIB = re.findall(r"\\bibitem\{([^}]+)\}", (SECTIONS / "e4_references.tex").read_text(encoding="utf-8"))
CITENUM = {k: i + 1 for i, k in enumerate(BIB)}

BOXES = {  # env: (label, style colour)
    "didyouknow": ("Did you know?", "Teal"),
    "workedexample": ("Worked example", "Navy"),
    "exercise": ("Exercise", "Orange"),
    "economistsfacts": ("How economists learn from facts", "Green"),
    "keypoints": ("Key points", "Plum"),
    "casestudy": ("Case study", "Navy"),
    "economistsdisagree": ("When economists disagree", "Orange"),
}
STYLE = "\x01"  # paragraph prefix: \x01Style Name\x01 text  -> wrapped in a custom-style div
DROP = {"small", "footnotesize", "scriptsize", "normalsize", "large", "Large", "sffamily", "rmfamily",
        "bfseries", "mdseries", "itshape", "raggedright", "RaggedRight", "centering", "medskip",
        "smallskip", "bigskip", "noindent", "hfill", "toprule", "midrule", "bottomrule", "addlinespace",
        "heavysans", "selectfont", "relax", "clearpage", "newpage", "protect", "item"}
SPACE = {"quad", "qquad", "enspace", "thinspace", ",", " "}
ESCAPE = set("*_[]#<>^|@\\`$")
WARN = set()


def balanced(s, i, open_="{", close="}"):
    depth = 0
    for j in range(i, len(s)):
        if s[j] == open_:
            depth += 1
        elif s[j] == close:
            depth -= 1
            if depth == 0:
                return j + 1
    raise ValueError("unbalanced: " + s[i:i + 60])


def arg(s, i):
    """Skip spaces, read one {group} or one token. Return (content, end)."""
    while i < len(s) and s[i] in " \n":
        i += 1
    if i < len(s) and s[i] == "{":
        j = balanced(s, i)
        return s[i + 1:j - 1], j
    return s[i], i + 1


def opt(s, i):
    while i < len(s) and s[i] == " ":
        i += 1
    if i < len(s) and s[i] == "[":
        j = balanced(s, i, "[", "]")
        return s[i + 1:j - 1], j
    return None, i


def strip_comments(t):
    return re.sub(r"(?m)(?<!\\)%.*$\n?", "", t)


class Inline:
    """Converts inline LaTeX to Markdown; collects margin notes for the paragraph."""

    def __init__(self):
        self.notes = []

    def __call__(self, s):
        out, i = [], 0
        while i < len(s):
            c = s[i]
            if c == "\\":
                m = re.match(r"\\([A-Za-z@]+)\*?|\\(.)", s[i:], flags=re.S)
                name, sym = m.group(1), m.group(2)
                i += len(m.group(0))
                if sym is not None:
                    out.append({"\\": "\n", "%": "%", "&": "&", "$": "\\$", "#": "\\#", "_": "\\_",
                                "-": "", "/": ""}.get(sym, " " if sym in SPACE else sym))
                    continue
                if name not in ("item",):
                    while i < len(s) and s[i] == " " and name not in SPACE:
                        i += 1
                txt, i = self.command(name, s, i)
                out.append(txt)
            elif c == "{":
                j = balanced(s, i)
                out.append(self(s[i + 1:j - 1]))
                i = j
            elif c == "}":
                i += 1
            elif c == "~":
                out.append("\u00a0")
                i += 1
            elif s.startswith("---", i):
                out.append("—"); i += 3
            elif s.startswith("--", i):
                out.append("–"); i += 2
            elif s.startswith("``", i):
                out.append("“"); i += 2
            elif s.startswith("''", i):
                out.append("”"); i += 2
            elif c == "`":
                out.append("‘"); i += 1
            elif c == "'":
                out.append("’"); i += 1
            elif c in ESCAPE:
                out.append("\\" + c); i += 1
            else:
                out.append(c); i += 1
        return "".join(out)

    def command(self, name, s, i):
        if name in ("textbf",):
            a, i = arg(s, i)
            inner = self(a).strip()
            return (f"**{inner}**" if inner else ""), i
        if name in ("emph", "textit"):
            a, i = arg(s, i)
            return f"*{self(a).strip()}*", i
        if name in ("textmd", "textrm", "textsf", "mbox", "text", "textup"):
            a, i = arg(s, i)
            return self(a), i
        if name == "textcolor":
            _, i = arg(s, i)
            a, i = arg(s, i)
            return self(a), i
        if name == "color":
            _, i = arg(s, i)
            return "", i
        if name == "textsubscript":
            a, i = arg(s, i)
            return f"~{self(a)}~", i
        if name == "textsuperscript":
            a, i = arg(s, i)
            return f"^{self(a)}^", i
        if name == "keyterm":
            o, i = opt(s, i)
            t, i = arg(s, i)
            d, i = arg(s, i)
            self.notes.append((self(t), self(o if o is not None else d)))
            return f"**{self(t)}**", i
        if name == "defterm":
            t, i = arg(s, i)
            _, i = arg(s, i)
            return f"**{self(t)}**", i
        if name == "termnote":
            t, i = arg(s, i)
            d, i = arg(s, i)
            self.notes.append((self(t), self(d)))
            return "", i
        if name == "sidenote":
            d, i = arg(s, i)
            self.notes.append((None, self(d)))
            return "", i
        if name == "cite":
            _, i = opt(s, i)
            a, i = arg(s, i)
            nums = sorted(CITENUM[k.strip()] for k in a.split(","))
            return "^" + ",".join(map(str, nums)) + "^", i
        if name in ("seesec", "secref", "ref"):
            a, i = arg(s, i)
            n = LABELS.get(a, "??")
            return {"seesec": f"(see Section {n})", "secref": f"Section {n}"}.get(name, n), i
        if name == "href":
            u, i = arg(s, i)
            t, i = arg(s, i)
            return f"[{self(t)}]({u})", i
        if name == "url":
            u, i = arg(s, i)
            return f"<{u}>", i
        if name == "answers":
            a, i = arg(s, i)
            return f"^[**Answers.** {self(a).strip()}]", i
        if name == "ans":  # review questions: answer on its own line under the question
            a, i = arg(s, i)
            return f"\x02*Answer.* {self(a).strip()}", i
        if name == "minihead":
            a, i = arg(s, i)
            return f"**{self(a).strip()}** ", i
        if name == "figsource":
            a, i = arg(s, i)
            return f"\n\n{STYLE}Figure Source{STYLE}Source: {self(a).strip()}\n\n", i
        if name == "fximg":
            a, i = arg(s, i)
            return f"\n\n![]({a}){{width=100%}}\n\n", i
        if name == "fxcap":
            kind, i = arg(s, i)
            lab, i = arg(s, i)
            a, i = arg(s, i)
            word = "Figure" if kind == "figure" else "Table"
            return f"\n\n{STYLE}Caption Label{STYLE}**{word} {LABELS.get(lab, '??')}.** {self(a).strip()}\n\n", i
        if name == "textperiodcentered":
            return "·", i
        if name == "par":
            return "\n\n", i
        if name in ("label", "addcontentsline", "vspace", "hspace"):
            if name == "addcontentsline":
                _, i = arg(s, i); _, i = arg(s, i)
            _, i = arg(s, i)
            return "", i
        if name in SPACE:
            return " ", i
        if name in DROP:
            return "", i
        if name == "ldots":
            return "…", i
        WARN.add(name)
        return "", i


def flush_paragraphs(buf, conv, out):
    for para in re.split(r"\n\s*\n", buf):
        if not para.strip():
            continue
        conv.notes = []
        md = conv(para)
        for piece in re.split(r"\n\s*\n", md):
            piece = re.sub(r"[ \t]*\n[ \t]*", " ", piece).strip()
            if not piece:
                continue
            if piece.startswith(STYLE):
                _, style, text = piece.split(STYLE, 2)
                out.append(div(style, text.strip()))
            else:
                out.append(piece)
        for term, note in conv.notes:
            out.append(div("Key Term", (f"**{term}**  " if term else "") + note.strip()))


def div(style, text):
    return f'::: {{custom-style="{style}"}}\n{text}\n:::'


def find_end(s, env, start):
    """Index of the matching \\end{env} for a \\begin{env} that ends at start."""
    depth, pos = 1, start
    pat = re.compile(r"\\(begin|end)\{%s\}" % re.escape(env))
    while True:
        m = pat.search(s, pos)
        if not m:
            raise ValueError("no end for " + env)
        depth += 1 if m.group(1) == "begin" else -1
        if depth == 0:
            return m.start(), m.end()
        pos = m.end()


def prep_figures_in_text(t):
    """Turn figure pieces that sit inside boxes into one-line commands."""
    t = re.sub(r"\\resizebox\{[^}]*\}\{!\}\{%?\s*\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}",
               r"\n\n\\fximg{figures/docx/timeline.png}\n\n", t, flags=re.S)
    t = re.sub(r"\\includegraphics(\[[^\]]*\])?\{([^}]+)\}",
               lambda m: "\n\n\\fximg{%s}\n\n" % img_path(m.group(2)), t)
    t = re.sub(r"\\captionof\{(figure|table)\}\{((?:[^{}]|\{[^{}]*\})*)\}\s*\\label\{([^}]+)\}",
               r"\n\n\\fxcap{\1}{\3}{\2}\n\n", t)
    t = re.sub(r"\\figsource\{", r"\n\n\\figsource{", t)
    return t


def img_path(p):
    p = p.replace("\\", "/")
    if p.endswith(".pdf"):
        p = p[:-4] + ".png"
    return p


def lst(env, body, conv, opts, inside_box=False):
    items = re.split(r"\\item\b", body)[1:]
    if inside_box:  # Word list styles would drop the box shading: write plain paragraphs
        out = []
        for n, it in enumerate(items):
            if "\\Alph" in (opts or ""):
                mark = f"{chr(65 + n)}\\."
            elif "\\alph" in (opts or ""):
                mark = f"\\({chr(97 + n)})"
            elif env == "enumerate":
                mark = f"{n + 1}\\."
            else:
                mark = "•"
            out.append(mark + "\u2002" + re.sub(r"\s*\n\s*", " ", conv(it)).strip())
        return "\n\n".join(out)
    out = []
    for n, it in enumerate(items):
        if "\\Alph" in (opts or ""):
            mark = f"{chr(65 + n)}.  "
        elif "\\alph" in (opts or ""):
            mark = f"({chr(97 + n)}) "
        elif env == "enumerate":
            mark = f"{n + 1}. "
        else:
            mark = "- "
        conv.notes = []
        text = re.sub(r"\s*\n\s*", " ", conv(it)).strip()
        main, *answers = text.split("\x02")
        lines = [mark + main.strip()]
        for a in answers:
            lines.append("")
            lines.append("    " + a.strip())
        out.append("\n".join(lines))
    return ("\n\n" if any("\x02" in conv(i) for i in items) else "\n").join(out)


def table_md(spec_widths, body, conv):
    body = re.sub(r"\\(toprule|midrule|bottomrule|addlinespace)(\[[^\]]*\])?", "", body)
    rows = [r for r in re.split(r"\\\\", body) if r.strip()]
    cells = [[re.sub(r"\s+", " ", conv(c)).strip().replace("|", "\\|") for c in r.split("&")] for r in rows]
    ncol = len(cells[0])
    total = sum(spec_widths)
    dashes = ["-" * max(3, round(60 * w / total)) for w in spec_widths]
    lines = ["| " + " | ".join(cells[0]) + " |", "|" + "|".join(dashes) + "|"]
    for r in cells[1:]:
        r = r + [""] * (ncol - len(r))
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def col_widths(spec):
    widths = []
    for m in re.finditer(r"p\{(\d+)mm\}|X|\bl\b|\bc\b|\br\b", spec):
        widths.append(int(m.group(1)) if m.group(1) else 45)
    return widths


def float_env(env, body, conv, out):
    """figure / table: image(s), caption, note text, source."""
    label = re.search(r"\\label\{([^}]+)\}", body)
    num = LABELS.get(label.group(1), "??") if label else "??"
    cap = re.search(r"\\caption\{((?:[^{}]|\{[^{}]*\})*)\}", body)
    caption = conv(cap.group(1)).strip() if cap else ""
    src = re.search(r"\\figsource\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}", body)
    source = conv(src.group(1)).strip() if src else ""
    images = []
    for m in re.finditer(r"\\includegraphics(\[[^\]]*\])?\{([^}]+)\}|\\input\{figures/([^}]+)\.tex\}", body):
        images.append(img_path(m.group(2)) if m.group(2) else f"figures/docx/{m.group(3)}.png")
    tab = re.search(r"\\begin\{tabularx?\}", body)
    rest = body
    for pat in (r"\\caption\{((?:[^{}]|\{[^{}]*\})*)\}", r"\\label\{[^}]+\}",
                r"\\figsource\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}",
                r"\\includegraphics(\[[^\]]*\])?\{[^}]+\}", r"\\resizebox\{[^}]*\}\{!\}\{\\input\{[^}]+\}\}",
                r"\\input\{[^}]+\}", r"\\begin\{minipage\}(\[[^\]]*\])?\{[^}]*\}", r"\\end\{minipage\}",
                r"\\begin\{tabularx?\}.*?\\end\{tabularx?\}"):
        rest = re.sub(pat, " ", rest, flags=re.S)
    note = re.sub(r"\s+", " ", conv(rest)).strip()
    note_parts = [p.strip() for p in conv(rest).split("\n") if p.strip()]
    word = "Figure" if env == "figure" else "Table"
    if env == "table":
        out.append(div("Caption Label", f"**{word} {num}.** {caption}"))
        m = re.search(r"\\begin\{(tabularx?)\}", body)
        e = m.group(1)
        j = m.end()
        if e == "tabularx":
            _, j = arg(body, j)
        spec, j = arg(body, j)
        end = body.index("\\end{%s}" % e, j)
        out.append(table_md(col_widths(spec), body[j:end], conv))
    else:
        for im in images:
            out.append(f"![]({im}){{width=100%}}")
        out.append(div("Caption Label", f"**{word} {num}.** {caption}"))
    if note:
        for p in note_parts:
            out.append(div("Caption Note", re.sub(r"\s+", " ", p)))
    if source:
        out.append(div("Figure Source", f"Source: {source}"))


def blocks(t, conv, inside_box=False):
    out, pos, buf = [], 0, []
    t = strip_comments(t)
    if inside_box:
        t = prep_figures_in_text(t)
    token = re.compile(r"\\begin\{(\w+)\}|\\(section|subsection)(\*?)\{|\\qsec\{|\\addcontentsline\{|"
                       r"\\label\{|\\newcommand|\\begingroup|\\endgroup|\\setlength\{|\\renewcommand")
    while True:
        m = token.search(t, pos)
        if not m:
            buf.append(t[pos:])
            break
        buf.append(t[pos:m.start()])
        flush_paragraphs("".join(buf), conv, out)
        buf = []
        tok = m.group(0)
        if m.group(1):
            env = m.group(1)
            s_end, e_end = find_end(t, env, m.end())
            body_start = m.end()
            if env in BOXES:
                o, body_start = opt(t, body_start)
                title, body_start = arg(t, body_start)
                label, colour = BOXES[env]
                out.append(div(f"Box {colour} Heading", f"**{label}** {conv(title).strip()}"))
                inner = blocks(t[body_start:s_end], conv, inside_box=True)
                out.append(f'::: {{custom-style="Box {colour}"}}\n' + "\n\n".join(inner) + "\n:::")
            elif env in ("itemize", "enumerate"):
                o, body_start = opt(t, body_start)
                out.append(lst(env, t[body_start:s_end], conv, o, inside_box))
            elif env in ("figure", "table"):
                _, body_start = opt(t, body_start)
                float_env(env, t[body_start:s_end], conv, out)
            elif env == "thebibliography":
                _, body_start = arg(t, body_start)
                items = re.split(r"\\bibitem\{[^}]+\}", t[body_start:s_end])[1:]
                out.append("\n".join(f"{n + 1}. {re.sub(r'\\s+', ' ', conv(x)).strip()}"
                                     for n, x in enumerate(items)))
            else:
                WARN.add("env:" + env)
                out += blocks(t[body_start:s_end], conv)
            pos = e_end
        elif m.group(2):
            title, pos = arg(t, m.end() - 1)
            if m.group(2) == "section":
                if m.group(3):
                    out.append(f"# {conv(title).strip()}")
                else:
                    blocks.secno += 1
                    out.append(f"# {blocks.secno}\u2002{conv(title).strip()}")
            else:
                out.append(f"## {conv(title).strip()}")
        elif tok.startswith("\\qsec"):
            title, pos = arg(t, m.end() - 1)
            out.append(f"### {conv(title).strip()}")
        elif tok.startswith("\\addcontentsline"):
            _, p = arg(t, m.end() - 1)
            _, p = arg(t, p)
            _, pos = arg(t, p)
        elif tok.startswith("\\label") or tok.startswith("\\setlength"):
            _, p = arg(t, m.end() - 1)
            if tok.startswith("\\setlength"):
                _, p = arg(t, p)
            pos = p
        elif tok in ("\\newcommand", "\\renewcommand"):
            name, p = arg(t, m.end())
            o, p = opt(t, p)
            _, pos = arg(t, p)
        else:  # \begingroup, \endgroup
            pos = m.end()
    flush_paragraphs("".join(buf), conv, out)
    return out


blocks.secno = 0


def markdown():
    main = (BOOK / "main.tex").read_text(encoding="utf-8")
    conv = Inline()
    title = re.search(r"\\chaptertitle\{(.*?)\}\s*\{(.*?)\}\s*\{(.*?)\}", main, flags=re.S)
    md = [div("Kicker", conv(title.group(1)).strip().upper()),
          div("Title", conv(title.group(2)).strip()),
          div("Subtitle", conv(title.group(3)).strip())]
    for name in re.findall(r"\\input\{sections/(\w+)\}", main):
        md += blocks((SECTIONS / f"{name}.tex").read_text(encoding="utf-8"), conv)
    return "\n\n".join(md) + "\n"


# --------------------------------------------------------------------------
# 3. Reference document (styles) and pandoc
# --------------------------------------------------------------------------
COL = {"Teal": "2A7072", "Navy": "1F3A5F", "Orange": "C8641E", "Green": "3B6E3B", "Plum": "6A3D6E"}
TINT = {"Teal": 0.07, "Navy": 0.06, "Orange": 0.07, "Green": 0.07, "Plum": 0.06}
SERIF, SANS = "Cambria", "Calibri"


def tint(hexcol, a):
    rgb = [int(hexcol[i:i + 2], 16) for i in (0, 2, 4)]
    return "".join(f"{round(255 - (255 - c) * a):02X}" for c in rgb)


def pstyle(sid, name, ppr="", rpr="", based="Normal", nxt=None):
    return (f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="{sid}"><w:name w:val="{name}"/>'
            f'<w:basedOn w:val="{based}"/>' + (f'<w:next w:val="{nxt}"/>' if nxt else "") +
            f'<w:qFormat/><w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>')


def fonts(f):
    return f'<w:rFonts w:ascii="{f}" w:hAnsi="{f}" w:cs="{f}" w:eastAsia="{f}"/>'


def set_style(xml, sid, ppr=None, rpr=None):
    """Replace pPr/rPr of an existing style (adds them if missing)."""
    m = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % re.escape(sid), xml, flags=re.S)
    if not m:
        return xml
    st = m.group(0)
    for tag, val in (("pPr", ppr), ("rPr", rpr)):
        if val is None:
            continue
        new = f"<w:{tag}>{val}</w:{tag}>"
        if re.search(rf"<w:{tag}>.*?</w:{tag}>|<w:{tag}/>", st, flags=re.S):
            st = re.sub(rf"<w:{tag}>.*?</w:{tag}>|<w:{tag}/>", new, st, count=1, flags=re.S)
        else:
            st = st.replace("</w:style>", new + "</w:style>")
    return xml[:m.start()] + st + xml[m.end():]


def reference_docx():
    ref = BUILD / "reference.docx"
    default = BUILD / "default_reference.docx"
    subprocess.run([PANDOC, "-o", str(default), "--print-default-data-file", "reference.docx"], check=True)
    zin = zipfile.ZipFile(io.BytesIO(default.read_bytes()))
    styles = zin.read("word/styles.xml").decode("utf-8")
    body = (f'{fonts(SERIF)}<w:sz w:val="22"/><w:color w:val="222222"/>')
    styles = set_style(styles, "Normal", None, body)
    for sid in ("BodyText", "FirstParagraph", "Compact"):
        sp = '<w:spacing w:before="0" w:after="120" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/>'
        if sid == "Compact":
            sp = '<w:spacing w:before="20" w:after="40"/><w:jc w:val="left"/>'
        styles = set_style(styles, sid, sp, None)
    navy = '<w:color w:val="1F3A5F"/>'
    styles = set_style(styles, "Heading1", '<w:keepNext/><w:spacing w:before="360" w:after="120"/>',
                       f'{fonts(SANS)}<w:b/><w:sz w:val="32"/>{navy}')
    styles = set_style(styles, "Heading2", '<w:keepNext/><w:spacing w:before="200" w:after="60"/>',
                       f'{fonts(SANS)}<w:b/><w:sz w:val="25"/>{navy}')
    styles = set_style(styles, "Heading3", '<w:keepNext/><w:spacing w:before="160" w:after="40"/>',
                       f'{fonts(SANS)}<w:b/><w:sz w:val="22"/>{navy}')
    styles = set_style(styles, "Title", '<w:spacing w:before="0" w:after="60"/>',
                       f'{fonts(SANS)}<w:b/><w:sz w:val="56"/>{navy}')
    styles = set_style(styles, "Subtitle",
                       '<w:pBdr><w:bottom w:val="single" w:sz="18" w:space="6" w:color="C8641E"/></w:pBdr>'
                       '<w:spacing w:before="0" w:after="240"/>',
                       f'{fonts(SANS)}<w:sz w:val="30"/><w:color w:val="5F5F5F"/>')
    styles = set_style(styles, "FootnoteText", '<w:spacing w:before="0" w:after="40"/>',
                       f'{fonts(SANS)}<w:sz w:val="17"/><w:color w:val="5F5F5F"/>')
    styles = set_style(styles, "ImageCaption", None, f'{fonts(SANS)}<w:sz w:val="19"/>')
    styles = set_style(styles, "CaptionedFigure", '<w:keepNext/><w:jc w:val="center"/>', None)
    new = [
        pstyle("Kicker", "Kicker", '<w:spacing w:before="0" w:after="60"/>',
               f'{fonts(SANS)}<w:b/><w:sz w:val="19"/><w:color w:val="C8641E"/>'),
        pstyle("CaptionLabel", "Caption Label", '<w:spacing w:before="60" w:after="20"/>',
               f'{fonts(SANS)}<w:sz w:val="19"/><w:color w:val="222222"/>'),
        pstyle("CaptionNote", "Caption Note", '<w:spacing w:before="0" w:after="20"/>',
               f'{fonts(SANS)}<w:sz w:val="19"/>'),
        pstyle("FigureSource", "Figure Source", '<w:spacing w:before="0" w:after="160"/>',
               f'{fonts(SANS)}<w:sz w:val="16"/><w:color w:val="5F5F5F"/>'),
        pstyle("KeyTerm", "Key Term",
               '<w:pBdr><w:left w:val="single" w:sz="12" w:space="6" w:color="1F3A5F"/></w:pBdr>'
               '<w:spacing w:before="0" w:after="120"/><w:ind w:left="4200"/>',
               f'{fonts(SANS)}<w:sz w:val="17"/><w:color w:val="222222"/>'),
    ]
    for name, col in COL.items():
        bg = tint(col, TINT[name])
        border = f'<w:pBdr><w:left w:val="single" w:sz="24" w:space="8" w:color="{col}"/></w:pBdr>'
        new.append(pstyle(f"Box{name}", f"Box {name}",
                          border + f'<w:shd w:val="clear" w:color="auto" w:fill="{bg}"/>'
                          '<w:spacing w:before="0" w:after="80"/><w:ind w:left="240" w:right="120"/>',
                          f'{fonts(SANS)}<w:sz w:val="20"/>'))
        new.append(pstyle(f"Box{name}Heading", f"Box {name} Heading",
                          border + f'<w:keepNext/><w:shd w:val="clear" w:color="auto" w:fill="{col}"/>'
                          '<w:spacing w:before="200" w:after="80"/><w:ind w:left="240" w:right="120"/>',
                          f'{fonts(SANS)}<w:sz w:val="20"/><w:color w:val="FFFFFF"/>'))
    styles = styles.replace("</w:styles>", "".join(new) + "</w:styles>")
    with zipfile.ZipFile(ref, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            buf = styles.encode("utf-8") if item.filename == "word/styles.xml" else zin.read(item.filename)
            zout.writestr(item, buf)
    return ref


def footnote_symbols(path):
    """Footnote marks *, †, ‡ restarting on each page (numbers are used by citations)."""
    tmp = path.with_suffix(".tmp")
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/settings.xml":
                s = data.decode("utf-8")
                fp = '<w:numFmt w:val="chicago"/><w:numRestart w:val="eachPage"/>'
                if "<w:footnotePr>" in s:
                    s = s.replace("<w:footnotePr>", "<w:footnotePr>" + fp, 1)
                elif "<w:compat" in s:
                    s = s.replace("<w:compat", f"<w:footnotePr>{fp}</w:footnotePr><w:compat", 1)
                else:
                    s = s.replace("</w:settings>", f"<w:footnotePr>{fp}</w:footnotePr></w:settings>")
                data = s.encode("utf-8")
            if item.filename == "word/document.xml":
                s = data.decode("utf-8")
                # pandoc writes its own footnotePr (restart each section); replace it
                s = re.sub(r"(<w:sectPr[^>]*>.*?)<w:footnotePr>.*?</w:footnotePr>", r"\1", s, flags=re.S)
                s = re.sub(r"<w:sectPr([^>]*)>", r'<w:sectPr\1><w:footnotePr><w:numFmt w:val="chicago"/>'
                           r'<w:numRestart w:val="eachPage"/></w:footnotePr>', s)
                data = s.encode("utf-8")
            zout.writestr(item, data)
    tmp.replace(path)


def main():
    render_tikz()
    md = markdown()
    (BUILD / "chapter.md").write_text(md, encoding="utf-8")
    if WARN:
        print("not converted:", sorted(WARN))
    ref = reference_docx()
    fmt = "markdown-tex_math_dollars-raw_tex-citations-smart-auto_identifiers"
    r = subprocess.run([PANDOC, str(BUILD / "chapter.md"), "-f", fmt, "-t", "docx",
                        "--reference-doc", str(ref), "--resource-path", str(BOOK), "-o", str(OUT)],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr)
    if r.stderr.strip():
        print(r.stderr.strip())
    footnote_symbols(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
