# Word Unscrambler for Python #

This algorithm uses letter frequencies instead of permutation based approach. Thus, it can unscramble large number of letters with constant performance.
List of words is getting scanned once regardles of word length.

https://theunscrambled.com site also used that technique in order to effectively provide unscrambled word solutions.

## Usage ##

```python

from unscrambler import WordUnscrambler

wu = WordUnscrambler()
print wu.unscramble("enscuamblr")

```
