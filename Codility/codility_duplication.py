def solution(A):
    # for value in set(A):
    #     if A.count(value) % 2 != 0:
    #         return value O(N**2)
    my_dict = {}
    for value in A:
        my_dict[value] = my_dict.get(value, 0) + 1
        if my_dict[value] % 2 == 0:
            my_dict.pop(value)
    return [*my_dict.keys()][0]

if __name__ == '__main__':
    print(solution([9, 3, 9, 3, 9, 7, 9]))
