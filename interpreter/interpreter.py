def main():
  math = input("Expression: ").split()
  n1 = int(math[0])
  n2 = math[1]
  n3 = int(math[2])

  if n2 == "-":
    print(f"{(n1 - n3):.1f}")
  elif n2 == "+":
    print(f"{(n1 + n3):.1f}")
  elif n2 == "/":
    print(f"{(n1 / n3):.1f}")
  elif n2 == "*":
    print(f"{(n1 * n3):.1f}")
  else:
    return print("Operator not find")

main()
