def common_prefix(s, t):
    cp = 0
    l = min(len(s), len(t))
    for i in range(l):
        if s[i] != t[i]:
            break
        cp += 1
    return cp

import sys
input = sys.stdin.readline

n = int(input())
original = []   # 원래 입력 순서대로 저장
words = []      # (단어, 원래 인덱스) 형태로 저장
for i in range(n):
    word = input().strip()
    original.append(word)
    words.append((word, i))
    
# 사전순 정렬 (문자열 기준)
sorted_words = sorted(words, key=lambda x: x[0])

# 1. 인접한 단어들만 비교하여 최대 공통 접두사 길이 L 찾기
max_cp = -1
for i in range(len(sorted_words) - 1):
    w1, _ = sorted_words[i]
    w2, _ = sorted_words[i+1]
    cp = common_prefix(w1, w2)
    if cp > max_cp:
        max_cp = cp

# 만약 최대 공통 접두사 길이가 0이면, 입력 순서상 가장 앞의 두 단어를 출력
if max_cp == 0:
    print(original[0])
    print(original[1])
    exit(0)

# 2. 각 단어(길이가 max_cp 이상)에서 접두사 max_cp글자를 key로 그룹화
groups = {}
for i, word in enumerate(original):
    if len(word) < max_cp:
        continue
    key = word[:max_cp]
    if key not in groups:
        groups[key] = []
    groups[key].append(i)

# 후보 쌍 중, 입력 순서 기준으로 (S, T) (S: 더 작은 인덱스, T: 그 다음) 가 가장 빠른 쌍 선택
best_pair = (10**9, 10**9)  # 매우 큰 초기값
for key, indices in groups.items():
    if len(indices) < 2:
        continue
    indices.sort()  # 원래 입력 순서대로 정렬
    candidate = (indices[0], indices[1])
    # 여러 그룹이 있을 수 있으므로, (S, T) 튜플이 사전순으로 가장 작은 쌍 선택
    if candidate < best_pair:
        best_pair = candidate

S_index, T_index = best_pair
print(original[S_index])
print(original[T_index])