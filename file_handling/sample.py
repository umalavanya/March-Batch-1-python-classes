with open("example.txt", "r") as text_file:
    content = text_file.read()
    print("Content of text file:")
    print(content)

text_file.close()


