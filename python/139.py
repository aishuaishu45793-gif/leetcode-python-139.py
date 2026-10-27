try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    if numbers:
        print("Largest number:", max(numbers))
        print("Smallest number:", min(numbers))
    else:
        print("Please enter at least one number.")

except ValueError:
    print("Invalid input! Please enter integers only.")