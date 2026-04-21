
with open("file.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("Python" in line):
        print(f"Yes it's present. line no: {lineno}")
        break
    lineno += 1

else:
        print("No Python isn't present.")