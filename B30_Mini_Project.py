#Class SN: B30
# Student Score Analyzer - Week 1 Project

def get_score(prompt):
    """
    Ask the user for a valid score between 0 and 100.
    Keeps asking until a valid number is entered.
    """
    while True:
        try:
            score = float(input(prompt))  # convert input to float

            if 0 <= score <= 100:
                return score  # valid input
            else:
                print("Score must be between 0 and 100. Try again.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    print("===== Student Score Analyzer =====")

    while True:  # BONUS: multiple students loop

        # Collect scores
        score1 = get_score("Enter score 1 (0-100): ")
        score2 = get_score("Enter score 2 (0-100): ")
        score3 = get_score("Enter score 3 (0-100): ")

        # Calculate average
        average = (score1 + score2 + score3) / 3

        # Determine pass/fail
        if average >= 50:
            result = "PASS "
        else:
            result = "FAIL "

        # Print summary
        print("\n===== STUDENT SUMMARY =====")
        print(f"Score 1: {score1}")
        print(f"Score 2: {score2}")
        print(f"Score 3: {score3}")
        print(f"Average: {average:.2f}")
        print(f"Result: {result}")
        print("===========================\n")

        # Ask for another student
        again = input("Another student? (y/n): ").lower()
        if again != "y":
            print("Goodbye ")
            break


# Run program
if __name__ == "__main__":
    main()