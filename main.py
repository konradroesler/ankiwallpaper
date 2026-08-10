import hashlib 

def extract_latex(text):
    # Find [latex], [$], [$$]
    # Construct canonical LaTeX
    # Normalize HTML
    # Return normalized LaTeX
    pass

def strip_html_for_latex(html):
    # Reproduce Anki's LATEX_NEWLINES behavior
    # Reproduce Anki's strip_html()
    pass

def latex_filename(latex, svg=False):
    normalized = strip_html_for_latex(latex)
    digest = hashlib.sha1(
        normalized.encode("utf-8")
    ).hexdigest()

    ext = "svg" if svg else "png"
    return f"latex-{digest}.{ext}"

if __name__ == "__main__":
    pass