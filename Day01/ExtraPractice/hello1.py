print("Hello, World!")


term = "Variable"
print(f"Today : {term}") #f = f string

learned = True
definition = False
print(f"Learned : {learned}, Definition : {definition}")

if learned:     
    print("Already learned about variables.")   #Space is important in Python, indentation is used to define blocks of code.
else:
    print("Still learning about variables.")


if term == "Variable" and not learned:
    print("You need to learn about variables.")


tags = ["Python", "Variables"]
tags.append("API")
print(len(tags))
print("API" in tags)