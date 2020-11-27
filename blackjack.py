import random

p_cards=[]
d_cards=[]

# Dealer-Cards
while len(d_cards) < 2:
    d_cards.append(random.randint(1, 11))

# Player-Cards
while len(p_cards) < 2:
    p_cards.append(random.randint(1, 11))

if sum(d_cards) > 21:
    print("Dealer BUSTED, You Win!")
elif sum(p_cards) > 21:
    print("You BUSTED, Dealer Win!")
else:
    
