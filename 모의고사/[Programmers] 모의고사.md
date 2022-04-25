# [Programmers] 모의고사

:writing_hand: [h0meb0dy](mailto:h0meb0dysj@gmail.com)

> https://programmers.co.kr/learn/courses/30/lessons/42840

## 문제 설명

수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

## 제한 조건

- 시험은 최대 10,000 문제로 구성되어있습니다.
- 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

## 입출력 예

| answers     | return  |
| ----------- | ------- |
| [1,2,3,4,5] | [1]     |
| [1,3,2,4,2] | [1,2,3] |

## 입출력 예 설명

입출력 예 #1

- 수포자 1은 모든 문제를 맞혔습니다.
- 수포자 2는 모든 문제를 틀렸습니다.
- 수포자 3은 모든 문제를 틀렸습니다.

따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

- 모든 사람이 2문제씩을 맞췄습니다.

## Solve

```python
def solution(answers):
    # calculate supoja1's score
    supoja1_score = 0
    for prob_num in range(len(answers)):
        if answers[prob_num] == prob_num % 5 + 1:
            supoja1_score += 1

    # calculate supoja2's score
    supoja2_score = 0
    for prob_num in range(len(answers)):
        if prob_num % 2 == 0:
            if answers[prob_num] == 2:
                supoja2_score += 1
        elif prob_num % 8 == 1 or prob_num % 8 == 3:
            if answers[prob_num] == prob_num % 8:
                supoja2_score += 1
        elif prob_num % 8 == 5:
            if answers[prob_num] == 4:
                supoja2_score += 1
        elif prob_num % 8 == 7:
            if answers[prob_num] == 5:
                supoja2_score += 1

    # calculate supoja3's score
    supoja3_score = 0
    for prob_num in range(len(answers)):
        if prob_num % 10 == 0 or prob_num % 10 == 1:
            if answers[prob_num] == 3:
                supoja3_score += 1
        elif prob_num % 10 == 2 or prob_num % 10 == 3:
            if answers[prob_num] == 1:
                supoja3_score += 1
        elif prob_num % 10 == 4 or prob_num % 10 == 5:
            if answers[prob_num] == 2:
                supoja3_score += 1
        elif prob_num % 10 == 6 or prob_num % 10 == 7:
            if answers[prob_num] == 4:
                supoja3_score += 1
        elif prob_num % 10 == 8 or prob_num % 10 == 9:
            if answers[prob_num] == 5:
                supoja3_score += 1

    # get answer
    answer = [1, 2, 3]
    if supoja1_score < supoja2_score or supoja1_score < supoja3_score:
        answer.remove(1)
    if supoja2_score < supoja1_score or supoja2_score < supoja3_score:
        answer.remove(2)
    if supoja3_score < supoja1_score or supoja3_score < supoja2_score:
        answer.remove(3)

    return answer
```