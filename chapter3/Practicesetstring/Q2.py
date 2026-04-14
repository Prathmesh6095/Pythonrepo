# write a program to fill in a letter template given below with name and date
letter  = '''
            Dear <|name|>,
            You are selected!
            <|date|>'''

print(letter.replace("<|name|>","Prathamesh").replace("<|date|>","10-06-2000"))
# print(f"""Dear {name},
# You are selected!
# {date}""") this is also a way

