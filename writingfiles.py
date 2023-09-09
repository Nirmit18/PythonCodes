with open('email.text','r') as emails:
    ans=emails.readlines()

print(ans)       
# it creates an array of gmail

for i in ans:
    if "hotmail" in i:
        # find particular keyboard
        print(i)