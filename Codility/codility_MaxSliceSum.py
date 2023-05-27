"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    max_sum = A[0]
    s = 0
    for value in A:
        s += value
        max_sum = max(max_sum, s)
        if s < 0:
            s = 0
    return max_sum






if __name__ == '__main__':
    print(solution([3, 2, -1, 4, 0]))  # 8
    print(solution([3, 1, -1, 4, 0]))  # 7
    print(solution([3, 1, -6, 4, 0]))  # 4
    print(solution([3]))  # 3
    print(solution([-10]))  # -10
    print(solution([-10, 0]))  # 0
    print(solution([1, -10]))  # 1
    print(solution([-10, 10]))  # 10
    print(solution([-10, -9]))  # -9
    print(solution([-9, -10]))  # -9
