# 정렬되지 않은 부분의 맨 앞 원소를 알맞은 위치에 삽입하는 알고리즘

# 이미 정렬을 마쳤거나, 끝나가는 상태의 정렬에서는 속도가 빠름
# 삽입할 위치가 멀리 떨어져있으면 이동 횟수가 많아짐

# "단순 선택 정렬"과는 
#  1. 값이 가장 작은 원소를 선택하지 않는다는 점이 다름
#  2. 왼쪽에 있는(인접한) 원소와 비교를 하여 안정성이 좋음

# 종료 조건 : 1. 배열의 왼쪽 끝에 도달하는 경우
#             2. tmp 보다 값이 작거나 값이 같은 원소 a[j-1]을 발견할 경우 

## 드모르간 법칙을 이용한 계속조건 생성 : 종료조건 (둘 중에 하나) = 계속조건 (둘다)

# 계속 조건 : 1. j가 0보다 큰 경우
#             2. a[j-1]의 값이 tmp 보다 큰 경우

def insertion_sort(a):
  n = len(a)
  for i in range(1,n):
    j = i
    tmp = a[i]           # 배열의 2번째부터 검사하기 시작
    while j > 0 and a[j-1] > tmp:
      a[j] = a[j-1]
      j -= 1
    a[j] = tmp