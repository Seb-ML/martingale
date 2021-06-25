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
print("highest total bet:", np.max(total_bet))


#The martingale strategy is one in which the better bets on either red or black and doubles their bet each time until they win,
#then repeats again starting from their minimum bet again. Thus theoretically their profit will be equal to their minimum bet after each win.

#This code simulates this to find out the maximum single bet needed to sustain this strategy in reality.
#The idea being, after a certain number of rounds, probabilistically there will come a point where the maximum bet exceeds the better's available cash,
#resulting in a huge loss.
        




