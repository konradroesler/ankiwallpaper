import subprocess
from pathlib import Path

line = r"Markov chain	$\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)$"
fields = line.split('\t')
for field in fields:
    print(field)
latex = r"""
\documentclass[20pt,border=20pt]{standalone}
\usepackage{graphicx}
\usepackage{bbold,enumitem}
\usepackage{mathrsfs}
\usepackage{xcolor}
\pagecolor{black}
\color{white}
\pagestyle{empty}

\begin{document}
\scalebox{5}{
""" + rf"""
{fields[0]}
""" + r"""
}
\par
\vspace{50pt}
\scalebox{5}{
""" + rf"""
{fields[1]}
""" + r"""
}
\end{document}
"""

Path("render.tex").write_text(latex)

# Compile LaTeX to PDF
subprocess.run(["pdflatex", "render.tex"], check=True)

# Convert PDF to PNG (ImageMagick)
subprocess.run([
    "magick", "render.pdf",
    "-background", "black",
    # "-gravity", "center",
    "-extent", "1920x1080",
    "-density", "300", 
    "-quality", "100",
    "render.png"
], check=True)
