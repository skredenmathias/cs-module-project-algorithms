'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
arrA = [1,1,2,2,3,4,4]
def single_number(arr):
    # Your code here
    for elem in arr:
        if arr.count(elem) == 1:
            return elem

    


    # OR:
    # create list, input all numbers that are duplicates
    # lst = []
    # for elem in range(len(arr)):
    #     for j in range(elem+1, len(arr)):
    #         if arr[elem] == arr[j]:
    #             lst.append(arr[elem])
    # check which element of arr does not appear in new list
    # return that element
    # for i in lst: #? reminder: confused about when to use lst, range(), len()
    #     for j in arr:
    #         if i != j:
    #             return j

# print(single_number(arrA))


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")