total_mana = int(input("How much Mana can you produce in total?"))
tef_cost = int(input("How much does Teferi cost, including Tax?"))
veil_cost = int(input("How much does it cost to get Chain Veil onto the battlefield?"))
c = int(input("Maximum amount of Mana from 4 permanents?"))
d = int(input("Maximum amount of Mana from 3 permanents?"))
upper_bound = int(input("How much Mana do you want to go for?"))

x = 0   #Total amount of Mana gained
y = 5   #Teferi's starting loyalty

if (tef_cost + veil_cost <= total_mana):
    i = 5   #i will refer to Teferi's loyalty at any given point
    j = 0   #j will refer to the total amount of Chain Veil activations
elif (tef_cost + veil_cost > total_mana and total_mana >= tef_cost):
    i = 4
    j = 1
else:
    i = 0
    j = 0
    print("You can't cast Teferi, mate.")   #sadlife


while i > 1:
    i -= 1
    x += d - 4
    j += 1

i -= 1
x += c  #The last activation before Teferi dies is a bit different because you don't need to activate Chain Veil again.

if (x < tef_cost + 2):
    print("You can't go infinite.")
else:
    while x < upper_bound:
        tef_cost += 2
        i = y + j
        x -= tef_cost
        while i > 1:
            i -= 1
            x += d - 4
            j += 1
        i -= 1
        x += c
    print("You can do it! You made", x, "Mana by activating Chain Veil", j, "times.")