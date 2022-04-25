# [Programmers] 소수 만들기

:writing_hand: [h0meb0dy](mailto:h0meb0dysj@gmail.com)

> https://programmers.co.kr/learn/courses/30/lessons/12977

## 문제 설명

주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

## 제한사항

- nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
- nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

## 입출력 예

| nums        | result |
| ----------- | ------ |
| [1,2,3,4]   | 1      |
| [1,2,7,6,4] | 4      |

## 입출력 예 설명

입출력 예 #1
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.

## Solve

### Idea

`nums`에 있는 수들은 1이상 1000 이하의 자연수이므로, 세 개의 수를 더하면 3000 이하의 수가 된다. 처음에 3000 이하의 소수들을 모두 구해놓으면 매번 소수인지 판별하지 않아도 되므로 시간을 절약할 수 있다.

### Code

```python
is_prime = [True for number in range(3001)] # if n is prime number, is_prime[n] = True

def prime_init():
    is_prime[0] = False # 0 is not prime number
    is_prime[1] = False # 1 is not prime number

    for num in range(4, 3001):
        for divider in range(2, int(num / 2) + 1):
            if is_prime[divider] == False:
                continue
            if num % divider == 0: # num is not prime number
                is_prime[num] = False
                break

def solution(nums):
    prime_init() # get prime numbers between 1 and 3000

    answer = 0

    for idx1 in range(len(nums)):
        for idx2 in range(idx1 + 1, len(nums)):
            for idx3 in range(idx2 + 1, len(nums)):
                if is_prime[nums[idx1] + nums[idx2] + nums[idx3]] == True:
                    answer += 1

    return answer
```