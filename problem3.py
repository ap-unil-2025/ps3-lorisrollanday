"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.
    """
    numbers = []

    while True:
        newnum = input("Enter a number (or type 'done' to finish): ")

        if newnum.lower() == "done":
            break
        
        try:
            number = float(newnum)
            numbers.append(number)
        except ValueError:
            print("❌ Invalid input. Please enter a valid number or 'done'.")

    return numbers
    

def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - min: smallest number
    - max: largest number
    - even_count: count of even integers
    - odd_count: count of odd integers
    """
    if not numbers:
        return None

    analysis = {}

    # Basic stats
    analysis["count"] = len(numbers)
    analysis["sum"] = sum(numbers)
    analysis["average"] = analysis["sum"] / analysis["count"]
    analysis["minimum"] = min(numbers)   # ✅ changer clé
    analysis["maximum"] = max(numbers)   # ✅ changer clé

    # Count even & odd (only for integers)
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num.is_integer():
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
    """
    if not analysis:
        print("⚠️ No analysis available (empty list).")
        return

    print("\n📊 Analysis Results:")
    print("-" * 30)
    print(f"Count       : {analysis['count']}")
    print(f"Sum         : {analysis['sum']}")
    print(f"Average     : {analysis['average']:.2f}")
    print(f"Minimum     : {analysis['min']}")
    print(f"Maximum     : {analysis['max']}")
    print(f"Even Count  : {analysis['even_count']}")
    print(f"Odd Count   : {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("=== Number Analyzer ===")
    print("Enter numbers one at a time. Type 'done' when finished.\n")

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("⚠️ No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()