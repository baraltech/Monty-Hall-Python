import random

carcount = 0
zonkcount = 0
iterations = 100000

for i in range(iterations):
    choices = ["Zonk", "Zonk", "Zonk"]
    #         ["Zonk", "Zonk", "Car"]
    choices[random.randint(0, 2)] = "Car"
    choice = 0
    if choices[1] == "Zonk":
        choices.pop(1)
    elif choices[2] == "Zonk":
        choices.pop(2)
    
    choice = choices[1]

    if choice == "Car":
        carcount += 1
    else:
        zonkcount += 1

print(f"Car:  {carcount} = {round(carcount/iterations*100, 1)}%")
print(f"Zonk: {zonkcount} = {round(zonkcount/iterations*100, 1)}%")
