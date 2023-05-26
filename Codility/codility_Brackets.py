"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    symbols_dict = {'(': ')', '[': ']', '{': '}'}
    output = []
    for symbol in S:
        if symbol not in symbols_dict and not output:
            return 0  # not properly nested
        elif symbol in symbols_dict:
            output.append(symbol)
        else:
            last_symbol = output.pop()
            if symbols_dict[last_symbol] != symbol:
                return 0
    return 1 if not output else 0
    pass


if __name__ == '__main__':
    print(solution("{[()()]}"))  # 1
    print(solution("([)()]"))  # 0
    print(solution(""))  # 1
    print(solution("()[]"))  # 1
    print(solution("]"))  # 0
    print(solution("()[]{}{"))  # 0
    print(solution("{"))  # 0
