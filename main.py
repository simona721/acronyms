acronyms = input("Enter your words to create an acronym: ")


words = acronyms.split()
print(words)
letters = [word[0] for word in words]
print("".join(letters).upper())
