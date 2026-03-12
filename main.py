from parser import parser, had_error as parser_had_error
import parser

def verify(code):
    print("\n--- Verifying Syntax ---")
    parser.had_error = False
    parser.parser.parse(code)
    if parser.had_error:
        print("Syntax errors found.")
    else:
        print("Syntax is valid! No errors detected.")

def code_input():
    print("\nEnter your JavaScript code below.")
    print("Type 'exit' on a new line to verify.\n")
    code = ""
    while True:
        line = input("js> ")
        if line.strip().lower() == "exit":
            break
        code += line + "\n"
    return code

def main():
    while True:
        print("JavaScript Syntax Verifier (PLY)")
        print("1. Variable declaration/instantiation")
        print("2. Iterative constructs (for/while)")
        print("3. Selective constructs (if/else)")
        print("4. Function declaration")
        print("5. Array declaration")
        print("6. Combination of all the above constructs")
        print("7. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            code = code_input()
            verify(code)

        elif choice == "2":
            code = code_input()
            verify(code)

        elif choice == "3":
            code = code_input()
            verify(code)

        elif choice == "4":
            code = code_input()
            verify(code)

        elif choice == "5":
            code = code_input()
            verify(code)

        elif choice == "6":
            code = code_input()
            verify(code)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.\n")

if __name__ == "__main__":
    main()