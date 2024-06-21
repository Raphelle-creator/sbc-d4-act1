from random import randint

# Define variables for choices
F, U = "F", "U"  # Fold, Unfold

# Generate random choices for computer players
c2, c3 = randint(0, 1), randint(0, 1)

# Get user input and standardize it to capitalized form
user = input("Choose Fold or Unfold:").capitalize()

# Assign user choice to p1
p1 = F if user == "Fold" else U
print("P1 =", p1)

# Assign computer choices based on random values
com2 = F if c2 == 1 else U
com3 = F if c3 == 1 else U

# Print computer choices
print("C2 =", com2)
print("C3 =", com3)

# Determine and print the winner
if (p1 == F and com2 == U and com3 == U) or (p1 == U and com2 == F and com3 == F):
    print("P1 Win!")
elif (p1 == U and com2 == F and com3 == U) or (p1 == F and com2 == U and com3 == F):
    print("C2 Win!")
elif (p1 == U and com2 == U and com3 == F) or (p1 == F and com2 == F and com3 == U):
    print("C3 Win!")
else:
    print("No one wins!")