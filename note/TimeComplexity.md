# Time Complexity (시간 복잡도)

- 알고리즘이 완료되는데 소요되는 시간의 양

- 실행환경에 따라서 실행시간이 달라지기 때문에 `연산의 실행 횟수 카운트`

  - 최악의 경우 시간복잡도 (worst-case analysis)
  - 평균 시간복잡도 (average-case analysis)

  

## Asymptotic Analysis (점근적 분석)

- 데이터의 개수가 n에서 무한으로 증가할 때 수행시간이 증가하는 growth rate로 시간복잡도를 표현하는 기법
-  Big Ω, Big Θ, Big O 표기법 등을 사용
  - Big Ω notation- 최선의 경우
  - Big Θ notation - 평균적인 경우
  - **Big O notation** - 최악의 경우, 가장 많이 사용된다.
  - 세 표기법 모두 데이터 입력값이 충분히 크다고 가정하기 때문에 영향력이 없는 항들은 무시
- 사용법이 간단하고 실행환경에 비의존적이라는 장점



### 1. 상수 시간복잡도 - O(1)

```python
def sample(data, n):
    """리스트의 크기 n에 관계없이 상수시간이 소요되는 함수
    data - 크기가 n인 리스트
    n    - data의 크기
    """
    k = n//2
    return data[k]
```



### 2. 선형 시간복잡도 - O(n)

```python
def sumation(data, n):
    """data 리스트의 합을 구하는 함수
    data - 크기가 n인 리스트
    n    - data의 크기
    """
    sum = 0
    
    for i in data:
        # 이 알고리즘에서 가장 자주 실행되는 코드로 실행횟수는 항상 n
        # 가장 자주 실행되는 문장의 실행횟수가 n번이라면
        # 모든 코드의 실행 횟수나 모든 연산의 실행횟수의 합은 n에 선형적으로 비례
        sum += i
    return sum
```



### 3. 순차탐색 - O(n)

```python
def search(n, data, target):
    for i in range(n):
        # 가장 자주 실행되는 문장으로 최악의 경우 n번 실행
        if data[i] == target:
            return i
    return -1
```



### 4. Quadratic - O(n^2)

```python
def is_distinct(n, x):
    for i in range(n-1):
        for j in range(i+1, n):
            # 가장 자주 실행되는 문장으로 최악의 경우 n(n-1)/2번 실행
            if x[i] == x[j]:
                return False
    return True
```

