score=[80,90,75]
total = 0
for score in scores:
  total = total + score

average =total /len(scores)

print("Scores:",score)
print("total:",total)
print(average)

print(max(scores))
print(min(scores))
