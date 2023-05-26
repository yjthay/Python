"""An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited."""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    unique_A = set(A)
    if len(unique_A) != 0:
        max_A = max(unique_A)
        master_set = set([i for i in range(1, max_A + 1)])
        if master_set.difference(unique_A):
            return list(master_set.difference(unique_A))[0]
        else:
            return max_A + 1
    else:
        return 1


if __name__ == '__main__':
    print(solution([2, 3, 1, 5]))  # 4
    print(solution([2]))  # 1
    print(solution([1, 2, 3, 4]))  # 5
    print(solution([2, 3, 4]))  # 1
    print(solution([]))  # 1
    # print(solution([1]))  # 2
