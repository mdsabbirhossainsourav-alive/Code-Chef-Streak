def max_streak(problems):
    streak = max_streak = 0
    for p in problems:
        if p > 0:
            streak += 1
            if streak > max_streak:
                max_streak = streak
        else:
            streak = 0
    return max_streak

t = int(input())

for _ in range(t):
    n = int(input())
    Om = list(map(int, input().split()))
    Addy = list(map(int, input().split()))
    
    om_streak = max_streak(Om)
    addy_streak = max_streak(Addy)
    
    if om_streak > addy_streak:
        print("Om")
    elif addy_streak > om_streak:
        print("Addy")
    else:
        print("Draw")
