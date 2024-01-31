import random

def randModelYear():
    return random.randrange(1990, 2025)

carList = ["toyota", "nissan", "honda", "ford", "mazda", "suzuki"]

print(random.choice(carList))
print(randModelYear())
