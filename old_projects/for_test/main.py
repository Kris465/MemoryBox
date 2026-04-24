from calculator import Calculator
from loguru import logger

def main():
    logger.info("Starting calculator")
    calc = Calculator()

    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            logger.info("Exiting calculator")
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"Result: {result}")
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"Result: {result}")
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"Result: {result}")
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    print(f"Result: {result}")
            except ValueError as e:
                logger.error(f"Error: {e}")
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
