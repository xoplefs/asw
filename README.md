# A Softer World Text Analysis

This is the start of a project that I first thought of just under 5 years ago,
on May 27, 2005, just a few days before the final A Softer World comic.

The spirit of the idea is to look for any sort of pattern in how sentences are
broken up between panels in A Softer World comics, relative to the structure
of the sentences. Because I had often found the breaks to be counter-intuitive,
I might expect a high occurence of the breaks being within major syntactic
constituents/phrases, rather than at their boundaries.

Next steps would be:

Use OCR to extract the text from all of the comics, using the comic panels as 
a basis to annotate the breaks.

Use NLPT and perhaps statistical packages to look for patterns, if any, within
those break.

I also want to be able to extract the alt-text (which is
'title') and match it with each comic's text and
filename. In the interest of making this more aligned with the CS50, I suppose
I could throw it all in an SQL database with a search feature. Maybe categorize
them there by whatever type of syntactic breaks.