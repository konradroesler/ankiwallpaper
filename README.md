# Anki Wallpapers

This CLI application is a collection of scripts written in order to convert a large number of svg files containing rendered LaTeX into png's.

### Motivation

I use anki's LaTeX plugin to study for my math courses in university. I then had the idea to create background images for my personal pc from these Anki cards and display them at random, so every time I'd look at my background I'd see a different card.

### Problem statement

The general anatomy of a flashcard is simple. Each card has a 'front' and a 'back', which contain some LaTeX code. When studying, the front is displayed. When clicking again, the back is displayed below. That's what I call the full view of a flash card.

Now the objective can be stated concisely:

>>> For every flashcard, create a png which shows the full view of that flash card.

### Challenges and solutions

This turned out to be tricky... The way anki stores flashcards which contain LaTeX is by storing every snippet of rendered LaTeX (delimited by `[latex] ... [\latex]` tags) as a seperate svg file in a collective media directory. Since each card has a unique identifier, you could imagine each svg would be stored in a way you could easily tell which card it belongs to, e.g. the name of the svg file contains the uid, but this is not the case. Instead Anki the files name is a hash generated in a way I can't trace back the inputs.

So, out of a large collection of svg's we now need to match two svg's to the same card and label them 'front' and 'back' respectively, given only...

1. a `.txt` file of all cards, including uid, front text, back text. Each line in the file represents one card and the fields are seperated via tabs.
2. Anki's media folder containing all svg's

I matched an svg to a card by parsing the svg's raw text representation and extracing the value of the `href` attribute of each `use` tag. These values are typically in the range 0-122 and are identical to the corresponding symbols ASCII value. I then built a translation dictionary which I feed the extracted `href`'s into and get a list of plain text symbols that svg contains. Then I go through the `.txt` and check which line contains these symbols while preserving order.

### Issues

There are a lot of details to this method which are documented in the docstrings. Since the above method works like a filter, there is no guarantee that a) a suitable card is found and b) the matched card is unique. To reduce the error rate, you'd need to add more and more well thought out rules to eliminate all edge cases. This seems like a lot of work.

### Other solutions and future work

When I originally did this project I did not have access to a strong LLM. When I get time to come back to this I will try to search through Anki's code base and find out how the svg's naming hash is generated. This would arguably be the cleanest solution.

### Reproducibility

1. This solution is tailored specifically to how I create Anki cards.
2. This method is not perfect. See the [issues](#issues).

# Developers notes

### Notes

Note that a use tag in any svg represents exactly one symbol.

Note that not all symbols are recorded inside the alphabet dict.

Note the following conflict: since the ids are in range 0-122, multiple symbols might be assigned the same id by this parser. However, this seems to behave quite nicely, since ```\mathbb{E}``` is assigned the same id as E.

Note also that the mapping: id -> symbol is not injective.

Note that the plaintext notes still contain ```\begin{enumerate}``` and ```\item```, while the svgs contain ```(i), (ii)``` etc., for this reason all note get preprocessed.
Note also that the preprocessing stage assumes that there are no nested environments.

### Implementation notes

Some notes addressing implementation details unique to my way of creating anki cards, which would need to be addressed in order to port this to other systems/anki users.

Note that I have edited the latex card template so that two dots are added to the end of every card. This was done so display math is centered properly.

Note that the following card structure is assumed: 3 content fields, front, back and course. The caveat here is that the course field is added to the front of the card, meaning that when searching the right note, the front and course fields actually have to be added together. I should refactor my own cards, delete the course field and instead define a macro in the preamble which is then used in the actual front field of the note to fix this.

### Implementation concepts

A finicky thing is that in the alphabet, one symbol (key) can have multiple ids (its value is a list of ids) and also one id can be element of multiple dict entries. So when the symbols are generated, its all lists, meaning we are searching for one of the symbols in the list. The current implementation is not clean.
