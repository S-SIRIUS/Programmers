def checkSkills(skill, skill_tree):
    for i in range (0, len(skill)):
        present = skill_tree.find(skill[i])
        if present == -1:
            present = 999
        if i==0:
            before = present
        else:
            if present >= before:
                before = present
                continue
            else:
                return 0            
    return 1
            

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += checkSkills(skill, skill_tree)

    return answer