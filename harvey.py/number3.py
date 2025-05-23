def calculate_series(n):
    """Calculates and displays the first n terms of the series and their sum.

    Args:
        n: The number of terms to calculate.
    """

    if n <= 0:
        print("Please enter a positive whole number.")  # More beginner-friendly wording
        return

    series = []  # A list to hold the terms of the series
    total_sum = 0  # Start with a sum of zero

    # Loop through the numbers from 1 up to n (including n)
    for i in range(1, n + 1):
        if i % 2 == 1:  # Check if i is odd (1, 3, 5, etc.)
            term = i / (i + 1)  # Calculate the term (positive)
        else:  # If i is even (2, 4, 6, etc.)
            term = -i / (i + 1)  # Calculate the term (negative)

        series.append(term)  # Add the term to the list
        total_sum = total_sum + term  # Add the term to the running total

    print("The first", n, "terms are:", series)  # Print the list of terms
    print("The sum of the terms is:", total_sum)  # Print the final sum


# Get input from the user, and keep asking until they give a valid number
while True:
    try:
        num_terms = int(input("Enter how many terms you want to calculate (a positive whole number): "))
        if num_terms > 0:  # Check if the number is positive
            break  # If it's positive, exit the loop
        else:
            print("Please enter a positive whole number.")  # Tell them to enter a positive number
    except ValueError:  # If they don't enter a number
        print("That's not a number! Please enter a whole number.")


calculate_series(num_terms)  # Call the function to do the calculation and print the results