"""
Search for substrings _term1^term2 where term1 and term2
are valid terms, i.e.
\\command,
\\command{arg1}{arg2} or
{something} OR
a single character.

We have a single character sub/superscript, if that character
is not a backslash, or brace open. The next should not matter then
"""

if __name__ == "__main__":
    text = r"Og=:-)ntLA	Lernen::Stochastik II::2. Discrete time martingales::2.1 Definition and first properties	Basic properties of a martingale	\begin{enumerate}[label=\alph*)]<br>\item $\mathbb{E}(X_n | \mathcal{F}_m) = X_m$ for $m \leq n$<br>\item $\mathbb{E}(X_n) = \mathbb{E}(X_0)$<br>\item $Y_n := \sum_{k=1}^n H_k (X_k - X_{k-1})$, $Y_0 = 0$ where $H$ is a bounded, predictable process, is a martingale<br>\end{enumerate}				"
    for i in range(text):
        if text[i] == "_":
            for 
