import src.textokens as textokens

line = r"Raileigh-Ritzsches Variationsprinzip	$$\mathcal{E}_0 \leq \frac{\langle \Psi | \hat{H} | \Psi \rangle}{\langle \Psi | \Psi \rangle}$$			"
tokens = textokens.generate_tokens(line)
print(tokens)
