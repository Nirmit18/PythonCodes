with open('PrintFormatting.py','r') as file:
    print(file.read())



#second way is using content 
# file can be accessed outside the fun
with open('PrintFormatting.py','r') as file:
    content=file.read()


print(content)