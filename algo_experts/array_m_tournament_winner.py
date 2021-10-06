
def tournamentWinner(competitions, results):
    # Write your code here.
    win = {}
    for i in range(len(competitions)):
        if results[i] == 1:
            if competitions[i][0] not in win:
                win[competitions[i][0]] = 3
            else:
                win[competitions[i][0]] += 3
            
        elif results[i] == 0:
            if competitions[i][1] not in win:
                win[competitions[i][1]] = 3
            else:
                win[competitions[i][1]] += 3
            
        
        
    return max(win.keys(), key=(lambda k: win[k]))


c = [
  ["HTML", "C"],
  ["C", "Python"],
  ["Python", "HTML"]
]

r = [1, 1, 0]

print(tournamentWinner(c, r))