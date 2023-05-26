"""Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited."""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B, K):
    # Implement your solution here
    return len(range(A + (K - A % K) % K, B + 1, K))


if __name__ == '__main__':
    print(solution(6, 11, 2))  # 3
    print(solution(6, 11, 10))  # 0
    print(solution(1, 20, 2))  # 10
    print(solution(1, int(2e9), 8))  # 10
    print(solution(7, 26, 5))  # 4
