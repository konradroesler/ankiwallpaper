from main import *

if __name__ == "__main__":
    svg_path = "./svgs/latex-70486d7fdafb0ed77d545542b8c434200c389f4a.svg"
    text = r"H9DPA%>BnC	Lernen::Stochastik II::1. Conditional expectations::1.1 Lp-spaces	Orthogonal projection of $Y$ onto $K$	$K \subset L^2 (\Omega, \mathcal{F}, \mathbb{P})$ closed, $Y \in L^2 (\Omega, \mathcal{F}, \mathbb{P})$. There exists a $\mathbb{P}$-a.s. unique $\hat{Y} \in K$, s.t. <br>\begin{enumerate}[label=(\roman*)]<br>&nbsp; &nbsp; \item $\left\| Y - \hat{Y} \right\| = d(Y, K) = \inf \{\left\| Y - X\right\|_2 : X \in K\}$<br>&nbsp; &nbsp; \item $Y - \hat{Y} \perp X$ for all $X \in K$, i.e. $Y - \hat{Y} \in K^\perp$ <br>\end{enumerate}<br>$\hat{Y}$ is called the orthogonal projection of $Y$ onto $K$.				"
    note = get_note(text)
    note = preprocess_note(note)
    print(note)
    with open(svg_path, "r") as file:
        ids = parse_svg_file(file)
        symbol_filter = generate_symbol_filter(ids)
        print(matches(symbol_filter, note.back))
    print(get_uppercase_in_latex_commands(note.back))
