import random
from collections import Counter, defaultdict

words = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.  Donec hendrerit tempor tellus.  Donec pretium posuere tellus.  Proin quam nisl, tincidunt et, mattis eget, convallis nec, purus.  Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.  Nulla posuere.  Donec vitae dolor.  Nullam tristique diam non turpis.  Cras placerat accumsan nulla.  Nullam rutrum.  Nam vestibulum accumsan nisl."

words = words.split()
n = len(words)

documents = [words[:random.randrange(n)] for _ in range(10)]
all_words = defaultdict(set)

for index, document in enumerate(documents):
    for word in document:
        all_words[word].add(index)

choice_words = ['Lorem', 'Nulla', 'ipsum']

choice_docs = set(range(10))

for word in choice_words:
    choice_docs &= all_words[word]
