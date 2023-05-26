"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # sorted_A = sorted(A)
    # my_dict = {}
    # for i in sorted_A:
    #     my_dict[i] = my_dict.get(i, 0) + 1
    # candidate = max(my_dict, key=my_dict.get)
    # if max(my_dict.values()) > len(A) // 2:
    #     return A.index(candidate)
    # else:
    #     return -1
    sorted_A = sorted(A)
    c = 0
    for idx in range(len(sorted_A)):
        if sorted_A[idx] != sorted_A[idx + 1]:
            c = 1
        else:
            c += 1
        if c > int(len(A) / 2):
            return A.index(sorted_A[idx])
    return -1


if __name__ == '__main__':
    print(solution([10, 2, 5, 1, 8, 20]))  # 1
    print(solution([10, 50, 5, 1]))  # 0
