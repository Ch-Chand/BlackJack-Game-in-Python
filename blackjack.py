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

while True:
    if sum(p_cards) > 21:
        print("You BUSTED, Dealer Win!")
    elif sum(p_cards) > sum(d_cards):
        print("Your card's sum   : " + str(sum(p_cards)))
        print("Dealer card's sum : " + str(sum(d_cards)))
        print("You Win!")
        break
    else:
        choice=str(input("Enter hit or stay :"))
        if choice=="hit":
            p_cards.append(random.randint(1,11))
        else:
            pass




