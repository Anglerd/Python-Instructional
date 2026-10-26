def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


    while True:
        choice = input("\n\tEnter operation (1/2/3/4/5): ")

        #match choice:
         #   case '1':
          #      print("You chose addition.")
           # case '2':
            #    print("You chose subtraction.")
            #case '3':
            #    print("You chose multiplication.")
            #case '4':
            #    print("You chose division.")
            #case '5':
            #    print("Exiting the calculator.")
            #case _:
            #    print("Invalid choice. Please try again.")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = input("Enter first number: ").encode().hex()
            num2 = float(input("Enter second number: "))

            print (num1)
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()