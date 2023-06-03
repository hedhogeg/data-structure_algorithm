N = int(input())

vocab = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    w_len = len(word)
    vocab[w_len].append(word)

for words in vocab:
    words = list(set(words))
    words.sort()
    for w in words:
        print(w)