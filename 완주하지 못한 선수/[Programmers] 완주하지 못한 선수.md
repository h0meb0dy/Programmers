# [Programmers] 완주하지 못한 선수

:writing_hand: [h0meb0dy](mailto:h0meb0dysj@gmail.com)

> https://programmers.co.kr/learn/courses/30/lessons/42576

## 문제 설명

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

## 제한사항

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

## 입출력 예

| participant                                       | completion                               | return   |
| ------------------------------------------------- | ---------------------------------------- | -------- |
| ["leo", "kiki", "eden"]                           | ["eden", "kiki"]                         | "leo"    |
| ["marina", "josipa", "nikola", "vinko", "filipa"] | ["josipa", "filipa", "marina", "nikola"] | "vinko"  |
| ["mislav", "stanko", "mislav", "ana"]             | ["stanko", "ana", "mislav"]              | "mislav" |

## 입출력 예 설명

예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

[출처](http://hsin.hr/coci/archive/2014_2015/contest2_tasks.pdf)

## Solve

### Idea

`completion`에서 반복문을 돌리면서 `participant`와 일일이 비교하는 무식한 방법을 쓰면 효율성 테스트를 통과할 수 없다.

`participant`와 `completion`에서 각각 모든 선수의 해시 값을 더한 후 두 값의 차이를 구하면, 그 값이 해시인 선수가 완주하지 못했다는 결론을 낼 수 있다.

### Code

```python
def solution(participant, completion):
    participant_dict = {hash(participant[idx]): participant[idx] for idx in range(len(participant))} # {hash: participant}

    participant_sum = 0
    for athlete in participant:
        participant_sum += hash(athlete) # sum of hashes of all participants

    completion_sum = 0
    for athlete in completion:
        completion_sum += hash(athlete) # sum of hashes of participants who completed race

    difference = participant_sum - completion_sum # hash of participant who didn't complete race

    return participant_dict[difference]
```