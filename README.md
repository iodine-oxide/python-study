# python-study(백준)

# 사용 기법 및 알고리즘 정리 [(문제집)](https://www.acmicpc.net/workbook/view/8708)

## [5073번, B3](https://www.acmicpc.net/problem/5073)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/5073.py)
- 이차원 list를 생성후 삼각형의 기본 원리 조건
- list를 set으로 변환하여 중복되지 않는 수들의 개수를 판별
- 개수를 기반으로 삼각형 유형 판단

## [23971번, B3](https://www.acmicpc.net/problem/23971)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/23971.py)
- 문제의 예시를 통하여 보았을 때 단순 X, Y좌표 상의 거리만 충족되면 됨
- 한줄의 가장 끝에 한명이 앉는 것이 최대 효율(행과 열 모두 가장 많이 앉을 수 있음)
- 대각선 길이의 고려가 없으므로 단순히 (한 행에 앉을 수 있는 사람수) X (한 열에 안을 수 있는 사람수)가 최대
- 따라서 W를 M+1, H를 N+1로 나누어 나머지에 따라 몫에 1을 더하거나 몫을 유지한 뒤 곱하면 최대 인원이 생성

## [2292번, B2](https://www.acmicpc.net/problem/2292)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/2292.py)
- 고등 수2 단골문제.. 방이 1, 1+6, 1+6+12, ...으로 커지는 것을 이용
- 방의 개수가 주어진 수를 처음 넘기는 단계의 수를 찾기
- 해당 단계의 모든 방으로 가는 최단 거리는 해당 단계의 수와 같음

## [1157번, B1](https://www.acmicpc.net/problem/1157)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/1157.py)
- 받은 문자를 list(문자)를 통해 알파벳 리스트로 변환
- dictionary에서 원래 오류 발생용도로 쓰이는 try:, exception:을 이용하여 중복되는 알파벳의 개수를 딕셔너리에 알파벳:개수로 저장(이 과정에서 .upper()을 이용하여 대문자로)
- dictionary에서 list(dictionary.keys())와 list(dictionary.values())를 이용하여 각각 알파벳과 나온 횟수를 list로 추출
- value list를 sort하여 값이 2개 이상인 경우 ?처리 해당 조건문에서 값이 1개일 때를 고려하여 조건 생성
- value list(sort 적용X)의 max값의 index를 list.index를 통해 도출, key list의 해당 인덱스 값을 반환

## [11723번, S5](https://www.acmicpc.net/problem/11723)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/11723.py)
- 기본적인 set에 대한 이해
- remove 명령에 대해 remove를 사용하면 set에 해당 인자가 없으면 오류가 발생하므로 discard 사용
- switch문을 구현하기위하여 dictionary를 사용하고자 하였으나, 오히려 dictionary로 구현 시 함수 호출로 인하여 실행시간이 초과됨
- 여러 인자를 추가할 경우 update()이용

## [9655번, S5](https://www.acmicpc.net/problem/9655)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/9655.py)
- 수학적 알고리즘만 구성하면 매우 쉬움
- 3 부터 시작한다고 할 때 처음 시작시 1개 혹은 3개만 가져감으로 게임의 결과는 돌이 한개 적거나 3개 적은 게임의 결과와 반대임
- 따라서 결국 홀수개의 돌일때는 상근이가, 짝수개의 돌일떄는 창영이가 이김

## [10431번, S5](https://www.acmicpc.net/problem/10431)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/10431.py)
- 맨 처음 입력받는 문자열들을 2차원 list(fn_list)로 정의, 각 실행의 횟수를 저장할 dictionary 생성
- 해당 lsit들을 하나씩 가져와 맨 앞의 숫자는 key로 다른 하나는 정리된 줄을 만드는 list(line)에 삽입
- 입력받은 순서대로 줄을 만드는 list(line)에 삽입함과 동시에 list를 순차적으로 순회하면서 해당 숫자가 삽입될 위치를 확인
- 확인과정에서 위치에 변동이 있으면 loc(기본값 0)으로 정의된 위치 변수의 값 변환, 없으면 break
- 변경된 loc값에 값을 집어넣고 움직인 횟수 변수(move)에 loc값 더하기

## [8979번, S5](https://www.acmicpc.net/problem/8979)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/8979.py)
- 입력받은 수들에 대해서 금메달 수 부터 비교하며 조건에 안맞으면 continue
- remove로 실행시간 줄이려 하였으나 그러면 동일 대상에 대한 순위 반영 안됨

## [7568번, S5](https://www.acmicpc.net/problem/7568)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/7568.py)
- 사람의 무게와 키, 등수는 기본을 1로 하여 정보를 가지는 이차원 배열생성
- 이차원 배열을 순회하며 자신보다 큰 사람이 있으면 등수에 1을 더함
- ps.딕셔너리의 경우 같은 정보를 가지는 경우 몸무게와 키가 같으면 정보가 무시됨.. 딕셔너리에 매몰되지 말자...

## [4659번, S5](https://www.acmicpc.net/problem/4659)[(코드)](https://github.com/iodine-oxide/python-study/blob/main/study_code_files/4659.py)
- 비밀번호를 받아 예외처리 조건들을 앞에 두고 이후에는 허용되지 않는 비밀번호를 조건을 두어 불만족시 조건을 확인하는 루프문을 이탈
