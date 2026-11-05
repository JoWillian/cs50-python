def main():
    user_time = input("What time is it? ")
    conv_time = convert(user_time)
    if 7 <= conv_time <= 8:
      print("breakfast time")
    elif 12 <= conv_time <= 13:
      print("lunch time")
    elif 18 <= conv_time <= 19:
      print("dinner time")

def convert(time):
    t = time.strip().split(":")
    t1 = int((t[0]))
    t2 = float((t[1]))
    total = t1 + (t2 / 60)
    return round(total,2)

if __name__ == "__main__":
    main()
