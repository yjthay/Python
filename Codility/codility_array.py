def solution(A, K):
    # Implement your solution here
    if A:
        K = K % len(A)
        return A[-K:] + A[:-K]
    else:
        return A


if __name__ == '__main__':
    print(solution([3, 8, 9, 7, 6], 6))  # [9, 7, 6, 3, 8]
    print(solution([3, 8, 9, 7, 6], 7))  # [9, 7, 6, 3, 8]
    print(solution([3, 8, 9, 7, 6], 8))  # [9, 7, 6, 3, 8]
    print(solution([3, 8, 9, 7, 6], 9))  # [9, 7, 6, 3, 8]
    print(solution([3, 8, 9, 7, 6], 10))  # [9, 7, 6, 3, 8]
    print(solution([0, 0, 0], 3))  # [0, 0, 0]
    print(solution([3, 8, 9, 7, 6], -1))  # [8, 9, 7, 6, 3]
    print(solution([3, 8, 9, 7, 6], 0))  # [3, 8, 9, 7, 6],
    print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
    print(solution([], 3))  # [9, 7, 6, 3, 8]