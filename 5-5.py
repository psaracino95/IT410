numbers = list(range(1, 56))
numT = 34
numF = 78

#Named T and F to determin which should prove True.
if numT in numbers:
    print(f"{numT} was found in the list.")
else:
    print(f"{numT} was not found in the list.")

if numF in numbers:
    print(f"{numF} was found in the list.")
else:
    print(f"{numF} was not found in the list.")