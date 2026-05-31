nums = []
while True:
    val = input("Enter number or 'stop': ")
    if val.lower() == "stop":
        break
    try:
        nums.append(float(val))
    except:
        print("Invalid input")
if nums:
    print("Average =", sum(nums)/len(nums))
