def calculate_coins(sum):
    coins = {1 : 0,
             2 : 0,
             5 : 0,
            10 : 0,
            20 : 0,
            50 : 0,
           100 : 0 }
    while sum >= 1:
        sum -= 1
        coins[100]+=1
    if sum >= 0.50:
        sum -= 0.50
        coins[50]+=1
    while sum >= 0.20:
        sum -= 0.20
        coins[20]+=1
    if sum >= 0.10:
        sum -= 0.1
        coins[10]+=1
    if sum >= 0.05:
        sum -= 0.05
        coins[5]+=1
    while sum >= 0.02:
        sum -= 0.02
        coins[2]+=1
    if sum >= 0.01:
        sum -= 0.01
        coins[1]+=1
    return coins