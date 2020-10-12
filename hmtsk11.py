from collections import Counter

a = [1, 2, 5, 4, 2, 3, 5, 1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
cnt = Counter(a)
print(cnt.most_common(5))