with open("old.txt")as f:
    content = f.read()

with open("old_to_new.txt", "w")as f:
    f.write(content)

