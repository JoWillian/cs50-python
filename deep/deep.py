x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").replace(" ","").lower()

match x:
  case "42" | "forty-two" | "fortytwo":
    print("Yes")
  case _:
    print("No")

