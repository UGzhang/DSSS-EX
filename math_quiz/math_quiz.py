import random


def random_int(min, max):
    """
    Generate a random integer between the specified min and max values.

    Args:
        min (int): The minimum value of the random integer.
        max (int): The maximum value of the random integer.

    Returns:
        int: A random integer between min and max, inclusive.
    """
    return random.randint(min, max)


def random_operator():
    """
    Select a random arithmetic operator from the list ['+', '-', '*'].

    Returns:
        str: A random operator chosen from ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def get_problem_answer(n1, n2, o):
    """
    Generate a mathematical problem and calculate its answer.

    Args:
        n1 (int): The first operand of the arithmetic problem.
        n2 (int): The second operand of the arithmetic problem.
        o (str): The operator for the arithmetic problem, one of ['+', '-', '*'].

    Returns:
        tuple: A tuple containing the problem as a string (str) and the answer (int).
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
       A math quiz game that asks the user a series of random math problems
       and checks their answers. And print the user's score at the end.
    """
    correct = 0  # correct count
    total = 5  # repeat count

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total):
        n1 = random_int(1, 10); n2 = random_int(1, 15); o = random_operator()

        PROBLEM, ANSWER = get_problem_answer(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        while True:  # Loop to keep asking for input until valid input is given
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)

                if useranswer == ANSWER:
                    print("Correct! You earned a point.")
                    correct += 1
                else:
                    print(f"Wrong answer. The correct answer is {ANSWER}.")
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    print(f"\nGame over! Your score is: {correct}/{total}")

if __name__ == "__main__":
    math_quiz()
