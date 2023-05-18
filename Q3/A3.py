def compute(n):
    # Check if n is less than 10
    if n < 10:
        out = n ** 2
    # Check if n is between 10 and 20
    elif n < 20:
        out = 1
        # Compute the factorial of (n-10) using a loop
        for i in range(1, n-10+1):
            out *= i
    # For n greater than or equal to 20
    else:
        lim = n - 20
        # Compute the sum of numbers from 1 to lim
        out = lim * (lim + 1) / 2
    print(out)

# Get user input for n
n = int(input("Enter an integer: "))

# Call the compute function with the user input
compute(n)

"""
Explanation of the code:
1.The compute function takes an integer n as input.
2.If n is less than 10, it computes the square of n and assigns it to out.
3.If n is between 10 and 20, it initializes out to 1 and computes the factorial of (n-10) using a loop.
4.If n is greater than or equal to 20, it calculates the sum of numbers from 1 to (n-20) and assigns it to out.
6.The result out is printed.
7.User input for n is obtained using the input function and converted to an integer.
8.The compute function is called with the user input as the argument.
"""

"""
To run the code:
1.Copy the code and save it to a Python file with a .py extension (e.g., filename.py).
2.Make sure you have Python installed on your system.
3.Open a command prompt or terminal and navigate to the directory where the Python file is saved.
4.Run the code by typing python filename.py and pressing Enter.
5.Follow the prompt to enter an integer value for n.
6.The program will compute the result based on the given input and display the output.
"""

