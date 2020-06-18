'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
arrA = [1,1,2,2,3,4,4]
def single_number(arr):
    for elem in arr:
        if arr.count(elem) == 1:
            return elem

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

def single_number_v2(arr):
    no_dups = []

    for elem in arr:
        if elem not in no_dups:
            no_dups.append(num)
        else:
            no_dups.remove(elem)
    return no_dups[0]

def single_number_v3(arr):
    counts = {}

    for elem in arr:
        if elem in counts:
            del ounts[elem]
        else:
            counts[elem] = 1

    for k, v in counts.items():
        if v == 1:
            return k
            # OR: counts[counts.keys()[0]]
    return 