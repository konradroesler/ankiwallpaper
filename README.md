# Anki Wallpapers

This CLI application is a collection of scripts written in order to convert a large number of svg files containing rendered LaTeX into png's.

![desktop](/screenshots/desktop.png)

### Motivation

I use anki's LaTeX plugin to study for my math courses in university. I then had the idea to create background images for my personal pc from these Anki cards and display them at random, so every time I'd look at my background I'd see a different card.

### Problem statement

The general anatomy of a flashcard is simple. Each card has a 'front' and a 'back', which contain some LaTeX code. When studying, the front is displayed. When clicking again, the back is displayed below. That's what I call the full view of a flash card.

Now the objective can be stated concisely:

**For every flashcard, create a png which shows the full view of that flash card.**

Anki stores the front and back as separate svg's by computing a hash value from the fields contents. We can replicate the way the hash is computed by looking at `rslib/src/latex.rs` in the Anki GitHub repostory. After we found the matching svg's, we copy them here, change their font to be white and use puppeteer to open a browser, stack two matching svg's and save a screenshot in `images/` programatically for every pair.