def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads)//2
    chickens = numheads - rabbits
    return chickens, rabbits

numheads = 35
numlegs = 94

chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")