text = """
machine learning is powerful
machine learning helps analyze data
data science uses machine learning
"""

words = text.lower().split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Frequency:", freq)

most = max(freq, key=freq.get)
print("Most frequent:", most)

print("Unique words:", set(words))

print("Words appearing more than once:")
for word in freq:
    if freq[word] > 1:
        print(word)
