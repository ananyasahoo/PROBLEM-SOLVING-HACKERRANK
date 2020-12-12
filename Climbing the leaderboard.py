def climbingLeaderboard(scores, Alice):
     scores = sorted(list(set(scores)))
     index = 0
     rank_list = []
     n = len(scores)
     for i in Alice:
         while (n > index and i >= scores[index]):
             index += 1
         rank_list.append(n+1-index) 
     return rank_list
    
   

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
