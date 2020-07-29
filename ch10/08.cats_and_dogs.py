def read_files(files):
    for file in files:
        print("File name: " + file)
        try:
            with open(file) as f:
                contents = f.read()
                print(contents.rstrip())
        except FileNotFoundError:
            print("ERROR -- The file " + file + " wasn't found")


read_files(["ch10/cats.txt", "ch10/dogs.txt"])

