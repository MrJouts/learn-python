favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

users = ["jen", "emi", "sarah", "mike"]

for name, language in favorite_languages.items():
    # print(name.title())
    if name.lower() in users:
        print(
            str(name.title()) + " thanks for your response on " + str(language.title())
        )
    else:
        print("Hello " + str(name.title()) + ", please take this survey")
