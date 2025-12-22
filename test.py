import re
import manim as mn
import src.aw_tokens as aw_tokens

line = r"Raileigh-Ritzsches Variationsprinzip	$$\mathcal{E}_0 \leq \frac{\langle \Psi | \hat{H} | \Psi \rangle}{\langle \Psi | \Psi \rangle}$$			"
line = r"Orthogonal projection of $Y$ onto $K$	$K \subset L^2 (\Omega, \mathcal{F}, \mathbb{P})$ closed, $Y \in L^2 (\Omega, \mathcal{F}, \mathbb{P})$. There exists a $\mathbb{P}$-a.s. unique $\hat{Y} \in K$, s.t. <br>\begin{enumerate}[label=(\roman*)]<br>&nbsp; &nbsp; \item $\left\| Y - \hat{Y} \right\| = d(Y, K) = \inf \{\left\| Y - X\right\|_2 : X \in K\}$<br>&nbsp; &nbsp; \item $Y - \hat{Y} \perp X$ for all $X \in K$, i.e. $Y - \hat{Y} \in K^\perp$ <br>\end{enumerate}<br>$\hat{Y}$ is called the orthogonal projection of $Y$ onto $K$.			"

tokens = aw_tokens.tex_environment_split(line)
print(tokens)
