winner_score = 0
winner = 1
for player in range(1, 6):
    player_score = sum(map(int, input().split()))
    if player_score > winner_score:
        winner = player
        winner_score = player_score                 
    
print(winner, winner_score)