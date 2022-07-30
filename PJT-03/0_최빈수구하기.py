import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input()) # test case int로 받아주기

for i in range(1, T+1): # for문으로 순회하기 range(____) ___범위만큼!
    n = input()
    cnt = [0] * 101 # 인덱스 [0] 첫번째 부터! #101수정
    max = 0 # 가장 많은 인원수
    person = 0
    arr = list(map(int,input().split()))  #리스트 
    for i in range(len(arr)): #리스트 돌면서 
        cnt[arr[i]] += 1 #cnt 1씩 더해주기 
    for j in range(1, len(cnt)): # 최빈값 중 가장 큰 값 구하는 공간   #
        if  max <= cnt[j]:  #mx  #
            max = cnt[j]
            person = j
 
    print('#{} {}'.format(i, person))


# 해쉬 # count 함수 
# 시간복잡도 