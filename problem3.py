"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully

        newnum = input("Tap the number to add to the list ")

        if newnum == "done":
            break
        
        try:
            number = float(newnum)
            numbers.append(number)
        except ValueError:
            print("This is invalid. Please enter a number or done")
    return numbers
    
def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # TODO: Calculate count
    analysis["count"] = len(numbers)
    # TODO: Calculate sum
    analysis["sum"] = sum(numbers)
    # TODO: Calculate average
    analysis["average"] = analysis["sum"] / analysis["count"]
    # TODO: Find minimum
    analysis["min"] = min(numbers)
    # TODO: Find maximum
    analysis["max"] = max(numbers)
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num.is_integer():  # check only if it's an integer
            if int(num) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    analysis["even_count"] = even_count
    analysis["odd_count"] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    print("\nAnalysis Results:")
    print("-" * 25)
    print(f"Count       : {analysis['count']}")
    print(f"Sum         : {analysis['sum']}")
    print(f"Average     : {analysis['average']:.2f}")
    print(f"Minimum     : {analysis['min']}")
    print(f"Maximum     : {analysis['max']}")
    print(f"Even Count  : {analysis['even_count']}")
    print(f"Odd Count   : {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()