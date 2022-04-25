# [Programmers] 키패드 누르기

:writing_hand: [h0meb0dy](mailto:h0meb0dysj@gmail.com)

> https://programmers.co.kr/learn/courses/30/lessons/67256

## 문제 설명

스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

![image](https://user-images.githubusercontent.com/104156058/165016292-0661483c-ee2e-4da1-b172-9f9493beb055.png)

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 `*` 키패드에 오른손 엄지손가락은 `#` 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 `1`, `4`, `7`을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 `3`, `6`, `9`를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 `2`, `5`, `8`, `0`을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
   4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

## 제한사항

- numbers 배열의 크기는 1 이상 1,000 이하입니다.
- numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
- hand는 `"left"` 또는 `"right"`입니다.
  - `"left"`는 왼손잡이, `"right"`는 오른손잡이를 의미합니다.
- 왼손 엄지손가락을 사용한 경우는 `L`, 오른손 엄지손가락을 사용한 경우는 `R`을 순서대로 이어붙여 문자열 형태로 return 해주세요.

## 입출력 예

| numbers                           | hand      | result          |
| --------------------------------- | --------- | --------------- |
| [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] | `"right"` | `"LRLLLRLLRRL"` |
| [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2] | `"left"`  | `"LRLLRRLLLRR"` |
| [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]    | `"right"` | `"LLRLLRLLRL"`  |

## 입출력 예에 대한 설명

**입출력 예 #1**

순서대로 눌러야 할 번호가 [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]이고, 오른손잡이입니다.

| 왼손 위치 | 오른손 위치 | 눌러야 할 숫자 | 사용한 손 | 설명                                                         |
| --------- | ----------- | -------------- | --------- | ------------------------------------------------------------ |
| *         | #           | 1              | L         | 1은 왼손으로 누릅니다.                                       |
| 1         | #           | 3              | R         | 3은 오른손으로 누릅니다.                                     |
| 1         | 3           | 4              | L         | 4는 왼손으로 누릅니다.                                       |
| 4         | 3           | 5              | L         | 왼손 거리는 1, 오른손 거리는 2이므로 왼손으로 5를 누릅니다.  |
| 5         | 3           | 8              | L         | 왼손 거리는 1, 오른손 거리는 3이므로 왼손으로 8을 누릅니다.  |
| 8         | 3           | 2              | R         | 왼손 거리는 2, 오른손 거리는 1이므로 오른손으로 2를 누릅니다. |
| 8         | 2           | 1              | L         | 1은 왼손으로 누릅니다.                                       |
| 1         | 2           | 4              | L         | 4는 왼손으로 누릅니다.                                       |
| 4         | 2           | 5              | R         | 왼손 거리와 오른손 거리가 1로 같으므로, 오른손으로 5를 누릅니다. |
| 4         | 5           | 9              | R         | 9는 오른손으로 누릅니다.                                     |
| 4         | 9           | 5              | L         | 왼손 거리는 1, 오른손 거리는 2이므로 왼손으로 5를 누릅니다.  |
| 5         | 9           | -              | -         |                                                              |

따라서 `"LRLLLRLLRRL"`를 return 합니다.

**입출력 예 #2**

왼손잡이가 [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]를 순서대로 누르면 사용한 손은 `"LRLLRRLLLRR"`이 됩니다.

**입출력 예 #3**

오른손잡이가 [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]를 순서대로 누르면 사용한 손은 `"LLRLLRLLRL"`이 됩니다.

## Solve

### Idea

키패드의 각 버튼들을 좌표로 표현해서 거리를 간단하게 계산할 수 있도록 한다.

손의 위치와 눌러야 할 버튼 사이의 거리만 계산하면 왼손으로 눌러야 할지 오른손으로 눌러야 할지 쉽게 결정할 수 있다.

### Code

```python
# calculate distance between key1 and key2
def distance(key1, key2):
    return abs(key2[0] - key1[0]) + abs(key2[1] - key1[1])

def solution(numbers, hand):
    position = {'*': (0, 0), '0': (1, 0), '#': (2, 0), '7': (0, 1), '8': (1, 1), '9': (2, 1), '4': (0, 2), '5': (1, 2), '6': (2, 2), '1': (0, 3), '2': (1, 3), '3': (2, 3)} # {key: coordinate}

    l_position = position['*'] # initial position of left hand
    r_position = position['#'] # initial position of right hand

    answer = ''

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L' # 1, 4, 7 -> left hand
            l_position = position[str(number)]
            continue
        elif number == 3 or number == 6 or number == 9:
            answer += 'R' # 3, 6, 9 -> right hand
            r_position = position[str(number)]
            continue

        l_distance = distance(l_position, position[str(number)]) # distance between left hand and key to tab
        r_distance = distance(r_position, position[str(number)]) # distance between right hadn and key to tab

        if l_distance < r_distance:
            answer += 'L'
            l_position = position[str(number)]
            continue
        elif l_distance > r_distance:
            answer += 'R'
            r_position = position[str(number)]
            continue

        if hand == 'left':
            answer += 'L'
            l_position = position[str(number)]
        else:
            answer += 'R'
            r_position = position[str(number)]
    
    return answer
```