# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    exist = set()
    for x in A:
        exist.add(x)
    result = 1
    while True:
        if result not in exist:
            return result
        result += 1
    return -1