"""A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited."""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # east, west = 0, 1
    # counter = {}
    # for idx, car_direction in enumerate(A):
    #     if car_direction == east:
    #         counter[idx] = 0
    #     else:
    #         counter = {key: counter[key] + 1 for key in counter}
    # return sum(counter.values())

    east, west = 0, 1
    counter = 0
    multiplier = 0
    for idx, car_direction in enumerate(A):
        if car_direction == east:
            multiplier += 1
        else:
            counter += multiplier
    return counter if counter <= 1e9 else -1


if __name__ == '__main__':
    print(solution([0, 1, 0, 1, 1]))  # 5
    print(solution([0, 0]))  # 0
    print(solution([1, 1]))  # 0
    print(solution([1, 0]))  # 0
    print(solution([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]))  # 0
    print(solution([0, 1, 1, 1, 1, 1, 1, 1]))  # 7
