with open("file.txt") as f:
    content = f.read()

if ("Python" in content):
    print("Yes it's present.")
else:
    print("No Python isn't present.")