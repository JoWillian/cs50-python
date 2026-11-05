def main():
  word = input("Greeting: ").strip(" ").lower()
  if word.startswith("hello"):
    print("$0")
  elif word.startswith("h"):
    print("$20")
  else:
    print("$100")

main()
