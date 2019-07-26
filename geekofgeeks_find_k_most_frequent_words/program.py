
def create_word_count(text):
    d = {}
    for w in text.split():
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d

def print_k_words(k, d):
    i = 0
    for w in sorted(d, key=d.get, reverse=True):
        i += 1
        if i > k:
            break
        print w, d[w]


text = "This is a string There are duplicate words in the string more string some more string"
d = create_word_count(text)
print_k_words(2, d)