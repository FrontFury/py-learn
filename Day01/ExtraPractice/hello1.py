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

note = {"term": "Variable", "definition": "A variable is a container for storing data values."}
print(note["term"])


notes = [
    {
        "id": 1,
        "term": "list",
        "definition": "An ordered, mutable collection of items.",
        "js_equivalent": "array",
        "tags": ["python", "data-structures"],
        "learned": True,
    },
    {
        "id": 2,
        "term": "dictionary",
        "definition": "A collection of unordered key-value pairs.",
        "js_equivalent": "object",
        "tags": ["python", "data-structures"],
        "learned": True,
    },
    {
        "id": 3,
        "term": "f-string",
        "definition": "A string literal prefixed with 'f' that evaluates expressions inside curly braces.",
        "js_equivalent": "template literal",
        "tags": ["python", "strings"],
        "learned": False,
    },
    {
        "id": 4,
        "term": "def",
        "definition": "The keyword used to define a reusable block of code.",
        "js_equivalent": "function",
        "tags": ["python", "functions"],
        "learned": False,
    },
]


for note in notes:
    print(note["term"])


query = "LI"

for note in notes:
    if query.lower() in note["term"].lower():
        print("Found:", note["term"])