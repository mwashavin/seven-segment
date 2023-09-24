word = input("enter a word").upper()
strn = input("enter string to search: ").upper()

found = True
start = 0
for ch in word:
    pos = strn.find(ch, start)
    if pos < 0:
        found = False
        break
    start = pos + 1
if found:
    print("Yes")
else:
    print("No")