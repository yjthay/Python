"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    if len(A) == 0:
        return 0
    S, E, CS, CE = [0] * len(A), [0] * len(A), [0] * len(A), [0] * len(A)

    for idx in range(len(A)):
        S[idx] = max(0, idx - A[idx])
        E[idx] = min(len(A) - 1, idx + A[idx])
        CS[S[idx]] += 1
        CE[E[idx]] += 1

    CCS, CCE = [0] * len(A), [0] * len(A)
    CCS[0], CCE[0] = CS[0], CE[0]
    for i in range(1, len(A)):
        CCS[i] = CS[i] + CCS[i - 1]
        CCE[i] = CE[i] + CCE[i - 1]

    print(S, CS, CCS, E, CE, CCE)
    r = 0
    for i in range(len(A)):
        if i == 0:
            r += (CCS[i] - CS[i]) * CS[i] + CS[i] * (CS[i] - 1) / 2
        else:
            tot += (CCS[i] - CCE[i - 1] - CS[i]) * CS[i] + CS[i] * (CS[i] - 1) / 2

    return int(tot) if int(tot) < 10000000 else -1


if __name__ == '__main__':
    print(solution([1, 5, 2, 1, 4, 0]))  # 11
