import random

carcount = 0
zonkcount = 0
iterations = 100000

for i in range(iterations):
    choices = ["Zonk", "Zonk", "Zonk"]
    #         ["Zonk", "Zonk", "Car"]
    choices[random.randint(0, 2)] = "Car"
    
    choice = choices[0] #first choice
    
    if choices[1] == "Zonk":
        choices.pop(1)
    elif choices[2] == "Zonk":
        choices.pop(2)
    
    choice = choices[1] #changed choice

    if choice == "Car":
        carcount += 1
    else:
        zonkcount += 1

print(f"Car:  {carcount} = {round(carcount/iterations*100, 1)}%") #probability of success if changed
print(f"Zonk: {zonkcount} = {round(zonkcount/iterations*100, 1)}%") #probability of success if not changed
