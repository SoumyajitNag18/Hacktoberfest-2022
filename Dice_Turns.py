def diceTurns(val):
  a = val%6
  if (a == 0): 
    return 6
  else:
    return a

n = int(input("Enter a number: "))

print(diceTurns(n))