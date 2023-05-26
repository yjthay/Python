"""This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited."""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    # B = sorted(A)
    # positive_list = list(filter(lambda x: x > 0 and x <= max(B), B))
    # if not positive_list:
    #     return 1
    # return min(set([i + 1 for i in range(positive_list[-1] + 1)]).difference(positive_list))

    # Implement your solution here
    # Use a set instead of a list for faster lookup and difference operations
    B = set(A)
    # Find the smallest positive integer that is not in B
    i = 1
    while i in B:
        i += 1
    return i

if __name__ == '__main__':
    # print(solution([1, 2, 3]))  # 4 ending
    # print(solution([2, 3, 4, 5]))  # 1
    print(solution([1, 3, 6, 4, 1, 2, 8]))  # 5 multiple
    # print(solution([1, 3, 6, 4, 1, 2, 2, 2, 8]))  # 5 multiple
    # print(solution([-1, -2, -3]))  # 1 starting
    # print(solution([-1, -2, -3, 2]))  # 1
    # print(solution([-1000, -2, -3, 2]))  # 1
