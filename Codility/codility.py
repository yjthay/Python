def solution(N):
    # Implement your solution here
    str_bin = bin(N)[2:]

    max_gap, current_gap = 0, 0
    left_pointer, right_pointer = 0, 0
    for idx, char in enumerate(str_bin):
        if char == '1':
            # right_pointer = idx
            # left_pointer, right_pointer = swap_pointers(left_pointer, right_pointer)
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
            continue
        current_gap += 1
    return max_gap


def swap_pointers(left_pointer, right_pointer):
    right_pointer = left_pointer
    return left_pointer, right_pointer


if __name__ == '__main__':
    print(solution(9))  # 2
    print(solution(20))  # 1
    print(solution(32))  # 0
    print(solution(15))  # 0
    print(solution(529))  # 4
    print(solution(1041))  # 5
