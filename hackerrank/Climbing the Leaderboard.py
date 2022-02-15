#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    start_val = len(ranked)-1
    
    answer = []
    for i in range(0, len(player)):
        flag = True
        for j in range(start_val, -1, -1):
            if ranked[j] > player[i]:
                flag = False
                start_val = j
                answer.append(j+2)
                break
            elif ranked[j] == player[i]:
                flag = False
                start_val = j
                answer.append(j+1)
                break
        
        if flag:
            answer.append(1)
            # print(1)
                
    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
