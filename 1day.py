# Function to sort array of 0s, 1s, and 2s
# Using Dutch National Flag Algorithm
def sort012(arr):
    low = 0        # Pointer for 0
    mid = 0        # Pointer for 1
    high = len(arr) - 1  # Pointer for 2

    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[low] and arr[mid]
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            # Swap arr[mid] and arr[high]
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Example usage
arr = [0, 1, 2, 1, 0, 2, 1, 0]
print("Original array:", arr)

sort012(arr)

print("Sorted array:  ", arr)
