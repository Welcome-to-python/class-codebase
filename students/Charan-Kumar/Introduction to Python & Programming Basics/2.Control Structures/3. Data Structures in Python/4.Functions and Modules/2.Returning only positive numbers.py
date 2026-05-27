def positive_numbers(nums):
    return [i for i in nums if i > 0]

# User input
nums = list(map(int, input("Enter numbers separated by space: ").split()))

print("Positive numbers:", positive_numbers(nums))