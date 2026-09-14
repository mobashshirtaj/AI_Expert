print("Hello! I'm your friendly chatbot.")
name = input("What's your name? ")
print(f"\nNice to meet you, {name}!\n")
feeling = input("How are you feeling today? ")
feel = ['good','great','happy','superb','wonderful','splendid','fantastic','delighted','thrilled','overjoyed']
if feeling.lower() in feel:
    print("\nI'm glad to hear that!\n")
else:
    print("\nI hope your day gets better!\n")

hobby = input("What's your favorite hobby? ")
print(f"\nWow, {hobby} sounds fun!\n")
