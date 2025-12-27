from main import *

if __name__ == "__main__":
    svg_path = "./svgs/latex-e2d23abe3d27dcf725d3310f524cab6b5418307b.svg"
    text = r"Og=:-)ntLA	Lernen::Stochastik II::2. Discrete time martingales::2.1 Definition and first properties	Basic properties of a martingale	\begin{enumerate}[label=\alph*)]<br>\item $\mathbb{E}(X_n | \mathcal{F}_m) = X_m$ for $m \leq n$<br>\item $\mathbb{E}(X_n) = \mathbb{E}(X_0)$<br>\item $Y_n := \sum_{k=1}^n H_k (X_k - X_{k-1})$, $Y_0 = 0$ where $H$ is a bounded, predictable process, is a martingale<br>\end{enumerate}				"
    note = get_note(text)
    note = preprocess_note(note)
    print(note)
    with open(svg_path, "r") as file:
        ids = parse_svg_file(file)
        symbol_filter = generate_symbol_filter(ids)
        print(matches(symbol_filter, note.back))
