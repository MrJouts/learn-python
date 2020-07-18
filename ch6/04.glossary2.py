glossary = {
    "string": "chain of characters",
    "indentation": "left espace at the beginning of a line",
    "if": "conditional clause",
    "or": "comparicion operator",
    "python": "Programming language",
    "for": "loop through a list",
    "dictionaries": "key value pair storage",
    "list": "list of values",
}

for word, meaning in glossary.items():
    print(str(word.title()) + ": " + str(meaning))
