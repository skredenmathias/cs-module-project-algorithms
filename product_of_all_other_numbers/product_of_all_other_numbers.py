'''
Input: a List of integers
Returns: a List of integers
'''
from functools import reduce

def product_of_all_other_numbers(arr):
    # store all values in a separate array
    original_values = arr.copy() #? O(n)
    # multiplies all values in array
    product = reduce(lambda x, y: x*y, arr)
    # replace all values in array with above number
    for elem in range(len(arr)): #? O(n)
        arr[elem] = product

    # now divide each index by its value
    for i in range(len(arr)): #? o(n)
        arr[i] = arr[i] // original_values[i] #? O
    return arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
