text = ""

for c in input("Input: "):
    if c in ["A", "E", "I", "O", "U", "a", "e", 'i', 'o', 'u']:
        pass
    else:
        text += c

print("Output: " + text)
