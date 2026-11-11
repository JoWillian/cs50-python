def main():
    calendar = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
    }
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                date = date.replace("/"," ").strip().split(" ")
                if date[0].isdigit():
                    day = int(date[1])
                    month = int(date[0])
                    year = int(date[2])
                else:
                    continue
            elif "," in date:
                date = date.replace(",","").strip().split(" ")
                if date[0].isalpha():
                    day = int(date[1])
                    month = int(calendar[date[0]])
                    year = int(date[2])
                else:
                    continue
            else:
                continue
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02d}-{day:02d}")
                break
            else:
                continue
        except (IndexError,ValueError,KeyError):
            pass

if __name__ == "__main__":
    main()
