"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    grid = set(i for i in range(1, X + 1))
    max_time = -1
    for time, position in enumerate(A):
        if position <= X and position in grid:
            grid.remove(position)
            max_time = max(max_time, time)
        if not grid:
            break
    return max_time if not grid else -1
    # ordered_A = set(position for position in A if position in grid)
    # ordered_A = [[0, 0]]
    # for time, position in enumerate(A):
    #     print(ordered_A)
    #     if position not in list(zip(*ordered_A))[0]:
    #         ordered_A.append([position, time])
    #     else:
    #         # ordered_A.append([position, min(time, ordered_A[position][1])])
    #         ordered_A[position][1] = min(time, ordered_A[position][1])
    # if grid.difference(set(list(zip(*ordered_A))[0])) != set():
    #     return -1
    # else:
    #     return (max(list(zip(*ordered_A))[1]))


if __name__ == '__main__':
    # print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))  # 6
    print(solution(2, [1, 2, 1, 4, 2, 3, 5, 4]))  # 4
    # print(solution(5, [1, 3, 1, 4, 2, 3, 4, 4]))  # -1 no end
    # print(solution(5, [1, 3, 1, 4, 3, 3, 5, 4]))  # -1 no mid
    # print(solution(5, [2, 3, 2, 4, 2, 3, 5, 4]))  # -1 no start
    # print(solution(2, [1, 10]))  # -1
    # print(solution(7, [1, 7, 6, 5, 4, 3, 2, 1]))  # 6
    # print(solution(7, [1, 3, 10, 2, 12, 23, 4124, 7]))  # -1
