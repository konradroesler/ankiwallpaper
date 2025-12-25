from main import *

if __name__ == "__main__":
    svg_path = "./svgs/latex-13215cc961e4066c236a0f80fe04154251cd50ff.svg"
    text = r"l1u(ZQE3FW	Lernen::Theo IV::6. Näherungsmethoden für stationäre Probleme::6.2 Zeitunabhängige Störungstheorie	$|n^{(1)}\rangle$	$$|n^{(0)}\rangle + \lambda |\tilde{n}^{(1)}\rangle$$	Korrigierter Zustandsvektor mit Korrektur erster Ordnung<br><br>nicht entartete ungestörte Zustände			"
    note = get_note(text)
    note = preprocess_note(note)
    print(note)
    with open(svg_path, "r") as file:
        ids = parse_svg_file(file)
        symbol_filter = generate_symbol_filter(ids)
        print(matches(symbol_filter, note.front))
