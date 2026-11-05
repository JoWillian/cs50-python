def main():
    camel_case = input("camelCase: ")
    print(snake_case(camel_case))

def snake_case(text):
    snake = ("")
    for letter in text:
        if letter.isupper():
            snake += "_"
            snake += letter
        else:
            snake += letter

    return print(snake)

main()
