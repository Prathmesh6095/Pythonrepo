with open("file.txt")as f:
    content1 = f.read()

with open("donke.txt")as f:
    content2 = f.read()

if(content1 == content2):
    print("Print yes these files are identical.")

else:
    print("No not identical")