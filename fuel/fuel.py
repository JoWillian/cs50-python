def main():
    while True:
        try:
            print(volume(input("Fraction: ")))
            break
        except (ValueError,ZeroDivisionError):
            pass

def volume(fraction):
    fraction = fraction.split("/")
    num = int(fraction[0])
    den = int(fraction[1])
    if num <= den and num >= 0 and den > 0:
        percentage = round((num / den),2)
        if percentage >= 0.99:
            return "F"
        elif percentage <= 0.01:
            return "E"
        else:
            return f"{percentage:.0%}"
    else:
        raise ValueError

main()
