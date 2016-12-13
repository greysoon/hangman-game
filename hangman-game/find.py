mString = "hello world"

index = 0

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

positions = findOccurences(mString, "l")

for position in positions:
	mString = mString[:position] + "p" + mString[position + 1:]

print(mString)