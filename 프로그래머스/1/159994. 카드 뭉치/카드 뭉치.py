from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    goal = deque(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    while goal:
        standard = goal.popleft()
        if cards1 and cards1[0] == standard:
            cards1.popleft()
        elif cards2 and cards2[0]==standard:
            cards2.popleft()
        else:
            answer='No'
            break
    return answer