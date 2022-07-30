import sys

sys.stdin = open("_문자열의거울상.txt")


T = int(input())
for test_case in range(1, T+1):
    text = list(input())
    text.reverse()
    for t in range(len(text)):
        if text[t] == 'b': text[t] = 'd'
        elif text[t] == 'd': text[t] = 'b'
        elif text[t] == 'p': text[t] = 'q'
        elif text[t] == 'q': text[t] = 'p'

    print("#"+str(test_case), "".join(text))