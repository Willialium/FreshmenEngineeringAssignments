# Get's the data from the user and initializes variables
value = float(input("Enter number: "))
min = value
max = value
sum = 0
total = 0

# Continues to get values until one is less than 0
while(value >= 0):
    # Keeps track of number of numbers inputed
    total += 1
    sum += value
    # If value is higher than max or lower than min, make it the new max or min
    if(value > max):
        max = value
    if(value < min):
        min = value
    value = float(input("Enter number: "))

# Prints results to screen
mean = sum / total
print("The min is {}, the max is {}, and the mean is {}".format(min, max, mean))