from collections import OrderedDict

glossary = {}
# glossary = OrderedDict()

glossary["string"] = "chain of characters"
glossary["or"] = "comparicion operator"
glossary["indentation"] = "left espace at the beginning of a line"
glossary["python"] = "Programming language"
glossary["if"] = "conditional clause"
glossary["list"] = "list of values"

for word, meaning in glossary.items():
    print(str(word.title()) + ": " + str(meaning))

