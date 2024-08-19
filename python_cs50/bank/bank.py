text = input("Greeting: ").strip().lower()

if text.find("hello") == 0:
    print("$0")
elif text.find("h") == 0:
    print("$20")
else:
    print("$100")
