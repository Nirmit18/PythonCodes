
import random


while(1):
    a=input("enter what u wish:")
    b=random.choice(["stone","paper","scissor"])
    print("b is",b)
    if a=="stone" and b!="paper" and b!="stone":
        print("you won")
        break
    elif a=="paper" and b!="scissor" and b!="paper":
        print("you won")
        break

    elif a=="scissor" and b!="stone" and b!="scissor":
        print("you won")
        break

    else:
        continue
    
print("game over")