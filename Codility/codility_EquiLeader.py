"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    counter = 0
    leader_dict = {}
    for val in A:
        leader_dict[val] = leader_dict.get(val, 0) + 1

    left_dict = {}
    for val in A:
        left_dict[val] = left_dict.get(val, 0) + 1
        leader_dict[val] -= 1

        left_leader = max(left_dict, key=left_dict.get)
        left_leader = left_leader if left_dict[left_leader] > sum(left_dict.values()) // 2 else None
        right_leader = max(leader_dict, key=leader_dict.get)
        right_leader = right_leader if leader_dict[right_leader] > sum(leader_dict.values()) // 2 else None

        if left_leader == right_leader and left_leader != None and right_leader != None:
            counter += 1
    return counter


if __name__ == '__main__':
    print(solution([4, 3, 4, 4, 4, 2]))  # 2
    print(solution([4, 4]))  # 1
    print(solution([4, 3]))  # 0
    print(solution([4, 3, 4]))  # 0
