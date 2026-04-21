words = ["Donkey","bad"]

with open("donke.txt", "r")as f:
    content  = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("donke.txt", "w") as f:
    f.write(content)
