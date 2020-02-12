input = input("Enter the stuff to spongebob case: ")

counter = 0
newString = ""

for x in input.lower():
  if x != " ":
    if counter % 2 == 0:
      newString += x.upper()
    else:
      newString += x
    counter += 1
  else:
    newString += " "

print(newString)