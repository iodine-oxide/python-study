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
- 딕셔너리에서 원래 오류 발생용도로 쓰이는 try:, exception:을 이용하여 중복되는 알파벳의 개수를 딕셔너리에 알파벳:개수로 저장(이 과정에서 .upper()을 이용하여 대문자로)
- 딕셔너리에서 list(dictionary.keys())와 list(dictionary.values())를 이용하여 각각 알파벳과 나온 횟수를 list로 추출
- value list를 sort하여 값이 2개 이상인 경우 ?처리 해당 조건문에서 값이 1개일 때를 고려하여 조건 생성
- value list(sort 적용X)의 max값의 index를 list.index를 통해 도출, key list의 해당 인덱스 값을 반환
