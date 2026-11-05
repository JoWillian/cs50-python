def main():
    user_twt = input("Input: ")
    print(omit(user_twt))

def omit(text):
    twt = ""
    for letter in text:
        if letter not in "AEIOUaeiou":
            twt += letter

    return twt

main()
