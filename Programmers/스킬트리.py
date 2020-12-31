def solution(skill, skill_trees):
    answer = 0
    for i in range(0, len(skill_trees)):
        prev_skill = list(skill)
        skill_str = ""
        for j in range(0, len(skill_trees[i])):
            if len(prev_skill) > 0:
                if skill_trees[i][j] in prev_skill:
                    skill_str += skill_trees[i][j]

        if skill.startswith(skill_str):
            answer += 1

    return answer