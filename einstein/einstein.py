def formula(mass):
    mass = mass * 90000000000000000
    return mass

def main():
    result = formula(int(input("m: ")))
    print(result)

main()
