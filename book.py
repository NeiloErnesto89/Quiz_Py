import re # for regular expressions
import collections #allows us to count occurences of words

text = open('book.txt').read().lower()
words = re.findall('\w+', text) # w denotes anything that's not a whitespace and + denotes one or more so it's considered a word
print(collections.Counter(words).most_common(8))