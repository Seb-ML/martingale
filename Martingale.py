import numpy as np

PROB_OF_WIN = 17/38
MIN_BET = 5
ROUNDS = 250
PROFITS = []
total_bet = []
highest_bet = []

def spin():
    return np.random.rand() < PROB_OF_WIN #returns 1 or 0

def round():
    global bet
    bet = [MIN_BET]
    stop_signal = 0
    while stop_signal == 0:
        if spin() == 0:
            bet.append(bet[-1]*2)
        if spin() == 1:
            stop_signal = 1
            PROFITS.append(bet[-1]*2 - np.sum(bet))
    #print("bets:", bet)

for i in range(ROUNDS):
    round()
    total_bet.append(np.sum(bet))
    highest_bet.append(bet[-1])


print("")
#print("profits:", PROFITS,"\n")
print("total profit:", np.sum(PROFITS))
print("highest single bet:", np.max(highest_bet))
print("highest total bet:", np.max(total_bet))


        




