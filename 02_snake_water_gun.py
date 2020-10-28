import random


def game(comp, you):
    if((comp == you)):
        return None
    elif((comp == 's') and (you == 'w')):
        return False

    elif((comp == 'w') and (you == 's')):
        return True

    elif((comp == 's') and (you == 'g')):
        return True

    elif((comp == 'g') and (you == 's')):
        return False

    elif((comp == 'w') and (you == 'g')):
        return False

    elif((comp == 'g') and (you == 'w')):
        return True


randNo = random.randint(1, 3)
you = input("select s forb snake,  w for water & g for gun : ")

if (randNo == 1):
    comp = 's'
elif(randNo == 2):
    comp = 'w'
else:
    comp = 'g'
print(f"computer choose {comp}")
print(f"you  choose {you}")

win_or_loss = game(comp, you)
if win_or_loss == None:
    print("game has been tied")
elif win_or_loss:
    print("you win this game")
else:
    print("You loose this game ")
