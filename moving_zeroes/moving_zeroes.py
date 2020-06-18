'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    lst = []
    for i in arr:
        if i == 0:
            lst.append(i)
        else:
            lst.insert(0, i)
    return lst


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


def moving_zeroes_v2(arr): # O (n^2)
    for i in range(len(arr)): # O(n)
        x = arr[i]
        if x != 0:
            arr = [x] + arr[:i] + arr[i+1:] # O(n)
    return arr