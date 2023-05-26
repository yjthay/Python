"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S is made only of the characters '(' and/or ')'.
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    nest_dict = {'(':')'}
    tracker = []
    for char in S:
        if char in nest_dict.keys():
            tracker.append(char)
        elif not tracker:
            return 0
        else:
            tracker.pop()
    return 1 if not tracker else 0


if __name__ == '__main__':
    print(solution("(()(())())"))  # 1
    print(solution("())"))  # 0
    print(solution(""))  # 10
    print(solution("((()))"))  # 1
    print(solution(")"))  # 0
