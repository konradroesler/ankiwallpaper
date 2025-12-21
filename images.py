import manim as mn
import src.ankiwallpaper as aw

class Image0(mn.Scene):
    def construct(self):
        line = r"Raileigh-Ritzsches Variationsprinzip	$$\mathcal{E}_0 \leq \frac{\langle \Psi | \hat{H} | \Psi \rangle}{\langle \Psi | \Psi \rangle}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image1(mn.Scene):
    def construct(self):
        line = r"Convergence in $L^p$	$X_n, X \in L^p$ and $$\lVert X_n \rVert_{L^p} \to \lVert X \rVert_{L^p}$$			(Stochastik II)"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image2(mn.Scene):
    def construct(self):
        line = r"$X_n \stackrel{L^p}{\to} X \implies \dots$	$$X_n \stackrel{p}{\to} X$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image3(mn.Scene):
    def construct(self):
        line = r"Orthogonal projection of $Y$ onto $K$	$K \subset L^2 (\Omega, \mathcal{F}, \mathbb{P})$ closed, $Y \in L^2 (\Omega, \mathcal{F}, \mathbb{P})$. There exists a $\mathbb{P}$-a.s. unique $\hat{Y} \in K$, s.t. <br>\begin{enumerate}[label=(\roman*)]<br>&nbsp; &nbsp; \item $\left\| Y - \hat{Y} \right\| = d(Y, K) = \inf \{\left\| Y - X\right\|_2 : X \in K\}$<br>&nbsp; &nbsp; \item $Y - \hat{Y} \perp X$ for all $X \in K$, i.e. $Y - \hat{Y} \in K^\perp$ <br>\end{enumerate}<br>$\hat{Y}$ is called the orthogonal projection of $Y$ onto $K$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image4(mn.Scene):
    def construct(self):
        line = r"Conditional expectation of $X$ given $\mathcal{G}$	$\mathcal{G}$ sub-$\sigma$-field, $X \geq 0$ or $X \in L^1$. Then $Y \geq 0$ or $Y \in L^1$ with<br>\begin{enumerate}[label=(\roman*)]<br>&nbsp; &nbsp; \item $Y$ is $\mathcal{G}$-measurable<br>&nbsp; &nbsp; \item $\mathbb{E}(Y \mathbb{1}_G) = \mathbb{E}(X \mathbb{1}_G) \ \forall G \in \mathcal{G}$<br>\end{enumerate}<br>is called (a version of) the conditional expectation of $X$ given $\mathcal{G}$. \\ \\ Notation: $\mathbb{E}(X | \mathcal{G}) := Y$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image5(mn.Scene):
    def construct(self):
        line = r"Factorization Lemma	Let $Z$ be an $(E, \mathcal{E})$-valued r.v. and $Y$ a real valued random variable. Then $Y$ is $\sigma(Z)$-m.b. iff there is a $\mathcal{E}$-$\mathcal{B}(\mathbb{R})$-m.b. function $h$ s.t. $Y=h(Z)$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image6(mn.Scene):
    def construct(self):
        line = r"Existence of $\mathbb{E}(X|\mathcal{G})$	$\mathcal{G} \subset \mathcal{F}$ sub-$\sigma$-field, $X \geq 0$ or $X \in L^1(\Omega, \mathcal{F}, \mathbb{P})$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image7(mn.Scene):
    def construct(self):
        line = r"$\mathbb{E}(X|Z)$	$$\mathbb{E}(X|\sigma(Z))$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image8(mn.Scene):
    def construct(self):
        line = r"We can write $h$ satisfying $\mathbb{E}(X | Z) = h(Z)$ in open form, if ...	\begin{enumerate}[label=(\roman*)]<br>\item $Z$ is discrete;<br>\item $(X, Z)$ has a joint density;<br>\item $X$ is of the form $X = g(Y, Z)$ and $Y, Z$ are independent.<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image9(mn.Scene):
    def construct(self):
        line = r"$Y, Z$ independent, then: $\mathbb{E}(g(Y, Z) | Z) =&nbsp;\dots$	$$\mathbb{E}(g(Y, z)) \rvert_{z = Z}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image10(mn.Scene):
    def construct(self):
        line = r"Properties of the conditional expectance	$\mathcal{G} \subset \mathcal{F}$, $X, Y \geq 0$ or $X, Y \in L^1$. Then<br>\begin{enumerate}<br>\item $\mathbb{E}(\mathbb{E}(X | \mathcal{G})) = \mathbb{E}(X)$<br>\item $X, Y \in L^1 \implies \mathbb{E}(a X + b Y | \mathcal{G}) = a \mathbb{E}(X | \mathcal{G}) + b \mathbb{E}(X | \mathcal{G})$<br>\item $X \leq Y$ a.s. $\implies \mathbb{E}(X | \mathcal{G}) \leq \mathbb{E}(Y | \mathcal{G})$ a.s.<br>\item $Y$ $\mathcal{G}$-m.b. and either $X, Y \geq 0$ a.s. or $X, Y, XY \in L^1$, then $\mathbb{E}(XY | \mathcal{G}) = Y \cdot \mathbb{E}(X | \mathcal{G})$ a.s.<br>\item $\mathbb{E}(X | \mathcal{G}) = X$ a.s. $\iff X$ is $\mathcal{G}$-m.b.<br>\item $X$ independent of $\mathcal{G} \implies \mathbb{E}(X | \mathcal{G}) = \mathbb{E}(X)$<br>\item Tower property: $\mathcal{H} \subset \mathcal{G} \subset \mathcal{F}$, then $\mathbb{E}(\mathbb{E}(X | \mathcal{G}) | \mathcal{H}) = \mathbb{E}(X | \mathcal{H})$ a.s.<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image11(mn.Scene):
    def construct(self):
        line = r"$H \leq G$	\begin{enumerate}[label=\alph*)]<br>\item $e \in H$<br>\item $g \circ h \in H$ und $h^{-1} \in H \ \forall g, h \in H$<br>\end{enumerate}<br>oder&nbsp;<br>\begin{enumerate}[label=\alph*)]<br>\item $H \neq \varnothing$<br>\item $g \circ h^{-1} \in H \ \forall g, h \in H$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image12(mn.Scene):
    def construct(self):
        line = r"Unterguppen derselben Gruppe sind [...]stabil	schnittstabil<br>$$H := \bigcap_{i \in I} H_i \leq G$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image13(mn.Scene):
    def construct(self):
        line = r"$\langle S \rangle \leq G$ ist eindeutig	\begin{enumerate}[label=\alph*)]<br>\item $S \subset \langle S \rangle$<br>\item $H \leq G$ und $S \subset H \implies \langle S \rangle \subset H$<br>\end{enumerate}<br>$$\langle S \rangle&nbsp; = \left\{\prod_{i=1}^k s_i | k \in \mathbb{N}_0, s_i \in S \cup S^{-} \right\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image14(mn.Scene):
    def construct(self):
        line = r"$G$ endlich erzeugt	$$G = \langle g_1, \dots, g_n \rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image15(mn.Scene):
    def construct(self):
        line = r"$G$ zyklisch	$$G = \langle g \rangle$$<br>$$g^n := \begin{cases} 1, &amp; n=0 \\ g \cdot g^{n-1}, &amp; n&gt;0 \\ g \cdot g^{n+1}, &amp; n&lt;0 \end{cases}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image16(mn.Scene):
    def construct(self):
        line = r"Zyklische Gruppen sind [...]	abelsch			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image17(mn.Scene):
    def construct(self):
        line = r"Homomorphismus	$$f(g \circ h) = f(g) \cdot f(h)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image18(mn.Scene):
    def construct(self):
        line = r"Monomorphismus	injektiver Homomorphismus, $G \hookrightarrow H$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image19(mn.Scene):
    def construct(self):
        line = r"Epimorphismus	surjektiver Homomorphismus, $G \twoheadrightarrow H$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image20(mn.Scene):
    def construct(self):
        line = r"Isomorphismus	bijektiver Homomorphismus, $G \simeq H$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image21(mn.Scene):
    def construct(self):
        line = r"Endomorphismus	Homomorphismus von $G$ in $G$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image22(mn.Scene):
    def construct(self):
        line = r"Automorphismus	bijektiver Endomorphismus			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image23(mn.Scene):
    def construct(self):
        line = r"$\varphi(e_G) =$	$$e_H$$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image24(mn.Scene):
    def construct(self):
        line = r"$\varphi(g^{-1})$	$$(\varphi(g))^{-1}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image25(mn.Scene):
    def construct(self):
        line = r"Die Verkettung von Homomorphismen ist ein	Homomorphismus			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image26(mn.Scene):
    def construct(self):
        line = r"Das Inverse eines Isomorphismus ist ein	Isomorphismus			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image27(mn.Scene):
    def construct(self):
        line = r"$(\text{Aut}, \circ)$ bildet eine&nbsp;	Gruppe			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image28(mn.Scene):
    def construct(self):
        line = r"Kern	$$\text{ker}(f) := \{g \in G | f(g) = 1\} \subset G`$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image29(mn.Scene):
    def construct(self):
        line = r"Bild	$$\text{im}(f) := \{f(g) \in H | g \in G\} \subset H$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image30(mn.Scene):
    def construct(self):
        line = r"exakte Sequenz	$$\text{ker}(f_i) = \text{im}(f_{i-1})$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image31(mn.Scene):
    def construct(self):
        line = r"$\text{ker}(f)$ und $\text{im}(f)$ sind&nbsp;	Untergruppen	Dies gilt für explizit für Gruppenhomomorphismen, im Allgemeinen jedoch nicht für z.B. Ringhomomorphismen		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image32(mn.Scene):
    def construct(self):
        line = r"$f$ Monomorphismus gdw	$$\text{ker}(f) = {1}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image33(mn.Scene):
    def construct(self):
        line = r"$f$ Epimorphismus gdw	$$\text{im}(f) = H$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image34(mn.Scene):
    def construct(self):
        line = r"$\varphi_g$ für $(G, \circ)$	$$\varphi_g: (\mathbb{Z}, +) \to (G, \circ) \ \text{mit} \ \varphi_g(1) = g$$<br>ist eindeutig. $\varphi_g(m) = g^m$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image35(mn.Scene):
    def construct(self):
        line = r"$\text{im}(\varphi_g)$	$$\langle g \rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image36(mn.Scene):
    def construct(self):
        line = r"$\forall g \in G \exists! m \in \mathbb{N}_0$ mit&nbsp;	$$g^k = 1 \iff k \in m\mathbb{Z}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image37(mn.Scene):
    def construct(self):
        line = r"$\text{ord}(g)$	$$\text{ord}(g) := |\langle g \rangle| = \begin{cases} m &amp; \text{falls ker}(\varphi_g) = m\mathbb{Z} \neq 0 \\ 0 &amp; \text{falls ker}(\varphi_g) = 0$$ \end{cases}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image38(mn.Scene):
    def construct(self):
        line = r"Banach space	complete normed Vector space			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image39(mn.Scene):
    def construct(self):
        line = r"sup-norm	$$\lVert f \rVert_{C^0} := \sup_{t \in [a, b]} |f(t)|$$<br>$C^0$-norm			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image40(mn.Scene):
    def construct(self):
        line = r"bounded	$$\lVert A x \rVert \leq c \lVert x \rVert$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image41(mn.Scene):
    def construct(self):
        line = r"A linear map $A: X \to Y$ between normed vector spaces is continuous if and only if it is [...]	bounded			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image42(mn.Scene):
    def construct(self):
        line = r"linear operator	linear map			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image43(mn.Scene):
    def construct(self):
        line = r"operator Norm	$$\lVert \cdot \rVert_{L(V, W)}$$<br>$$\lVert A \rVert_{L(V, W)} := \sup_{\lVert x \rVert_V = 1} \lVert A x \rVert_W$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image44(mn.Scene):
    def construct(self):
        line = r"If $Y$ is complete, then so is [...]	$$\mathcal{L}(X, Y)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image45(mn.Scene):
    def construct(self):
        line = r"$\mathcal{L}(X, X)$ with [...] is [...] if X is [...]	the operator norm, Banach space, Banach space			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image46(mn.Scene):
    def construct(self):
        line = r"$X$ Banach space, $A \in \mathcal{L}(X)$ with $\lVert A \rVert &lt; 1$, then	$(\mathbb{1} + A)^{-1} \in \mathcal{L}(X)$ is bounded			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image47(mn.Scene):
    def construct(self):
        line = r"$X, Y$ Banach spaces, $A \in \mathcal{L}(X, Y)$ has bounded inverse, then	$A + B$ has bounded inverse for sufficiently small $\lVert B \rVert$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image48(mn.Scene):
    def construct(self):
        line = r"$C^m$-norm	$$\lVert f \rVert_{C^m} := \sum_{|\alpha| \leq m} <br>\lVert \partial^\alpha f \rVert_{C^0}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image49(mn.Scene):
    def construct(self):
        line = r"Für $E[\psi]:= \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle}$ gilt $\delta E = 0$ gdw	$|\psi\rangle$ ist Eigenzustand von $\hat{H}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image50(mn.Scene):
    def construct(self):
        line = r"$\sigma(Z)$ for discrete $Z$	$$\sigma(Z^{-1}(z_1), \dots, Z^{-1}(z_n))$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image51(mn.Scene):
    def construct(self):
        line = r"$\mathbb{E}(X | \mathcal{G})$ for a disjoint decomposition of $\Omega$ where $\mathcal{G} = \sigma(A_1, ..., A_n)$	$$\sum_{i = 1}^n \frac{\mathbb{E}(X \mathbb{1}_{A_i})}{\mathbb{P}(A_i)} \mathbb{1}_{A_i}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image52(mn.Scene):
    def construct(self):
        line = r"$\text{Var}(X|\mathcal{G})$	$$\mathbb{E}((X - \mathbb{E}(X|\mathcal{G}))^2|\mathcal{G})$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image53(mn.Scene):
    def construct(self):
        line = r"(conditional) variance decomposition	$$\text{Var}(X) = \mathbb{E}(\text{Var}(X|\mathcal{G})) + \text{Var}(\mathbb{E}(X|\mathcal{G}))$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image54(mn.Scene):
    def construct(self):
        line = r"Banach algebra	additional product satisfying $$\lVert x y \rVert \leq \lVert x \rVert \cdot \lVert y \rVert$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image55(mn.Scene):
    def construct(self):
        line = r"$C_b^m (\Omega)$	$$f \in C^m (\Omega), \lVert f \rVert_{C^m} &lt; \infty$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image56(mn.Scene):
    def construct(self):
        line = r"$f_k \stackrel{C^m}{\to} f$	The partial derivatives of $f_k$ converge uniformly to the partial derivatives of $f$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image57(mn.Scene):
    def construct(self):
        line = r"$C^m_b (\Omega)$ with the $C^m$-norm is a&nbsp;	Banach space			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image58(mn.Scene):
    def construct(self):
        line = r"$f_k \stackrel{C^\infty}{\to} f$	$\partial^\alpha f_k$ converges uniformly to $\partial^\alpha f$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image59(mn.Scene):
    def construct(self):
        line = r"$f_k \stackrel{C^m_{\text{loc}}}{\to} f$	$$f_k \stackrel{C^j (K)}{\to} f$$&nbsp;<br>for all $j \leq m$ and $K \subset \Omega$ compact			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image60(mn.Scene):
    def construct(self):
        line = r"topological vector space	$(X, \mathcal{T})$ with continuous addition and scalar multiplication			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image61(mn.Scene):
    def construct(self):
        line = r"norm equivalence&nbsp;	$$\frac{1}{c} \lVert f \rVert_0 \leq \lVert f \rVert_1 \leq c \lVert f \rVert_0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image62(mn.Scene):
    def construct(self):
        line = r"semi norm	scalar linearity and triangle inequality hold			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image63(mn.Scene):
    def construct(self):
        line = r"locally convex space	vector space with the topology induced by&nbsp;<br>$$B^{\alpha}_R (x_0). \quad x_0 \in X, R&gt;0, \alpha \in I$$<br>where $(\lVert \cdot \rVert_\alpha)_{\alpha \in I}$ is a family of seminorms where $\lVert x \rVert_{\alpha} = 0$ for all $\alpha \in I$ implies $x = 0$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image64(mn.Scene):
    def construct(self):
        line = r"convergence in LCS	$$\lVert x - x_n \rVert_{\alpha} \to 0$$<br>for all $\alpha \in I$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image65(mn.Scene):
    def construct(self):
        line = r"open in LCS	there exists a finite $I_0 \subset I$ and $\epsilon_{\alpha}$ so that&nbsp;<br>$$\{ x \in X | \lVert x - x_0 \rVert_{\alpha} &lt; \epsilon_{\alpha} \ \text{for all} \ \alpha \in I_0\}$$<br>is contained in $U$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image66(mn.Scene):
    def construct(self):
        line = r"every LCS is a [...]	TVS			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image67(mn.Scene):
    def construct(self):
        line = r"monotone convergence	$$\mathbb{E}(X_n | \mathcal{G}) \uparrow \mathbb{E}(X | \mathcal{G}) \ \text{a.s.}$$<br>for $0 \leq X_n \uparrow X$ a.s.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image68(mn.Scene):
    def construct(self):
        line = r"Fatou's lemma&nbsp;	$$\mathbb{E}(\liminf_n X_n | \mathcal{G}) \leq \liminf_n \mathbb{E}(X_n | \mathcal{G}) \quad \text{a.s.}$$<br>for $X_n \geq 0$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image69(mn.Scene):
    def construct(self):
        line = r"dominated convergence&nbsp;	$$\mathbb{E}(X_n | \mathcal{G}) \to \mathbb{E}(X | \mathcal{G}) \quad \text{a.s.}$$<br>if $X_n \to X$ and $Z \in L^1(\Omega, \mathcal{F}, \mathbb{P}), Z \geq |X|$ exists			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image70(mn.Scene):
    def construct(self):
        line = r"Jensen's inequality	$$u(\mathbb{E}(X | \mathcal{G})) \leq \mathbb{E}(u(X) | \mathcal{G})$$<br>for $X \in L^1$ and convex $u(X) \in L^1$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image71(mn.Scene):
    def construct(self):
        line = r"Dynkin-system	\begin{enumerate}<br>\item $\Omega \in \mathcal{D}$<br>\item $A, B \in \mathcal{D}$ with $A \subset B$, then $B \setminus A \in \mathcal{D}$&nbsp;<br>\item $(A_n) \subset \mathcal{D}$ with $A_n \subset A_{n+1}$, then $\bigcup_n A_n \in \mathcal{D}$&nbsp;<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image72(mn.Scene):
    def construct(self):
        line = r"monotone class theorem	$\mathcal{E} \subset \mathcal{P}(\Omega)$ closed under finite intersection, $\mathcal{D}$ Dynkin system satisfying $\mathcal{E} \subset \mathcal{D} \subset \sigma(\mathcal{E})$, then $$\mathcal{D} = \sigma(\mathcal{E})$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image73(mn.Scene):
    def construct(self):
        line = r"monotone class theorem - vector version	$\mathcal{E} \subset \mathcal{P}(\Omega)$ closed under finite intersection, $\mathcal{H}$ vector space of functions from $\Omega$ to $\mathbb{R}$ such that&nbsp;<br>\begin{itemize}<br>\item $\mathbb{1}_E \in \mathcal{H} \ \text{for all} \ E \in \mathcal{E}$<br>\item if $(f_n) \subset \mathcal{H}$ with $0 \leq f_1 \leq f_2 \leq \dots$ and $f := \lim_n f_n$ is bounded, then $f \in \mathcal{H}$<br>\end{itemize}<br>Then $\mathcal{H}$ contains all $\sigma(\mathcal{E})$-measurable functions.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image74(mn.Scene):
    def construct(self):
        line = r"$\mathbb{E}(X \mathbb{1}_G) = \mathbb{E}(Y \mathbb{1}_G)$ for all $G \in \mathcal{G}$ is equivalent to	\begin{itemize}<br>\item $\mathcal{E}(X \mathbb{1}_G) = \mathbb{E}(Y \mathbb{1}_G)$ for all $G \in \mathcal{E}$ if $\sigma(\mathcal{E}) = \mathcal{G}$<br>\item $\mathbb{E}(X Z) = \mathbb{E}(Y Z)$ for all bdd $G$-msb rv $Z$<br>\end{itemize}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image75(mn.Scene):
    def construct(self):
        line = r"$\mathbb{Z}/n\mathbb{Z}$	$$\{[0],[1],\dots,[n-1]\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image76(mn.Scene):
    def construct(self):
        line = r"$gH$	$$\{gh | h \in H\}$$	Linksnebenklasse		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image77(mn.Scene):
    def construct(self):
        line = r"$aH \cap bH \neq \varnothing$ or equivalently $\dots$	\begin{itemize}<br>\item $aH = bH$<br>\item $a \in bH$<br>\item $b^{-1} a \in H$<br>\end{itemize}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image78(mn.Scene):
    def construct(self):
        line = r"$G$ ist darstellbar als [...]	disjunkte Vereinigung von Linksnebenklassen	$G$ Gruppe		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image79(mn.Scene):
    def construct(self):
        line = r"$G/H$	$$\{gH | g \in G \}$$	Menge aller Linksnebenklassen		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image80(mn.Scene):
    def construct(self):
        line = r"Repräsentantesystem der Linksnebenklassen	$$R \to G/H, g \mapsto g H$$&nbsp;<br>ist eine Bijektion für $R \subset G$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image81(mn.Scene):
    def construct(self):
        line = r"$[G : H]$	$$|G/H| = |R|$$<br>Index von $H$ in $G$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image82(mn.Scene):
    def construct(self):
        line = r"Satz von Lagrange	$$|G| = [G : H] \cdot |H|$$<br>für $H \leq G$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image83(mn.Scene):
    def construct(self):
        line = r"Für $H \leq G$ ist die Ordnung von [...] ein Teiler von [...]	$$H, |G|$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image84(mn.Scene):
    def construct(self):
        line = r"kleiner Fermat'scher Satz	$\text{ord}(g)$ ist Teiler von $|G|$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image85(mn.Scene):
    def construct(self):
        line = r"Jede Gruppe von Primzahlordnung ist [...]	zyklisch			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image86(mn.Scene):
    def construct(self):
        line = r"$\mathcal{H}$ independent of $\sigma(\sigma(X), \mathcal{G})$, then $\mathbb{E}(X | \sigma(\mathcal{H}, \mathcal{G}) = \dots$	$$\mathbb{E}(X | \mathcal{G}) \ \text{a.s.}$$	Sheet 1, 3 c)<br><br>To prove, use the monotone class theorem.		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image87(mn.Scene):
    def construct(self):
        line = r"If two random variables can be expressed as measurable functions of each other, they ...	generate the same $\sigma$-algebra			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image88(mn.Scene):
    def construct(self):
        line = r"Partitionierung von $\hat{H}$	$$\hat{H} = \hat{H}_0 + \lambda \hat{H}'_1$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image89(mn.Scene):
    def construct(self):
        line = r"Potenzreihenansatz bezüglich $\lambda$	\begin{align*}<br>E_n &amp;= E_n^{(0)} + \lambda \Delta \tilde{E}^{(1)}_n + \lambda^2 \Delta \tilde{E}_n^{(2)} + \dots \\<br>|n\rangle &amp;= |n^{(0)}\rangle + \lambda |\tilde{n}^{(1)}\rangle + \lambda^2 |\tilde{n}^{(2)}\rangle + \dots<br>\end{align*}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image90(mn.Scene):
    def construct(self):
        line = r"$\Delta \tilde{E}_n^{(1)}$	$$\langle n^{(0)} | \hat{H}'_1 | n^{(0)} \rangle$$	nicht entartete ungestörte Zustände		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image91(mn.Scene):
    def construct(self):
        line = r"$|\tilde{n}^{(1)}\rangle$	$$\sum_{n \neq m} \frac{\langle m^{(0)} | \hat{H}'_1 | n^{(0)} \rangle}{\hat{E}^{(0)}_m - \hat{E}^{(0)}_n} | m^{(0)} \rangle$$	Die Korrektur erster Ordnung des Zustandsvektors<br><br>nicht entartete ungestörte Zustände		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image92(mn.Scene):
    def construct(self):
        line = r"$|n^{(1)}\rangle$	$$|n^{(0)}\rangle + \lambda |\tilde{n}^{(1)}\rangle$$	Korrigierter Zustandsvektor mit Korrektur erster Ordnung<br><br>nicht entartete ungestörte Zustände		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image93(mn.Scene):
    def construct(self):
        line = r"$N \trianglelefteq G$	$$gN = Ng \ \forall g \in G$$	Normalteiler von G		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image94(mn.Scene):
    def construct(self):
        line = r"Zeitpropagationsoperator	$$|\psi(t)\rangle = \hat{U}(t,t_0) |\psi(t_0)\rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image95(mn.Scene):
    def construct(self):
        line = r"Mikroreversibilität	$$\hat{U}(t,t_0) \hat{U}(t_0,t) = \hat{I}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image96(mn.Scene):
    def construct(self):
        line = r"$\hat{U}(t,t_0)$ für $\hat{H}$ zeitunabhängig	$$e^{-\frac{i}{\hbar} \hat{H}(t-t_0)}$$	Folgt aus Def des Zeitpropagators und der Lösung der zeitabhängigen Schrödingergleichung		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image97(mn.Scene):
    def construct(self):
        line = r"$\hat{A}_H$	$$\hat{U}^\dag(t,t_0) \hat{A} \hat{U}(t,t_0)$$	Operator im Heisenberg Bild		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image98(mn.Scene):
    def construct(self):
        line = r"$|\psi_H\rangle$	$$\hat{U}^\dag(t,t_0)|\psi\rangle$$	Zustandsvektor im Heisenberg Bild. Der Erwartungswert bleibt dann erhalten.		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image99(mn.Scene):
    def construct(self):
        line = r"Heisenberg-Gleichung	$$\frac{d}{dt} \hat{A}_H = \frac{i}{\hbar}[\hat{H}_H, \hat{A}_H] + \frac{\partial \hat{A}_H}{\partial t}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image100(mn.Scene):
    def construct(self):
        line = r"regular conditional distribution $\mathbb{P}^X$	\begin{enumerate}[label=\alph*)]<br>\item $B \mapsto \mathbb{P}^X(\omega; B)$ is a probability measure on $(E, \mathcal{E})$ for each $\omega$<br>\item $\mathbb{P}^X(\cdot; B) = \mathbb{P}(X\in B|\mathcal{G})$ for each $B$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image101(mn.Scene):
    def construct(self):
        line = r"$\mathbb{P}(X\in B| \mathcal{G})$	$$\mathbb{E}(\mathbb{1}_B (X) | \mathcal{G})$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image102(mn.Scene):
    def construct(self):
        line = r"$\mathbb{E}(f(X)|\mathcal{G})(\omega)$	$$\int_E f(x) \mathbb{P}^X(\omega, dx) \ \text{for} \ \mathbb{P}\text{-a.a.} \ \omega \in \Omega$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image103(mn.Scene):
    def construct(self):
        line = r"Konjugationsabbildung	$$c_g: G \to G, x \mapsto gxg^{-1}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image104(mn.Scene):
    def construct(self):
        line = r"$N \trianglelefteq G$ gdw	\begin{enumerate}[label=\alph*)]<br>\item $\text{ker}(\varphi) = N$ für ein Gruppenhomomorphismus $\varphi: G \to H$<br>\item $p: G \to G/N, g \mapsto gN$ ist ein Gruppenhomomorphismus<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image105(mn.Scene):
    def construct(self):
        line = r"A regular conditional distribution of $X$ given $\mathcal{G}$ exists if ...	$(E, \mathcal{E})$ is a Borel space			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image106(mn.Scene):
    def construct(self):
        line = r"Borel space $(E, \mathcal{E})$	There exists a Borel set $A$ and a bijection $\psi: E \to A$ such that $\psi, \psi^{-1}$ are measurable	E-B(A)-mb, B(A)-E-mb		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image107(mn.Scene):
    def construct(self):
        line = r"Polish space	separable, completely metrizable topological space&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image108(mn.Scene):
    def construct(self):
        line = r"Kuratowski's theorem	If $E$ ist a Polish space, then $(E, \mathcal{B}(E))$ is a Borel space			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image109(mn.Scene):
    def construct(self):
        line = r"filtration	Increasing family of $\sigma$-algebras $(\mathcal{F}_n)_{n\in N_0}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image110(mn.Scene):
    def construct(self):
        line = r"$(X_n)$ is adapted to $(\mathcal{F}_n)$	$X_n$ is $\mathcal{F}_n$ measurable			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image111(mn.Scene):
    def construct(self):
        line = r"natural filtration of $(X_n)$&nbsp;	$$\mathcal{F}_n^X := \sigma(X_k | k \leq n)$$	smallest filtration where the process is adapted to the filtration		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image112(mn.Scene):
    def construct(self):
        line = r"predictable process	$X_n$ is $\mathcal{F}_{n-1}$-measurable			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image113(mn.Scene):
    def construct(self):
        line = r"filtered probability space&nbsp;	$$(\Omega, \mathcal{F}, (\mathcal{F}_n)_{n\in N_0}, \mathbb{P})$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image114(mn.Scene):
    def construct(self):
        line = r"$\mathcal{F}_{\infty}$	$$\sigma(\bigcup_{n \in \mathbb{N}} \mathcal{F}_n)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image115(mn.Scene):
    def construct(self):
        line = r"martingale	\begin{enumerate}[label=(\roman*)]<br>\item $(X_n)_{n\in N_0}$ is adapted to $(\mathcal{F}_n)_{n \in N_0}$<br>\item $X_n \in L^1(\mathbb{P})$<br>\item $\mathbb{E}(X_n | \mathcal{F}_{n-1}) = X_{n-1}$<br>\end{enumerate}	(X_n) is called a martingale with respect to (F_n) and P<br><br>(wording)		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image116(mn.Scene):
    def construct(self):
        line = r"submartingale	$$\mathbb{E}(X_n | \mathcal{F}_{n-1}) \geq X_{n-1}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image117(mn.Scene):
    def construct(self):
        line = r"supermartingale	$$\mathbb{E}(X_n | \mathcal{F}_{n-1}) \leq X_{n-1}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image118(mn.Scene):
    def construct(self):
        line = r"Basic properties of a martingale	\begin{enumerate}[label=\alph*)]<br>\item $\mathbb{E}(X_n | \mathcal{F}_m) = X_m$ for $m \leq n$<br>\item $\mathbb{E}(X_n) = \mathbb{E}(X_0)$<br>\item $Y_n := \sum_{k=1}^n H_k (X_k - X_{k-1})$, $Y_0 = 0$ where $H$ is a bounded, predictable process, is a martingale<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image119(mn.Scene):
    def construct(self):
        line = r"A LCS is metrizable if and only if ...	it's topology can be defined by a countable family of seminorms			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image120(mn.Scene):
    def construct(self):
        line = r"Frechet space	An LCS which topology can be defined via a \textbf{complete} metric			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image121(mn.Scene):
    def construct(self):
        line = r"continuous extensions of linear operators	&nbsp;A linear operator $A: X_0 \to Y$ into a Banach space $Y$ can be uniquely extended from a dense $X_0 \subset X$ to a normed vector space $X$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image122(mn.Scene):
    def construct(self):
        line = r"dual space	$$X^* := \mathcal{L}(X, \mathbb{K})$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image123(mn.Scene):
    def construct(self):
        line = r"transpose	$$A^* \in \mathcal{L}(Y^*, X^*), \ (A^* \lambda)(x) := \lambda (A x)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image124(mn.Scene):
    def construct(self):
        line = r"$\mathcal{T}: X \to X^{**}$	For all vec. spaces $X$ there exists a canonical bdd. op. $\mathcal{T}$ defined by<br>$$(\mathcal{T} x)(\lambda) := \lambda(x)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image125(mn.Scene):
    def construct(self):
        line = r"reflexive	$X$ Banach, $\mathcal{T}: X \to X^{**}$ isomorphism	X does not really have to be Banach, this definition makes sense for normed vector spaces		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image126(mn.Scene):
    def construct(self):
        line = r"Hamel basis	maximal independent subset $\{e_{\alpha}\}_{\alpha \in I}$, i.e.<br>$$x = \sum_{\alpha \in I} c_{\alpha} e_{\alpha}$$<br>with finite nonzero $c_{\alpha}$ for any $x$	this definition works for any vector space		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image127(mn.Scene):
    def construct(self):
        line = r"Hilbert space	complete inner product space $(H, \langle,\rangle)$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image128(mn.Scene):
    def construct(self):
        line = r"$W^\perp$	$$\{x \in H | \langle w, x \rangle = 0 \ \forall w \in W\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image129(mn.Scene):
    def construct(self):
        line = r"$H = W \oplus W^\perp$ iff	$H$ Hilbert space, $W \subset H$ closed			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image130(mn.Scene):
    def construct(self):
        line = r"closest point theorem	$H$ Banach. For all convex closed sets $K \subset H$, there exists a point closest to $K$ in $H \setminus K$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image131(mn.Scene):
    def construct(self):
        line = r"convex	sets:<br>$$\forall x,y \in K: tx + (1-t)y \in K \ \forall t \in [0,1]$$<br>functions:<br>$$\forall x,y \in K: f(tx + (1-t)y) \leq tf(x) + (1-t)f(y) \ \forall t \in [0,1]$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image132(mn.Scene):
    def construct(self):
        line = r"strictly convex (normed vector space)	$$t x+(1-t)y \in \bar{B} \setminus \partial \bar{B} \ \forall t \in (0,1)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image133(mn.Scene):
    def construct(self):
        line = r"uniformly convex (normed vector space)	$$\forall \epsilon &gt; 0 \exists \delta &gt; 0 \ \text{s.t.} \ x, y \in \bar{B} \ \text{with} \ \lVert x - y \rVert \geq \epsilon \implies \text{dist}(\frac{x+y}{2}, \partial B) \geq \delta$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image134(mn.Scene):
    def construct(self):
        line = r"Every inner product space is&nbsp;	uniformly convex			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image135(mn.Scene):
    def construct(self):
        line = r"closest point theorem 2	For uniformly convex Banach space $X$ and closed convex set $K \subset X$ and point $x \in X \setminus K$, $\exists! y \in K$ closest to $x$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image136(mn.Scene):
    def construct(self):
        line = r"orthonormal set	$$\forall v \in S: \lVert v \rVert = 1 \ \text{and} \ v, w \in S \ \text{with} \ v \neq w: \langle v, w \rangle = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image137(mn.Scene):
    def construct(self):
        line = r"Pythagorean theorem	$$\forall x \in H: x = \sum_{j=1}^n \langle e_j, x \rangle e_j + x' \ \text{for some} \ x' \in W^\perp$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image138(mn.Scene):
    def construct(self):
        line = r"$\Lambda_x$	$$\Lambda_x: H \to \mathbb{K}, \Lambda_x (y) := \langle x, y \rangle$$<br>is a bounded linear functional	3.8		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image139(mn.Scene):
    def construct(self):
        line = r"$W \subset H$ dense iff	$$W^\perp = \{0\}$$	H is a Hilbert space		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image140(mn.Scene):
    def construct(self):
        line = r"Riesz representation theorem	In a Hilbert space, the map $H \to H^*, x \mapsto \Lambda_x := \langle x, \cdot \rangle$ is a real-linear isomorphism.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image141(mn.Scene):
    def construct(self):
        line = r"adjoint	$$\langle y, A x \rangle = \langle A^* y , x\rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image142(mn.Scene):
    def construct(self):
        line = r"orthonormal basis	orthonormal set such that $\text{Span}(S) = \mathcal{H}$	orthonormal set of a Hilbert space&nbsp;		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image143(mn.Scene):
    def construct(self):
        line = r"An orthonormal set is a orthonormal basis iff&nbsp;	it is maximal			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image144(mn.Scene):
    def construct(self):
        line = r"$$x = \sum_{\alpha \in I_x} \langle e_\alpha, x \rangle e_\alpha$$	Every $x$ has this representation with a countable $I_x$ where the sum converges absolutely			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image145(mn.Scene):
    def construct(self):
        line = r"separable (metric space)	contains a countable dense subset			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image146(mn.Scene):
    def construct(self):
        line = r"The basis of a Hilbert space is at most countable iff	$\mathcal{H}$ is separable			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image147(mn.Scene):
    def construct(self):
        line = r"$|\Psi_W (t)\rangle$	$$\hat{U}^\dag_0 (t, t_0) |\Psi (t)\rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image148(mn.Scene):
    def construct(self):
        line = r"$\hat{A}_W$	$$\hat{U}^\dag_0 (t, t_0) \hat{A} \hat{U}_0 (t, t_0)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image149(mn.Scene):
    def construct(self):
        line = r"$\hat{U}_0 (t, t_0)$	$$e^{-\frac{i}{\hbar} \hat{H}_0 (t-t_0)}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image150(mn.Scene):
    def construct(self):
        line = r"Ehrenfest Theorem	$$\frac{d}{dt} \langle \hat{A} \rangle = \frac{i}{\hbar} \langle [\hat{H}, \hat{A}] \rangle + \frac{\partial}{\partial t} \langle \hat{A} \rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image151(mn.Scene):
    def construct(self):
        line = r"Nach dem Ehrenfest Theorem sind $\hat{A}$ Erhaltungsgrößen, wenn	$\hat{A}$ ist nicht explizit zeitabhängig und kommutiert mit $\hat{H}$<br>$$\frac{d}{dt} \langle \hat{A} \rangle = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image152(mn.Scene):
    def construct(self):
        line = r"Martingales under information reduction	Any $(\mathcal{F}_n)$ martingale is a $(\mathcal{G}_n)$ martingale if $\mathcal{G}_n \subset \mathcal{F}_n$ and $(X_n)$ is adapted to $(\mathcal{G}_n)$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image153(mn.Scene):
    def construct(self):
        line = r"Doob decomposition	Any submartingale $(X_n)$ can be decomposed into a martingale $(M_n)$ and a predictable increasing process $(A_n)$ where<br>$$X_n = X_0 + M_n + A_n$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image154(mn.Scene):
    def construct(self):
        line = r"stopping time (with respect to $(\mathcal{F}_n)$)	$$\tau: \Omega \to \bar{\mathbb{N}}_0 \ \text{where} \ \{\tau \leq n\} \in \mathcal{F}_n$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image155(mn.Scene):
    def construct(self):
        line = r"min/max of stopping times	$$\tau \wedge \sigma \ \text{and} \ \tau \vee \sigma \ \text{are stopping times}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image156(mn.Scene):
    def construct(self):
        line = r"characterization of a stopping time	$\tau$ is a stopping time iff $\{\tau = n\} \in \mathcal{F}_n$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image157(mn.Scene):
    def construct(self):
        line = r"$X^\tau_n (\omega)$	$$X_{n\wedge\tau(\omega)}(\omega)$$<br>which is a process adapted to $(\mathcal{F}_n)$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image158(mn.Scene):
    def construct(self):
        line = r"$X_\tau (\omega)$	$$X_{\tau(\omega)}(\omega)$$<br>which is a random variable&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image159(mn.Scene):
    def construct(self):
        line = r"Optional stopping theorem	If $X$ is a (sub-/super-)martingale, $X^\tau$ is also a (sub-/super-)martingale			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image160(mn.Scene):
    def construct(self):
        line = r"Expectance of bounded (super-)martingales and stopping times	$$\mathbb{E}(X_\tau) = \mathbb{E}(X_0)$$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image161(mn.Scene):
    def construct(self):
        line = r"Zeitordnungsoperator	$$\hat{\mathcal{T}}[\hat{A}(t) \hat{B}(t')] := \begin{cases} \hat{A}(t) \hat{B}(t') \ &amp;\text{für} \ t &gt; t' \\ \hat{B}(t') \hat{A}(t) \ &amp;\text{für} \ t' &gt; t \end{cases}$$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image162(mn.Scene):
    def construct(self):
        line = r"Dyson-Reihe für den Zeitentwicklungsoperator	$$\hat{U}(t, t_0) = \hat{\mathcal{T}}[e^{-\frac{i}{\hbar} \int_{t_0}^t dt' \hat{H}(t')}]$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image163(mn.Scene):
    def construct(self):
        line = r"innerer Automorphismus	Elemente eines Normalteilers von $\text{Aut(G)}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image164(mn.Scene):
    def construct(self):
        line = r"Zentrum	$$\{h \in G | g h = h g \ \forall g \in G\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image165(mn.Scene):
    def construct(self):
        line = r"Quotient	$$G/N$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image166(mn.Scene):
    def construct(self):
        line = r"$\text{SL}_n (\mathbb{R})$	$$\{A \in \text{GL}_n (\mathbb{R}) | \det A = 1\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image167(mn.Scene):
    def construct(self):
        line = r"$\text{SO}_n (\mathbb{R})$	$$\{A \in \text{SL}_n (\mathbb{R}) | A \cdot&nbsp; A^T = 1\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image168(mn.Scene):
    def construct(self):
        line = r"Erster Isomorphiesatz&nbsp;	$HN \leq G$ und&nbsp;<br>\begin{itemize}<br>\item $N \trianglelefteq HN$<br>\item $H \cap N \trianglelefteq H$<br>\item $H/H \cap N \simeq HN/N$ (Erweiterungsregel)<br>\end{itemize}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image169(mn.Scene):
    def construct(self):
        line = r"Zweiter Isomorphiesatz	Für $N, H \trianglelefteq G$, $N \subset H$ gilt&nbsp;<br>\begin{itemize}<br>\item $N \trianglelefteq H$&nbsp;<br>\item $H/N \trianglelefteq G/N$<br>\item $G/H \simeq (G/N)/(H/N)$ (Kürzungsregel)<br>\end{itemize}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image170(mn.Scene):
    def construct(self):
        line = r"Erweiterungsregel	$$H/H \cap N \simeq HN/N$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image171(mn.Scene):
    def construct(self):
        line = r"Kürzungsregel	$$G/H \simeq (G/N)/(H/N)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image172(mn.Scene):
    def construct(self):
        line = r"normale Hülle	$$\langle S^G\rangle \trianglelefteq G$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image173(mn.Scene):
    def construct(self):
        line = r"freie Gruppe	$$F_S := \{ \ \text{Wörter mit den Variablen aus} \ S \ \}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image174(mn.Scene):
    def construct(self):
        line = r"universelle Eigenschaft freier Gruppen	Für jede Abbildung $f: S \to G$ existiert eine Erweiterung zu einem Homomorphismus<br>$$\hat{f}: F_S \to G \ \text{mit} \ \hat{f}|_S = f$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image175(mn.Scene):
    def construct(self):
        line = r"Gruppe erzeugt von $x_1, \dots, x_n$ modulo den Relationen $r_1, \dots, r_m$	$S = \{x_1, \dots, x_n \}, R = \{ r_1, \dots, r_m \} \subset F := F_S$<br>$$\langle x_1, \dots, x_n | r_1 = \dots = r_m = 1\rangle := F/ \langle R^F \rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image176(mn.Scene):
    def construct(self):
        line = r"Präsentation	Angabe von Erzeugern $x_1, \dots, x_n$ und Relationen $r_1, \dots, r_m$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image177(mn.Scene):
    def construct(self):
        line = r"Präsentation einer zyklischen Gruppe	$$\langle x | x^n = 1\rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image178(mn.Scene):
    def construct(self):
        line = r"Wirkung von $(G, \circ)$ auf $M$	$$G \times M \to M, \ (g, m) \mapsto g \cdot m$$&nbsp;<br>mit&nbsp;<br>\begin{enumerate}[label=\alph*)]<br>\item $e \cdot m = m$<br>\item $(g_1 \circ g_2) \cdot m = g_1 \circ (g_2 \circ m))$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image179(mn.Scene):
    def construct(self):
        line = r"Martingale condition for bounded stopping times	$$\mathbb{E}(X_\tau) = \mathbb{E}(X_0) \ \text{for all bounded} \ \tau$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image180(mn.Scene):
    def construct(self):
        line = r"$\mathcal{F_\tau}$	$$\{A \in \mathcal{F} | A \cap \{\tau \leq n\} \in \mathcal{F}_n \ \forall n \in \mathbb{N}_0\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image181(mn.Scene):
    def construct(self):
        line = r"Basic properties of $\mathcal{F}_\tau$&nbsp;	\begin{enumerate}[label=\alph*)]<br>\item $\tau = n$, then $\mathcal{F}_\tau = \mathcal{F}_n$<br>\item $\sigma \leq \tau$, then $\mathcal{F}_\sigma \subset \mathcal{F}_\tau$<br>\item $\tau$ finite and $X$ adapted, then $X_\tau$ is $\mathcal{F}_\tau$-mb.<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image182(mn.Scene):
    def construct(self):
        line = r"closed martingale	$$X_n = \mathbb{E}(Y|\mathcal{F}_n) \ \text{for all} \ n \in \mathbb{N}_0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image183(mn.Scene):
    def construct(self):
        line = r"optional sampling theorem (unbounded $\tau, \sigma$)	$X$ closed by $Y$, $\sigma \leq \tau$ stopping times. Then<br>$$\mathbb{E}(X_\tau | \mathcal{F}_\sigma) = X_\sigma \ \text{a.s. and} \ \mathbb{E}(X_\tau) = \mathbb{E}(X_\infty) = \mathbb{E}(Y)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image184(mn.Scene):
    def construct(self):
        line = r"Linksabbildungen und Gruppenhomomorphismen	Es existiert eine Bijektion zwischen<br>$$\lambda: G \times M \to M \quad \text{und} \quad f: G \to \frak{S}_M := \{\text{bijektive Abbildungen} \ M \to M\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image185(mn.Scene):
    def construct(self):
        line = r"treu	Der Homomorphismus<br>$$G \to \frak{S}_M, g \mapsto g \cdot m$$<br>ist injektiv<br><br>$e_G$ ist das einzige Element, welches alle $m \in M$ fixiert.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image186(mn.Scene):
    def construct(self):
        line = r"Isomorphien zu $\frak{S}_n$&nbsp;	Jede endliche Gruppe der Ordnung $n$ ist zu einer Untergruppe von $\frak{S}_n$ isomorph	symmetrische Gruppe		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image187(mn.Scene):
    def construct(self):
        line = r"$\text{Stab}_G (m)$	$$G_m := \{g \in G| g \cdot m = m \}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image188(mn.Scene):
    def construct(self):
        line = r"frei&nbsp;	$$\text{Stab}_G (m) = \{e_G\} \ \text{für alle} \ m \in M$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image189(mn.Scene):
    def construct(self):
        line = r"Orbit von $m$	$$G \cdot m$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image190(mn.Scene):
    def construct(self):
        line = r"transitiv	$$\exists m \in M: G \cdot m = M$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image191(mn.Scene):
    def construct(self):
        line = r"Einfache Aussagen über Stabilisatoren und Orbits	\begin{enumerate}[label=\alph*)]<br>\item $G/\text{Stab}_G (m) \to G \cdot m, g \mapsto g \cdot m$ ist eine Bijektion<br>\item $\text{Stab}(g \cdot m) = g \text{Stab}(m) g^{-1}$ für alle $g \in G, m \in M$<br>\item $G \cdot m_1 \cap G \cdot m_2 \neq \varnothing \iff G \cdot m_1 = G \cdot m_2$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image192(mn.Scene):
    def construct(self):
        line = r"Bahnformel	$$|M| = \sum_{m \in R} |G \cdot m| \ \text{mit} \ |G \cdot m| = [G : \text{Stab}_G (m)]$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image193(mn.Scene):
    def construct(self):
        line = r"$M/G$&nbsp;	Menge der Bahnen			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image194(mn.Scene):
    def construct(self):
        line = r"$\text{Fix}(g)$&nbsp;	$$\{m \in M | g \in \text{Stab}_G (m)\}$$<br>Fixpunkte von $g$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image195(mn.Scene):
    def construct(self):
        line = r"Lemma von Burnside	$$|M/G| = \frac{1}{|G|} \sum_{g\in G} |\text{Fix}(g)|$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image196(mn.Scene):
    def construct(self):
        line = r"weak convergence	$$x_n \rightharpoonup x \iff \forall \Lambda \in E^*, \Lambda(x_n) \to \Lambda(x)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image197(mn.Scene):
    def construct(self):
        line = r"weak topology	locally convex topology generated by $\{\lVert x \rVert_{\Lambda} := |\Lambda(x)|\}_{\Lambda \in E^*}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image198(mn.Scene):
    def construct(self):
        line = r"weak $L^p$-convergence	$f_n$ is weakly $L^p$-convergent to $f$, iff<br>$$\int_X \langle g, f_n \rangle d\mu \to \int_X \langle g, f \rangle d\mu \ \forall g \in L^2(X)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image199(mn.Scene):
    def construct(self):
        line = r"weak$^*$-topology (on $E^*$)	locally convex topology generated by the seminorms $\{\lVert \Lambda \rVert_x := |\Lambda(x)|\}_{x\in E}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image200(mn.Scene):
    def construct(self):
        line = r"Banach-Alaoglu theorem (separable case)	In $E$ a separable Banach space, every bdd seq in $E^*$ has a weak$^*$-conv sub seq			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image201(mn.Scene):
    def construct(self):
        line = r"strong convergence out of weak convergence condition	$x_n \rightharpoonup x$ and $\lVert x_n \rVert \to \lVert x\rVert$, then $x_n \to x$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image202(mn.Scene):
    def construct(self):
        line = r"optional sampling theorem (bounded $\tau, \sigma$)	$X$ a martingale, then<br>$$\mathbb{E}(X_\tau | \mathcal{F}_\sigma) = X_\sigma \ \text{a.s.}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image203(mn.Scene):
    def construct(self):
        line = r"$P_{i \to f}(t)$	$$\langle i | \hat{P}_f | i \rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image204(mn.Scene):
    def construct(self):
        line = r"$\hat{P}_f$	$$|f\rangle \langle f |$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image205(mn.Scene):
    def construct(self):
        line = r"$\hat{U}^{(n)} (t, t_0)$	$$\frac{1}{n!} (-\frac{i}{\hbar})^n \int_{t_0}^t d\tau_1 \int_{t_0}^t d\tau_2 \dots \int_{t_0}^t d\tau_n \hat{\mathcal{T}}[\hat{H}(\tau_1) \hat{H}(\tau_2) \dots \hat{H}(\tau_n)]$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image206(mn.Scene):
    def construct(self):
        line = r"$|\psi_W^{(n)}(t)\rangle$	$$\hat{U}_W^{(n)} (t, t_0) | \varphi_i\rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image207(mn.Scene):
    def construct(self):
        line = r"$P_{i \to f}(t)$ in Näherung	$$|\sum_{j = 0}^\infty \mathcal{A}_{i \to f}^{(j)}|^2$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image208(mn.Scene):
    def construct(self):
        line = r"$\mathcal{A}_{i \to f}^{(n)}(t)$	$$\langle \varphi_i | \psi_W^{(n)} (t) \rangle$$<br>Übergangsamplitude			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image209(mn.Scene):
    def construct(self):
        line = r"$X_n^*$	$$\sup_{k \leq n} |X_k|$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image210(mn.Scene):
    def construct(self):
        line = r"Doob's first martingale inequality	$$\mathbb{P}(X^*_n \geq \alpha) \leq \frac{\mathbb{E}|X_n|}{\alpha}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image211(mn.Scene):
    def construct(self):
        line = r"Doob's $L^p$-martingale inequality	$$\lVert X^*_n \rVert_p \leq \frac{p}{p-1} \lVert X_n \rVert_p$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image212(mn.Scene):
    def construct(self):
        line = r"Hölder's inequality	$$\mathbb{E}|XY| \leq \lVert X \rVert_p \lVert Y \rVert_q$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image213(mn.Scene):
    def construct(self):
        line = r"Doob's upcrossing inequality	$X_n$ submartingale&nbsp;<br>$$\mathbb{E}(U_n) \leq \frac{1}{b-a} \mathbb{E}[(X_n - a)^+]$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image214(mn.Scene):
    def construct(self):
        line = r"Martingale convergence theorem	$X$ submartingale with $\sup_n \mathbb{E}(X^+_n) &lt; \infty$, then $\lim_n X_n =: X_\infty$ exists and is finite a.s. and $X_\infty \in L^1$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image215(mn.Scene):
    def construct(self):
        line = r"$(f * g)(x)$	$$\int_{\mathbb{R}^n} f(x-y)g(y)dy$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image216(mn.Scene):
    def construct(self):
        line = r"$\partial^\alpha(f * g) = (\partial^\alpha f) * g$ iff	$f \in C_0^\infty(\mathbb{R}^n)$ and $g \in L_\text{loc}^1(\mathbb{R}^n)$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image217(mn.Scene):
    def construct(self):
        line = r"Young's inequality	$$\lVert f * g \rVert_{L^p} \leq \Vert f \rVert_{L^1} \cdot \lVert g \rVert_{L^p}$$			(functional analysis)"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image218(mn.Scene):
    def construct(self):
        line = r"approximate identity	is a seq of smooth functions $\rho_j: \mathbb{R} \to [0, \infty)$ s.t. for every $\varphi \in C_0(\mathbb{R}^n)$:<br>$$\int_{\mathbb{R}^n} \varphi(x) \rho_j(x) dx \stackrel{j \to \infty}{\longrightarrow} \varphi(0)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image219(mn.Scene):
    def construct(self):
        line = r"shrinking support	$$\forall \epsilon &gt; 0 \exists N \in \mathbb{N} \forall n \geq N: \text{supp}(\rho_j) \subset B_{\epsilon} (0)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image220(mn.Scene):
    def construct(self):
        line = r"characterization of approximate identities using shrinking support	a sequence of smooth functions with shrinking support is an approximate identity iff<br>$$\int_{\mathbb{R}^n} \rho_j dm \to 1 \ \text{as} \ j \to \infty$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image221(mn.Scene):
    def construct(self):
        line = r"properties of $f_j$&nbsp;	\begin{enumerate}[label=\alph*)]<br>\item $f_j$ is smooth<br>\item $\lVert f_j \rVert_{L^p} \leq C \lVert f \rVert_{L^p}$<br>\item $f_j \stackrel{L^p(\mathbb{R}^n)}{\longrightarrow} f$<br>\end{enumerate}	Where f_j = f convoluted with rho_j		"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image222(mn.Scene):
    def construct(self):
        line = r"uniform integrability of $\mathcal{X}$	$$\lim_{c \to \infty} \sup_{X \in \mathcal{X}} \mathbb{E}(\mathbb{1}_{\{|X|\geq c\}} |X|) = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image223(mn.Scene):
    def construct(self):
        line = r"$\epsilon$-$\delta$-characterizations of uniform integrability	$\mathcal{X}$ is $L^1$ bounded (i.e. $\sup_{X \in \mathcal{X}} \mathbb{E}|X| &lt; \infty$) and <br>$$\forall \epsilon &gt; 0\exists \delta &gt; 0 \forall A \in \mathcal{F}: \mathbb{P}(A) &lt; \delta \implies \sup_{X\in \mathcal{X}} \mathbb{E}(|X|\mathbb{1}_A) &lt; \epsilon$$<br>iff $\mathcal{X}$ u.i.			(Stochastik II)"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image224(mn.Scene):
    def construct(self):
        line = r"criterion of de la Vallee Poussin	$\exists$ convex $G: \mathbb{R}_+ \to \mathbb{R}_+$ s.t.<br>$$\sup_{X \in \mathcal{X}} \mathbb{E}(G(|X|)) &lt; \infty \ \text{and} \ \lim_{x \to \infty} \frac{G(x)}{x} = + \infty$$<br>iff $\mathcal{X}$ u.i.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image225(mn.Scene):
    def construct(self):
        line = r"Vitali's convergence theorem	$(X_n)_{n \in \mathbb{N}_0} \subset L^1, X_\infty \in L^1$, TFAE:<br>\begin{enumerate}[label=(\roman*)]<br>\item $X_n \stackrel{L^1}{\longrightarrow} X_\infty$<br>\item $X_n \stackrel{p}{\longrightarrow} X_\infty$ and $(X_n)$ is u.i.<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image226(mn.Scene):
    def construct(self):
        line = r"$L^1$-convergence theorem for martingales	$X$ a u.i. submartingale, then $X_\infty := \lim_n X_n$ exists a.s., $X_\infty \in L^1$, $X_n \stackrel{L^1}{\longrightarrow} X_\infty$ and $\mathbb{E}(X_\infty|\mathcal{F}_n) \geq X_n \ \forall n$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image227(mn.Scene):
    def construct(self):
        line = r"Baker-Campbell-Haudorff Gleichung	$$e^{\hat{A}} \cdot e^{\hat{B}} = e^{\hat{A} + \hat{B} + \frac{1}{2} [\hat{A}, \hat{B}] + \mathcal{O}^3 + \dots}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image228(mn.Scene):
    def construct(self):
        line = r"Trotter Gleichung	$$e^{\hat{A} + \hat{B}} = \lim_n (e^\frac{\hat{A}}{n} e^\frac{\hat{B}}{n})^n$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image229(mn.Scene):
    def construct(self):
        line = r"$k$-Zykel	$$\sigma(i_v) = \begin{cases} i_{v+1}, \ &amp; v&lt;k \\ i_1, \ &amp; v=k \end{cases}$$<br>$$\sigma(i) = i \ \forall i \not\in \{i_1, \dots, i_k\}$$<br>$$\sigma = (i_1 \ i_2 \ \dots \ i_k)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image230(mn.Scene):
    def construct(self):
        line = r"Träger&nbsp;	$$\text{Supp}(\sigma) := \{i_1, \dots, i_k\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image231(mn.Scene):
    def construct(self):
        line = r"einfache Rechenregeln für Zyklen	\begin{enumerate}[label=\alph*)]<br>\item $(i_1 \ i_2 \ \dots \ i_k) = (i_1 \ i_2) \circ (i_2 \ i_3) \circ \dots \circ (i_{k-1} \ i_k)$<br>\item $(i_1 \ i_2 \ \dots \ i_k)^{-1} = (i_k \ i_{k-1} \ \dots \ i_2 \ i_1)$<br>\item $\tau \circ (i_1 \ i_2 \ \dots \ i_k) \circ \tau^{-1} = (\tau(i_1) \ \tau(i_2) \ \dots \ \tau(i_k))$<br>\item $\sigma, \tau \in \frak{S}_n$ disjunkt, dann $\sigma \circ \tau = \tau \circ \sigma$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image232(mn.Scene):
    def construct(self):
        line = r"Konjugation eines Zykelprodukts	$$j_{\nu \mu} = \tau(i_{\nu \mu})$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image233(mn.Scene):
    def construct(self):
        line = r"Satz über die Zykelzerlegung einer Permutation	Jede Permutation lässt sich bis auf Reihenfolge eindeutig in disjunkte nichttriviale Zykel zerlegen			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image234(mn.Scene):
    def construct(self):
        line = r"Zykeltyp (von $\sigma$)	Tupel der Längen der Zykel der Zerlegung. Konventionell aufsteigend mit eingefügten Einsen.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image235(mn.Scene):
    def construct(self):
        line = r"Konjugationsklasse	$$x^G = \{g x g^{-1} | g \in G \}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image236(mn.Scene):
    def construct(self):
        line = r"Zentralisator	$$Z_G (x) = \{g \in G | g x g^{-1} = x \}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image237(mn.Scene):
    def construct(self):
        line = r"Konjugationsklassen von $\frak{S}_n$ und Partitionen	entsprechen sich bijektiv			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image238(mn.Scene):
    def construct(self):
        line = r"Erzeuger von $\frak{A}_n$	3-Zyklen			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image239(mn.Scene):
    def construct(self):
        line = r"einfache Gruppe	$$N \trianglelefteq G \implies N = {1} \ \text{oder} \ N = G$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image240(mn.Scene):
    def construct(self):
        line = r"Die alternierende Gruppe ist für $n \geq 5$	einfach			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image241(mn.Scene):
    def construct(self):
        line = r"alle 3-Zyklen sind&nbsp;	zueinander konjugiert			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image242(mn.Scene):
    def construct(self):
        line = r"Kolmogorov's 0-1-law	$$\forall A \in \mathcal{T} := \bigcap_{n \in \mathbb{N}} \mathcal{T}_n: \mathbb{P}(A) \in \{0,1\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image243(mn.Scene):
    def construct(self):
        line = r"backwards martingale	\begin{enumerate}[label=(\roman*)]<br>\item $X_{-n}$ is $\mathcal{F}_{-n}$-mb<br>\item $X_{-n} \in L^1$<br>\item $\mathbb{E}(X_{-n} | \mathcal{F}_{-n-1}) = X_{-n-1}$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image244(mn.Scene):
    def construct(self):
        line = r"Backwards martingale convergence theorem	Any backwards martingale $(X_{-n})_{n\in \mathbb{N}_0}$ converges in $L^1$ to $X_{-\infty} \in L^1$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image245(mn.Scene):
    def construct(self):
        line = r"Kolmogorov's strong law of large numbers	$(X_n)_{n \in \mathbb{N}}$ iid and $\mathbb{E}|X_n| &lt; \infty$, then<br>$$\lim_{n \to \infty} \frac{S_n}{n} = \mathbb{E}(X_0)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image246(mn.Scene):
    def construct(self):
        line = r"Dichotomy for martingales with bounded increments	$\mathbb{E}(\sup_n |\Delta X_n|) &lt; \infty$, then<br>$$\mathbb{P}(\{\lim_n X_n \ \text{exists and is finite} \} \dot\cup \{\limsup_n X_n = +\infty, \liminf_n X_n = -\infty\}) = 1$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image247(mn.Scene):
    def construct(self):
        line = r"$\mathbb{Q} \ll \mathbb{P}$	$\mathbb{Q}, \mathbb{P}$ on $(\Omega, \mathcal{F})$. $\mathbb{Q}$ is absolutely continuous with respect to $\mathbb{P}$, iff&nbsp;<br>$$\mathbb{P}(A) = 0 \implies \mathbb{Q}(A) = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image248(mn.Scene):
    def construct(self):
        line = r"$\epsilon$-$\delta$-characterization of absolute continuity	$$\forall \epsilon &gt; 0 \exists \delta &gt; 0: \mathbb{P}(A) &lt; \delta \implies \mathbb{Q}(A) &lt; \epsilon$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image249(mn.Scene):
    def construct(self):
        line = r"Radon-Nikodym theorem	If $\mathbb{Q} \ll \mathbb{P}$, then a unique Radon-Nikodym density exists.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image250(mn.Scene):
    def construct(self):
        line = r"density of $\mathbb{Q}$ with respect to $\mathbb{P}$	$\mathbb{P}$-integrable non-negative $X =: \frac{d\mathbb{Q}}{d\mathbb{P}}$ s.t. $\mathbb{Q}(A) = \mathbb{E}^{\mathbb{P}}(X \mathbb{1}_A)$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image251(mn.Scene):
    def construct(self):
        line = r"Baye's formula	$$\mathbb{E}^{\mathbb{Q}}(Z|\mathcal{G}) = \frac{\mathbb{E}^{\mathbb{P}}(Z X | \mathcal{G})}{\mathbb{E}^{\mathbb{P}}(X | \mathcal{G})}$$<br>where $\mathbb{Q} \ll \mathbb{P}$ and $X$ is the Radon-Nikodym density			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image252(mn.Scene):
    def construct(self):
        line = r"$p$-Gruppe	$$|G| = p^n \ \text{for} \ n \in \mathbb{N}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image253(mn.Scene):
    def construct(self):
        line = r"$p$-Untergruppe	Untergruppe, die eine $p$-Gruppe ist			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image254(mn.Scene):
    def construct(self):
        line = r"$p$-Sylowgruppe (von $G$)	maximale $p$-Untergruppe			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image255(mn.Scene):
    def construct(self):
        line = r"erster Satz von Sylow	$$p^k | |G| \implies \exists H \leq G: |H| = p^k$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image256(mn.Scene):
    def construct(self):
        line = r"zweiter Satz von Sylow	\begin{enumerate}[label=\alph*)]<br>\item jede $p$-Untergruppe ist in einer $p$-Sylowgruppe enthalten<br>\item je zwei $p$-Sylowgruppen sind zueinander konjugiert<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image257(mn.Scene):
    def construct(self):
        line = r"Sylowgruppen als Normalteiler	Es sind äquivalent:<br>\begin{enumerate}[label=\alph*)]<br>\item $N$ ist Normalteiler<br>\item $N$ ist die einzige $p$-Sylowgruppe<br>\item $N = \{g\in G|\exists k \in \mathbb{N}_0: \text{ord}(g) = p^k\}$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image258(mn.Scene):
    def construct(self):
        line = r"dritter Satz von Sylow	\begin{enumerate}[label=\alph*)]<br>\item $n_p (G) \equiv 1 \mod p$<br>\item $n_p (G) | |G|$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image259(mn.Scene):
    def construct(self):
        line = r"Präsentation einer Gruppe mit Ordnung $pq$	$$\langle x, y | x^p = y^q = 1, yxy^{-1} = x^k \rangle \ \text{für ein} \ k \ \text{mit} \ k | (k^q -1)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image260(mn.Scene):
    def construct(self):
        line = r"Ring	$(R, +, \cdot)$, sodass&nbsp;<br>\begin{enumerate}[label=\alph*)]<br>\item $(R, +)$ ist eine abelsche Gruppe<br>\item $(R, \cdot)$ ist ein Monoid<br>\item Distributivgesetz gilt<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image261(mn.Scene):
    def construct(self):
        line = r"Einheitengruppe	$$R^\times = \{r \in R| \exists s \in R: rs = sr = 1\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image262(mn.Scene):
    def construct(self):
        line = r"Schiefkörper	Ring mit $R^\times = R \setminus \{0\}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image263(mn.Scene):
    def construct(self):
        line = r"Körper	kommutativer Schiefkörper			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image264(mn.Scene):
    def construct(self):
        line = r"Nullteiler	$a$ heißt Nullteiler, falls $\exists b \in R \setminus \{0\}: a b=0 \vee b a = 0$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image265(mn.Scene):
    def construct(self):
        line = r"Integritätsring	kommutativer Ring ohne Nullteiler&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image266(mn.Scene):
    def construct(self):
        line = r"Teilring	Teilmenge eines Rings, die selbst ein Ring ist			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image267(mn.Scene):
    def construct(self):
        line = r"$R[x]$	$$\{(a_k)_{k \in \mathbb{N}_0} \in R^{\mathbb{N}_0} | \exists n \in \mathbb{N}_0 \forall k &gt; n: a_k = 0\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image268(mn.Scene):
    def construct(self):
        line = r"Ringhomomorphismus	\begin{enumerate}[label=\alph*)]<br>\item $\phi(a + b) = \phi(a) + \phi(b)$<br>\item $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ und $\phi(1) = 1$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image269(mn.Scene):
    def construct(self):
        line = r"universelle Eigenschaft von Polynomringen	$\phi: R \to S$ Homomorphismus von kommutativen Ringen und $s_1, \dots, s_n$ eine Auswahl aus $S$, dann existiert genau ein Ringhomomorphismus $\Phi: R[x_1, \dots, x_n] \to S$ mit&nbsp;<br>\begin{enumerate}[label=\alph*)]<br>\item $\Phi|_R = \phi$<br>\item $\Phi(x_i) = s_i$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image270(mn.Scene):
    def construct(self):
        line = r"Linksideal	additive Untergruppe sodass $r \cdot a \in I \ \forall r\in R\forall a\in I$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image271(mn.Scene):
    def construct(self):
        line = r"Rechtsideal	additive Unterguppe, sodass $a \cdot r \in I \forall r \in R \forall a \in I$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image272(mn.Scene):
    def construct(self):
        line = r"Ideal	Rechtsideal und Linksideal			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image273(mn.Scene):
    def construct(self):
        line = r"Nullideal	$$I = \{0\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image274(mn.Scene):
    def construct(self):
        line = r"Einsideal	$$I = R$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image275(mn.Scene):
    def construct(self):
        line = r"Charakterisierung von Idealen	\begin{enumerate}[label=\alph*)]<br>\item Kern eines Ringhomomorphismus<br>\item $p: R \to R/I, a \mapsto a + I$ ist ein Ringhomomorphismus<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image276(mn.Scene):
    def construct(self):
        line = r"Charakterisierung von Körpern als kommutative Ringe	$R$ besitzt kein nichttriviales echtes Ideal			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image277(mn.Scene):
    def construct(self):
        line = r"Homomorphiesatz (für Ideale)	Jeder Ringhomomorphismus $\phi: R \to S$ induziert einen Isomorphismus<br>$$\bar{\phi}:&nbsp;R/I&nbsp;\stackrel{\sim}{\longrightarrow}&nbsp;\text{im}(\phi) \ \text{mit} \&nbsp;&nbsp;I := \text{ker}(\phi)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image278(mn.Scene):
    def construct(self):
        line = r"absolutely continuous (functions)	$$\forall \epsilon &gt; 0\forall \delta &gt; 0\forall a_1 \leq b_1 \leq \dots \leq a_n \leq b_n: \sum_{i=1}^n (b_n - a_n) &lt; \delta \implies \sum_{i=1}^n (F(b_n) - F(a_n)) &lt; \epsilon$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image279(mn.Scene):
    def construct(self):
        line = r"fundamental theorem of calculus for the Lebesgue integral	For any $f$ on a compact $[a, b]$, TFAE:<br>\begin{enumerate}[label=(\arabic*)]<br>\item $f$ is absolutely continuous<br>\item $f$ is differentiable a.e., $f' \in L^1([a, b])$ and $f(x) = f(a) + \int_a^x f'(t) dt$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image280(mn.Scene):
    def construct(self):
        line = r"Lebesgue point	$$\lim_{r \to 0^+} \frac{1}{m(B_r (x))} \int_{B_r (x)} |f(y) - f(x)| dy = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image281(mn.Scene):
    def construct(self):
        line = r"Lebesgue differentiation theorem	For any $f \in L^1_{\text{loc}}(\mathbb{R}^n)$, almost every point in $\mathbb{R}^n$ is a Lebesgue point of $f$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image282(mn.Scene):
    def construct(self):
        line = r"Chebyshev's inequality	$$\mu(\{x \in X | g(x) &gt; t\}) \leq \frac{\lVert g \rVert_{L^1}}{t}$$			(functional analysis)"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image283(mn.Scene):
    def construct(self):
        line = r"maximal function	$$M f(x) := \sup_{r&gt;0} \frac{1}{m(B_r (x))} \int_{B_r (x)} |f| dm$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image284(mn.Scene):
    def construct(self):
        line = r"weakly integrable	$$\exists C &gt; 0: \mu(\{x\in X||f(x)|&gt;t\}) \leq \frac{C}{t}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image285(mn.Scene):
    def construct(self):
        line = r"Hardy-Littlewood theorem	There exists a constant $C&gt;0$ dependent only on the dimension $n$ s.t. $\lVert M f \rVert_{L^1_{\text{weak}}} \leq C \lVert f \rVert_{L^1}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image286(mn.Scene):
    def construct(self):
        line = r"Vitali's covering lemma	$$\bigcup_{i=1}^N B_{r_i} (x_i) \subset \bigcup_{j \in I} B_{3r_j} (x_j)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image287(mn.Scene):
    def construct(self):
        line = r"Radon-Nidkodym density	$f =: \frac{d\lambda}{d\mu}$ s.t.<br>$$\lambda(A) = \int_A f d\mu$$			(functional analysis)"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image288(mn.Scene):
    def construct(self):
        line = r"absolutely continuous (measures)	$$\mu(A) = 0 \implies \lambda(A) = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image289(mn.Scene):
    def construct(self):
        line = r"total variation	$$TV(f) := \sup \{ \sum_{i=1}^N |f(x_i) - f(x_{i-1})| | N &gt; 0, a &lt; x_1 &lt; \dots &lt; x_N = b\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image290(mn.Scene):
    def construct(self):
        line = r"uniformly integrable&nbsp;	$$\forall \epsilon &gt; 0 \exists \delta &gt; 0 \forall f \in \mathcal{F} \forall mb. A \subset X: \mu(A) &lt; \delta \implies \int_A |f| d\mu &lt; \epsilon$$			functional analysis"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image291(mn.Scene):
    def construct(self):
        line = r"Vitali's convergence theorem	For a Lebesgue-measurable subset $X \subset \mathbb{R}$ with finite measure,&nbsp; if $(f_n)_{n \in \mathbb{N}}$ is a uniformly integrable collection of functions on $X$ such that $f_n \to f$ pointwise almost everywhere, then $f \in L^1 (X)$, and $\int_X f_n dm \to \int_X f dm$.			functional analysis"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image292(mn.Scene):
    def construct(self):
        line = r"fourier series of $f$	$$f(x) = \sum_{k \in \mathbb{Z}^n} e^{-2\pi i k \cdot x} \hat{f}_k (x)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image293(mn.Scene):
    def construct(self):
        line = r"$\mathbb{T}^n$	$$\mathbb{R}^n/\mathbb{Z}^n$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image294(mn.Scene):
    def construct(self):
        line = r"$\ell^p(\mathbb{Z}^n)$	$$L^p(\mathbb{Z}^n, \nu)$$<br>and $\nu$ is the counting measure on $\mathbb{Z}^n$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image295(mn.Scene):
    def construct(self):
        line = r"Markov chain	$$\mathbb{P}(X_n \in B | \mathcal{F}_m) = \mathbb{P}(X_n \in B | X_m)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image296(mn.Scene):
    def construct(self):
        line = r"homogeneous Markov chain	$$\bar{\mathbb{P}}_l = \bar{\mathbb{P}}_k$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image297(mn.Scene):
    def construct(self):
        line = r"initial distribution	$$\bar{\mu}(B) = \mathbb{P}(X_0 \in B)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image298(mn.Scene):
    def construct(self):
        line = r"probabilistic structure of a homogeneous Markov chain	$$\mathbb{E}(g(X_0, \dots, X_n)) = \int_E \dots \int_E g(x_0, \dots, x_n) \bar{P}(x_{n-1}; dx_n) \dots \bar{P}(x_0, dx_1) \bar{\mu}(dx_0)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image299(mn.Scene):
    def construct(self):
        line = r"$(p_{i j})$	$$:= \bar{P}(i, \{j\}) = \mathbb{P}(X_n = j | X_{n-1} = i)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image300(mn.Scene):
    def construct(self):
        line = r"starting condition lemma for Markov chains	A $(\mu, P)$-Markov chain conditioned on ${X_m = i}$ generates a $(\delta_i, P)$-Markov chain $(X_{n+m})_{n\in \mathbb{N}_0}$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image301(mn.Scene):
    def construct(self):
        line = r"simple transition probability formulas	\begin{enumerate}[label=(\roman*)]<br>\item $\mathbb{P}(X_n = j) = (\mu P^n)_j$<br>\item $\mathbb{P}(X_{m+n} = j | X_m = i) = p_{i j}^{(n)}$<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image302(mn.Scene):
    def construct(self):
        line = r"Chapman-Kolmogorov equation	$$\mathbb{P}(X_{m+n} = z | X_0 = x) = \sum_{y \in E} \mathbb{P}(X_m = y | X_0 = x) \mathbb{P}(X_n = z | X_0 = y)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image303(mn.Scene):
    def construct(self):
        line = r"$i \to j$	$$\mathbb{P}(X_n = j \ \text{for some} \ n \geq 0 | X_0 = i) &gt; 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image304(mn.Scene):
    def construct(self):
        line = r"$i \leftrightarrow j$	$i$ communicates with $j$, $i \to j$ and $j \to i$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image305(mn.Scene):
    def construct(self):
        line = r"closed communicating class	$$i \in C \wedge i \to j \implies j \in C$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image306(mn.Scene):
    def construct(self):
        line = r"absorbing state	$\{i\}$ is a closed communicating class			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image307(mn.Scene):
    def construct(self):
        line = r"irreducible Markov chain	the state space is a closed communicating class			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image308(mn.Scene):
    def construct(self):
        line = r"$\mathbb{P}_i (B)$&nbsp;	$$\mathbb{P}(B|X_0 = i)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image309(mn.Scene):
    def construct(self):
        line = r"$H^A$	$$\inf \{n\geq 0| X_n \in A\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image310(mn.Scene):
    def construct(self):
        line = r"$h_i^A$	$$\mathbb{P}_i (H^A &lt; \infty)$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image311(mn.Scene):
    def construct(self):
        line = r"$\mathscr{S}(\mathbb{Z}^n)$	The space of rapidly decreasing coefficients. $f \in \mathscr{S}(\mathbb{Z}^n)$, if&nbsp;<br>$$\forall \ \text{polynomial} \ P: \mathbb{R}^n \to \mathbb{R}: \mathbb{Z}^n \to V, k \mapsto P(k) f(k) \ \text{is bounded}$$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image312(mn.Scene):
    def construct(self):
        line = r"$\hat{f}_k$	$$\int_{\mathbb{T}^n} e^{-2\pi i k \cdot x} f(x) dx$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image313(mn.Scene):
    def construct(self):
        line = r"$\mathscr{F} f$	$$(\mathscr{F} f)_k = \hat{f}_k$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image314(mn.Scene):
    def construct(self):
        line = r"$\mathscr{F}^* g$	$$:= \check{g}(x) := \sum_{k \in \mathbb{Z}^n}&nbsp; e^{2\pi i k \cdot x} g_k$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image315(mn.Scene):
    def construct(self):
        line = r"Parseval's identity	For every $f, g \in C^{\infty}(\mathbb{T}^n)$,<br>$$\langle \hat{f}, \hat{g} \rangle_{\ell^2} = \langle f, g \rangle_{L^2}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image316(mn.Scene):
    def construct(self):
        line = r"$\mathscr{F}$ and $\mathscr{F}^*$	$\mathscr{F}: L^2(\mathbb{T}^n) \to \ell^2(\mathbb{Z}^n)$ and $\mathscr{F}^*: \ell^2(\mathbb{Z}^n) \to L^2(\mathbb{T}^n)$ are unitary maps and inverse to each other			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image317(mn.Scene):
    def construct(self):
        line = r"$\widehat{\partial^{\alpha} f}_k$	$$(2\pi i k)^{\alpha} \hat{f}_k$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image318(mn.Scene):
    def construct(self):
        line = r"Fourier transform	$$(\mathscr{F} f)(p) := \hat{f}(p) := \int_{\mathbb{R}^n} e^{-2\pi i p \cdot x} f(x) dx$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image319(mn.Scene):
    def construct(self):
        line = r"Fourier inverse transform	$$(\mathscr{F}^* g)(x) := \check{g}(x) := \int_{\mathbb{R}^n} e^{2\pi i p \cdot x} g(p) dp$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image320(mn.Scene):
    def construct(self):
        line = r"Schwartz space	space of smooth and rapidly decreasing functions. $f \in \mathscr{S}(\mathbb{R}^n)$, if<br>$$\forall \alpha, \beta: x^{\alpha} \partial^{\beta} f \ \text{is bounded}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image321(mn.Scene):
    def construct(self):
        line = r"Plancherel's theorem	For every $f, g \in \mathscr{S}(\mathbb{R}^n)$, $\langle f, g \rangle_{L^2} = \langle \hat{f}, \hat{g} \rangle_{L^2}$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image322(mn.Scene):
    def construct(self):
        line = r"Klein-Gordong-Gleichung	$$(\square + (\frac{m c}{\hbar})^2) \Psi(\vec{r}, t) = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image323(mn.Scene):
    def construct(self):
        line = r"Dirac'scher Hamiltonoperator	$$\hat{\mathbb{H}}_D = c \vec{\mathbb{\alpha}} \cdot \vec{p} + \mathbb{\beta} m c^2$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image324(mn.Scene):
    def construct(self):
        line = r"zeitabhängige Dirac-Gleichung (für das freie Teilchen)	$$i \hbar \frac{\partial}{\partial t} \Psi = \hat{\mathbb{H}}_D \Psi$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image325(mn.Scene):
    def construct(self):
        line = r"recurrent	$$\mathbb{P}_i (X_n = i \ \text{for infinitely many} \ n) = 1$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image326(mn.Scene):
    def construct(self):
        line = r"transcient	$$\mathbb{P}_i (X_n = i \ \text{for infinitely many} \ n) = 0$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image327(mn.Scene):
    def construct(self):
        line = r"$T_i^{(k)}$	$$\inf \{n &gt; T_i^{(k-1)} | X_n = i\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image328(mn.Scene):
    def construct(self):
        line = r"Strong Markov property	Conditional on $\tau &lt; \infty$ and $X_{\tau} = i$, the process $(X_{\tau + n})_{n \in \mathbb{N}}$ is a $(\delta_i, P)$-Markov chain.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image329(mn.Scene):
    def construct(self):
        line = r"$\lVert f \rVert_{W^{m, p}}$	$$\sum_{|\alpha|\leq m} \lVert \partial^{\alpha} f \rVert_{L^p}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image330(mn.Scene):
    def construct(self):
        line = r"$\lVert f \rVert_{H^m}$	$$\lVert (1 + |p|^2)^{m/2} \hat{f} \rVert_{L^2}$$<br>and for fully periodic functions:<br>$$\lVert (1 + |k|^2)^{m/2} \hat{f} \rVert_{\ell^2}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image331(mn.Scene):
    def construct(self):
        line = r"$H^m (\mathbb{R}^n), H^m(\mathbb{T}^n)$	$$\{f \in L^2(\mathbb{R}^n) | \lVert f \rVert_{H^m} &lt; \infty\}$$<br>$$\{f \in L^2(\mathbb{T}^n) | \lVert f \rVert_{H^m} &lt; \infty\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image332(mn.Scene):
    def construct(self):
        line = r"$\langle f, g \rangle_{H^m}$	$$\int_{\mathbb{R}^n} (1+|p|^2)^m \langle \hat{f}(p), \hat{g}(p) \rangle dp$$<br>and for fully periodic functions:<br>$$\sum_{k \in \mathbb{Z}^n} (1+|k|^2)^m \langle \hat{f}(k), \hat{g}(k) \rangle$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image333(mn.Scene):
    def construct(self):
        line = r"continous inclusion $H^s(\mathbb{R}^n) \hookrightarrow C^m(\mathbb{R}^n)$	$H^s(\mathbb{R}^n) \to C^m(\mathbb{R}^n), f \mapsto \tilde{f}$ is a continuous bounded operator. This exists if&nbsp;<br>$$\lVert f \rVert_{C^m} \leq c \lVert f \rVert_{H^s}$$<br>for some constant $c$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image334(mn.Scene):
    def construct(self):
        line = r"Sobolov embedding theorem, case $p = 2$	Assume $n \in \mathbb{N}$ and $s &gt; 0$ satisfy $2s &gt; n$. Then there exists a continuous inclusion<br>$$H^{s+m}(\mathbb{R}^n) \hookrightarrow C^m(\mathbb{R}^n) \quad \text{and} \quad H^{s+m}(\mathbb{T}^n) \hookrightarrow C^m(\mathbb{T})$$<br>for every integer $m \geq 0$.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image335(mn.Scene):
    def construct(self):
        line = r"compact operator	it maps every compact set in $X$ onto a precompact set in $Y$<br><br>or equivalently<br><br>for every bounded sequence in $X$, $Ax_{n_k}$ has a convergent subsequence in $Y$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image336(mn.Scene):
    def construct(self):
        line = r"Rellich-Kondrachov for $p=2$	For every $t&gt;s\geq 0$, the natural inclusion $H^t (\mathbb{R}^n) \hookrightarrow H^s (\mathbb{R}^n)$ is compact.			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image337(mn.Scene):
    def construct(self):
        line = r"Primideal	$$a b \in I \implies a \in I \vee b \in I$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image338(mn.Scene):
    def construct(self):
        line = r"maximales Ideal	$$\nexists J: I \subsetneq J \subsetneq R$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image339(mn.Scene):
    def construct(self):
        line = r"Charakterisierung der Struktur von $R/I$ durch Ideale	\begin{enumerate}[label=\alph*)]<br>\item $R/I$ Integritätsring $\iff$ $I$ Primideal<br>\item $R/I$ Körper $\iff$ $I$ maximales Ideal<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image340(mn.Scene):
    def construct(self):
        line = r"multiplikative Teilmenge	$$1 \in S \wedge ab \in S \forall a, b \in S$$<br>$S \subset R$&nbsp;			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image341(mn.Scene):
    def construct(self):
        line = r"Lokalisierung von $R$ nach $S$	$$S^{-1} R := (R \times S)/\sim$$<br>wobei $\sim$ definiert ist durch<br>$$(r_1, s_1) \sim (r_2, s_2) :\iff \exists s \in S: s \cdot (r_1 s_2 - r_2 s_1) = 0$$<br>Elemente sind definiert durch&nbsp;<br>$$\frac{r}{s} := [(r, s) \ \text{modulo} \ \sim]$$<br>Addition und Multiplikation machen $S^{-1} R$ zu einem Ring			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image342(mn.Scene):
    def construct(self):
        line = r"Quotientenkörper	$R$ Integritätsring, dann ist $R\setminus \{0\}$ ein Untermonoid.<br>$$\text{Quot}(R) := S^{-1} R \quad \text{für} \quad S = R\setminus \{0\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image343(mn.Scene):
    def construct(self):
        line = r"Aussagen über die Lokalisierung von $R$ in $S$	\begin{enumerate}[label=\alph*)]<br>\item Die Lokalisierungsabbildung $f: R \to S^{-1} R, a \mapsto \frac{a}{1}$ ist ein Homomorphismus von Ringen mit $f(S) \subset (S^{-1} R)^{\times}$<br>\item Jeder Homomorphismus $g: R \to T$ in einen Ring $T$ mit $g(R) \subset T^{\times}$ faktorisiert eindeutig über die Lokalisierungsabbildung<br>\end{enumerate}			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image344(mn.Scene):
    def construct(self):
        line = r"$b$ ist Teiler von $a$	$$\exists c \in R: a = b c$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image345(mn.Scene):
    def construct(self):
        line = r"$b$ ist assoziiert zu $a$&nbsp;	$$\exists c \in R^{\times}: a = bc$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image346(mn.Scene):
    def construct(self):
        line = r"convergent sequences of compact operators	converge to a compact operator			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image347(mn.Scene):
    def construct(self):
        line = r"$p \in R$ prim	$$p = a b \implies p | a \vee p | b$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image348(mn.Scene):
    def construct(self):
        line = r"$p \in R$ irreduzibel&nbsp;	$$p = a b \implies a \in R^{\times} \vee b \in R^{\times}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image349(mn.Scene):
    def construct(self):
        line = r"faktorieller Ring	$$\forall a \in R \setminus (R^{\times} \cup \{0\}) \exists p_1, \dots, p_n \ \text{prim}: a = p_1 \dots p_n$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image350(mn.Scene):
    def construct(self):
        line = r"$\text{ggT}(a_1, \dots, a_n)$	$$:= \prod_{p \in \mathscr{P}} p^{m_p} \quad \text{mit} \quad m_p := \min \{m_p (a_i) | 1 \leq i \leq n\}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image351(mn.Scene):
    def construct(self):
        line = r"$\text{kgV}(a_1, ..., a_n)$	$$:= \prod_{p \in \mathscr{P}} p^{n_p} \quad \text{mit} \quad n_p := \max \{m_p (a_i) | 1 \leq i \leq n \}$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image352(mn.Scene):
    def construct(self):
        line = r"primitives Polynom	$$\text{ggT}(a_0, \dots, a_n) = 1$$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
class Image353(mn.Scene):
    def construct(self):
        line = r"Inhalt des Polynoms	$c(f) \in K^{\times} \setminus R^{\times}$, sodass $f(x) = c(f) \cdot f^*(x)$			"
        group = aw.generate_vgroup(line)
        self.add(group)
            
