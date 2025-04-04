#Complex Number Algebra - Show addition, multiplication, negation, and inversion of complex numbers
# in separate functions. (Subtraction and division operations can be made with pairs of these operations.)
# Print the results for each operation tested.

def add_complex(z1,z2):
    return (z1.real +z2.real) +(z1.imag +z2.imag) * 1j

def mult_complex(z1,z2):
    return (z1.real * z2.real) + (z1.imag * z2.imag) * 1j

def neg(z):
    return -z.real - (z.imag * 1j)

def inverse(z):
    if z == 0:
        return "it should be nonzero."
    return 1/(z.real +(z.imag *1j))
def calculator():
    print("Welcome to the complex Algebra!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Inverse")
    print("6.Negation")
    print("0. Exit")

    while True:
        choice = int(input("enter choice (0 for exit):"))

        if choice in [1, 2, 3, 4, 5, 6]:
            n1 = complex(input("enter number 1:"))
        if choice in [1, 2, 3, 4]:
            n2 = complex(input("enter number 2:"))

        if choice == 1:
            print(f"{n1} +{n2} = {add_complex(n1, n2)}")
        elif choice == 2:
            print(f"{n1} -{n2} = {add_complex(n1, neg(n2))}")
        elif choice == 3:
            print(f"{n1}  * {n2} = {mult_complex(n1, n2)}")
        elif choice == 4:
            print(f"{n1} / {n2} = {mult_complex(n1, inverse(n2))}")
        elif choice == 5:
            print(f" inverse of {n1} is {inverse(n1)}")
        elif choice == 6:
            print(f" negation of {n1} is {neg(n1)}")
        elif choice == 0:
            break
        else:
            print(" incorrect input!!")

calculator()
