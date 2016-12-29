from collections import Counter
with open("text.rtf", 'r') as f:
    text = f.read()

c = Counter(text)
print (c.most_common()[:-10-1:-1])
