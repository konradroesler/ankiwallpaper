from main import *

if __name__ == "__main__":
    svg_path = "./svgs/latex-91c84c9f824066de398267b925ba83ec1d780280.svg"
    text = r'"u$]#zd:}I3"	Lernen::Algebra und Funktionentheorie::2. Ringe und Polynome::2.5 Faktorielle Ringe und das Lemma von Gauss	$p \in R$ prim	$$p = a b \implies p | a \vee p | b$$				'
    note = get_note(text)
    note = preprocess_note(note)
    with open(svg_path, "r") as file:
        ids = parse_svg_file(file)
        symbol_filter = generate_symbol_filter(ids)
        print(matches(symbol_filter, text))
