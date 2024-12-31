def greeting():
    greet = input("Greeting: ")
    if greet.strip().lower() == "hello":
        print("$0")
    elif greet.strip().lower()[0] == "h":
        print("$20")
    else:
        print("$100")

greeting()
