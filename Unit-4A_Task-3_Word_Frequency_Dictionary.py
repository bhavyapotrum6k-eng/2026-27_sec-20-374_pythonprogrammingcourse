sentence = 'python is easy and python is fun'
words = sentence.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print('Word Frequency:', count)