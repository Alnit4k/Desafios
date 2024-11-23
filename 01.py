import math

def calculate_ratios(arr):
    n = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n
    
    return positive_ratio, negative_ratio, zero_ratio

# Example input
arr = []
for arr in range (6):
    n=int(input())
    arr.append(n)
    


positive_ratio, negative_ratio, zero_ratio = calculate_ratios(arr)

print("{:.6f}".format(positive_ratio))
print("{:.6f}".format(negative_ratio))
print("{:.6f}".format(zero_ratio))

