print("what phrase do you see?")
phrase = input()
print()
print("reversing...")
print()
for char in range(len(phrase) - 1, -1, -1):
  print(phrase[char], end="")
