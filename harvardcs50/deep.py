def great_answer():
    answer = input("What is the answer to life, the universe and everything? ")
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

great_answer()