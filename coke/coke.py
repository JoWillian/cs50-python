def main():
    amount = 0
    while amount < 50:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
           amount += coin

        print(f"Amount Due: {50 - amount}")

    print(f"Change Owed: {abs(amount - 50)}")

main()
