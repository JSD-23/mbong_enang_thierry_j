def maxProfit(prix):
    profit = []
    for p in prix:
        for q in prix[prix.index(p)+1:]:
            profit.append(q-p)
    bon_profit = []
    for p in profit:
        if p > 0:
            bon_profit.append(p)
    if len(bon_profit) == 0:
        return 0
    
    return max(bon_profit)

#prix = [7,1,5,3,6,4]
#prix1 = [7,6,5,4,3,1]

#print(maxProfit(prix), maxProfit(prix1), sep=" ")