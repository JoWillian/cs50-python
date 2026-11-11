def main():
    grocery = []
    while True:
        try:
            grocery.append(str(input().strip().upper()))
        except EOFError:
            for item in sorted(set(grocery)):
                print(f"{grocery.count(item)} {item}")
            break

main()
