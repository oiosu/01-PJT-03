import sys

sys.stdin = open("_소득불균형.txt")


#오류가 있는 코드 
# T = int(input())

# for i in range(1, T+1):
#     N = int(input())
# result = list(map(int, input().split()))
# result_avg = sum(result)/N
# cnt = 0 
# for j in range (result):
#     if j <= result_avg:
#         cnt += 1

# print('#{} {}'.format(i, cnt))


T = int(input())  # test case int로 받아주기

for i in range(1, T + 1) : #for 문을 통해 다음과 같은 범위 만큼! 
    n = int(input())
    data = list(map(int, input().split()))  #데이터 리스트 맵핑 
    sum_value = sum(data)     # sum의 값과 평균값을 구하는 공간 
    avg_value = sum_value / n

    result = 0 #result 초기화 
    for p in data :
        if p <= avg_value :   # 평균값 이하일 경우
            result += 1  # result에 1씩 더해준다. 

    print('#%d %d' % (i, result))



total_t = int(input())