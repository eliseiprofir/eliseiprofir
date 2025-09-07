# SIMPLE OPERATIONS BETWEEN TWO NUMBERS
#### Video Demo:  <URL "https://youtu.be/SNUhBZeEEbk">
#### Description: The provided Python program is a simple command-line calculator that allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) between two numbers. It also includes error handling to ensure that users enter valid numeric inputs and handles division by zero errors. Here's a detailed description of the program:

#### The program begins with the definition of four functions: add, sub, mul, and div. Each function takes two parameters a and b, representing the operands for the respective arithmetic operation. Within each function, there is a try block to attempt the operation, and if an exception occurs (e.g., non-numeric input), it returns an error message.
#### add(a, b): Computes the sum of a and b.
#### sub(a, b): Computes the difference between a and b.
#### mul(a, b): Computes the product of a and b.
#### div(a, b): Computes the division of a by b, handling division by zero cases.
#### The main function is the program's core. It starts with a user-friendly menu, displaying the available operations and allowing the user to select one. It uses a while loop to keep the program running until the user chooses to exit (by selecting '0').

#### Inside the loop, the user's choice is captured, and based on their selection, the program prompts the user to enter two numbers for the chosen operation. The input is wrapped in try blocks to catch any invalid input, such as non-numeric characters.

#### After validating the input, the program performs the selected operation using the corresponding function and displays the result. If there's an error during input validation or division by zero, an error message is displayed, ensuring a user-friendly experience.

#### The program also includes an exit option ('0') to gracefully terminate the calculator. If the user enters an invalid choice, it prompts them to try again.

#### Overall, this program is a basic calculator that provides essential arithmetic operations with error handling, making it suitable for performing simple calculations while ensuring robust user interaction.