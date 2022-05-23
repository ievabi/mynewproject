
def try_me():
    num = int(input("Pick a number from 1-10: "))
    if num in range(1,11):
        return print(f"Good choice! You picked {num}")

    return print("Why do you waste my time?Bye!")
