#!/usr/bin/env python
"""
Emoji Example
===============
"""
import io
import string
from os import path

import matplotlib.pyplot as plt
from wordcloud import WordCloud

d = path.dirname(__file__)

text = io.open(path.join(d, 'data/emoji-final.txt')).read()

normal_word = r"(?:\w[\w']+)"
ascii_art = r"(?:[{punctuation}][{punctuation}]+)".format(
  punctuation=string.punctuation)

emoji = r"(?:[^\s])(?<![\w{ascii_printable}])".format(
  ascii_printable=string.printable)
regexp = r"{normal_word}|{ascii_art}|{emoji}".format(normal_word=normal_word,
                                                     ascii_art=ascii_art,
                                                     emoji=emoji)

font_path = path.join(d, 'emojione-svg.otf')
wordcloud = WordCloud(font_path=font_path, regexp=regexp,
                      background_color="white").generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
