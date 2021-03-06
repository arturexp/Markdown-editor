mark = "plain bold italic header link inline-code new-line"
formatted_text = []


def formatting():
    print(f"Available formatters: {mark}")
    print("Special commands: !help !done")


def header():
    level = int(input("Level: "))

    if 1 <= level <= 6:
        text = input("Text: ")
        formatted_text.append(f"{'#' * level} {text}\n")
    else:
        print("The level should be within the range of 1 to 6")
        header()


def plain():
    text = input("Text: ")
    formatted_text.append(text)


def bold():
    text = input("Text: ")
    formatted_text.append(f"**{text}**")


def italic():
    text = input("Text: ")
    formatted_text.append(f"*{text}*")


def code():
    text = input("Text: ")
    formatted_text.append(f"`{text}`")


def new_line():
    formatted_text.append("\n")


def link():
    label = input("Label: ")
    url = input("URL: ")
    formatted_text.append(f"[{label}]({url})")


def print_format():
    #print(" ".join(formatted_text))
    for item in formatted_text:
        print(item, end="")
    print()


while True:
    user = input("Choose a formatter: ")
    if user == "!help":
        formatting()
    elif user == "!done":
        break
    elif user not in mark:
        print("Unknown formatting type or command")
    elif user == "header":
        header()
        print_format()
    elif user == "plain":
        plain()
        print_format()
    elif user == "bold":
        bold()
        print_format()
    elif user == "inline-code":
        code()
        print_format()
    elif user == "link":
        link()
        print_format()
    elif user == "new-line":
        new_line()
        print_format()
    elif user == "italic":
        italic()
        print_format()
