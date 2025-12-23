# Anki Wallpapers

### Notes

Note that a use tag in any svg represents exactly one symbol.

Note that not all symbols are recorded inside the alphabet dict.

Note the following conflict: since the ids are in range 0-122, multiple symbols might be assigned the same id by this parser. However, this seems to behave quite nicely, since ```\mathbb{E}``` is assigned the same id as E.

Note also that the mapping: id -> symbol is not injective.

Note that the plaintext notes still contain ```\begin{enumerate}``` and ```\item```, while the svgs contain ```(i), (ii)``` etc., for this reason all note get preprocessed.

### Implementation notes

Some notes addressing implementation details unique to my way of creating anki cards, which would need to be addressed in order to port this to other systems/anki users.

Note that I have edited the latex card template so that two dots are added to the end of every card. This was done so display math is centered properly.

Note that the following card structure is assumed: 3 content fields, front, back and course. The caveat here is that the course field is added to the front of the card, meaning that when searching the right note, the front and course fields actually have to be added together. I should refactor my own cards, delete the course field and instead define a macro in the preamble which is then used in the actual front field of the note to fix this.
