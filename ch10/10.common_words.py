def count_words(files):
    for file in files:
        with open(file) as f:
            contents = f.read()
            count = contents.lower().count("the")
            print("File name: " + file + " | " + str(count))


books = ["books/boy_scouts.txt", "books/toto.txt", "books/tw_magazine.txt"]

count_words(books)

