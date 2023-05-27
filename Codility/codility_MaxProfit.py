"""
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A) == 0:
        return 0
    max_profit = 0
    min_price = A[0]
    for v in A:
        if v < min_price:
            min_price = v
        temp_profit = v - min_price
        if temp_profit > max_profit:
            max_profit = temp_profit
    return max_profit
    # if len(A) == 0:
    #     return 0
    # min_p = A[0]
    # max_profit = 0
    # temp_profit = 0
    # for idx in range(1, len(A)):
    #     if A[idx] < min_p:
    #         min_p = A[idx]
    #         temp_profit = 0
    #     else:
    #         temp_profit += (A[idx] - A[idx - 1])
    #     if max_profit < temp_profit:
    #         max_profit = temp_profit
    # return max_profit


if __name__ == '__main__':
    print(solution([23171, 21011, 21123, 21366, 21013, 21367]))  # 356
    print(solution([100, 105, 100, 99]))  # 5
    print(solution([100, 100, 99]))  # 0
    print(solution([100, 99, 98, 97]))  # 0
    print(solution([100, 101, 102, 103, 104]))  # 4
    print(solution([100, 101, 80, 103, 104]))  # 24
    print(solution(range(1, 200001)))  # 199999
    print(solution([100, 101, 80, 103, 104, 70, 105]))  # 35
    print(solution([1, 2, 3, 5, 1, 10, 1, 20]))  # 19
    print(solution([100, 2, 99, 1]))  # 97
