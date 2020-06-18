'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import time
# start_time = time.time()
def sliding_window_max(nums, k):
    max_values = []
    for i in range(len(nums)): # O(n) ?
        # move window
        window = nums[i:k+i]

        # restrict results
        if len(window) == 3:
            # extract largest value
            max_value = max(window)
            max_values.append(max_value)
    return max_values

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

# end_time = time.time()
# print(end_time - start_time)