"""A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited."""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(set(A)) != len(A):
        return 0
    perm_list = set(i for i in range(1, len(A) + 1))
    for value in A:
        if value in perm_list:
            perm_list.remove(value)
        else:
            return 0
    return 1 if not perm_list else 0




if __name__ == '__main__':
    print(solution([2, 3, 1]))  # 1
    print(solution([4, 1, 3]))  # 0
    print(solution([1, 1, 2]))  # 0
    print(solution([1, 4, 2]))  # 0
    print(solution([1, 5, 2]))  # 0
