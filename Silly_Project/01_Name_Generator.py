
import random
import sys
import pandas as pd


def Create_Name_Sets():
    df = pd.read_fwf("\names.txt", sep=" ", header = None)
    firstName = set()
    lastName = set()
    for i, person in df.iterrows():
        full_name = person[0].split(",")
        if len(full_name) > 1:
            last_name = full_name[0]
            lastName.add(last_name)
            first_name = full_name[1].split(" ")[1]
            firstName.add(first_name)

    return firstName, lastName


def Random_Name ():
    firstName, lastName = Create_Name_Sets()

    firstNameSelect = random.choices(list(firstName), k=1)
    lastNameSelect= random.choices(list(lastName), k=1)
    fullName = firstNameSelect + lastNameSelect
    print(*fullName, file=sys.stderr)


def Play_Game ():
    while True:
            random_name()
            play_again = input("Press T to Play again or Press N to quit \n")
            if play_again.lower() == "n":
                break





Play_Game()

