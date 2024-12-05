import numpy as np

def main():
    print("Welcome to the NumPy demonstration!")

    # User Input: Create a 1D NumPy array
    user_input = input('Enter numbers separated by spaces to create an array [example "1 2 3 4 5 6 7 8 9"]: ')
    try:
        data = np.array([float(x) for x in user_input.split()])
        print("\nYour NumPy Array:", data)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Perform mathematical operations
    print("\nChoose a mathematical operation to perform:")
    print("1. Square each element")
    print("2. Multiply each element by a constant")
    print("3. Compute statistical properties (mean, std dev, sum)")
    print("4. Reshape array into a matrix")
    
    choice = input("\nEnter your choice (1/2/3/4): ")
    
    if choice == '1':
        squared = data ** 2
        print("\nSquared Array:", squared)

    elif choice == '2':
        constant = float(input("Enter the constant to multiply each element: "))
        multiplied = data * constant
        print(f"\nArray multiplied by {constant}:", multiplied)

    elif choice == '3':
        mean = np.mean(data)
        std_dev = np.std(data)
        total_sum = np.sum(data)
        print(f"\nMean: {mean}")
        print(f"Standard Deviation: {std_dev}")
        print(f"Sum of elements: {total_sum}")

    elif choice == '4':
        try:
            rows = int(input("Enter the number of rows for reshaping: "))
            matrix = data.reshape(rows, -1)
            print("\nReshaped Matrix:\n", matrix)
            print("\nMatrix Transpose:\n", matrix.T)
            print("\nDot Product of Matrix with Transpose:\n", np.dot(matrix, matrix.T))
        except ValueError:
            print("Invalid dimensions for reshaping. Ensure the array can be reshaped.")
        except Exception as e:
            print("Error:", e)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()