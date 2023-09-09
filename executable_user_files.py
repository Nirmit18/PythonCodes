filename=input("enter filename:")
content=input("what is the content:")

with open(filename,'w') as file:
    file.write(content)

open_file=input("Would you like to read to read this file:")
if open_file=='y':
    with open(filename,'r') as file:
        print(file.read())