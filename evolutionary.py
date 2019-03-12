from neuralnetwork import NeuralNetwork
import random
import math
networks = []
for i in range(10):
    networks.append(NeuralNetwork([2, 4, 3, 3], -1, 1, -1, 1))

yeet = None

losse = []

amount = 25


class West:
    def __init__(self, network):
        self.network = network
        self.ammo = 0

    def run(self, enemyAmmo):
        result = self.network.run([self.ammo, enemyAmmo])
        highestIndex = -1
        highestVal = 0
        for index in range(len(result)):
            output = result[index]
            if highestIndex < 0:
                highestVal = output
                highestIndex = index
            elif output > highestVal:
                highestVal = output
                highestIndex = index
        if highestIndex is 0 and self.ammo is 0:
            return -1
        return highestIndex


def play(net1, net2):
    ww1 = West(net1)
    ww2 = West(net2)

    # 0 = shoot, 1 = reload, 2 = block
    for _ in range(25):
        move1 = ww1.run(ww2.ammo)
        move2 = ww2.run(ww1.ammo)
        if move1 is 0 and move2 is 1:
            return 1
        elif move1 is 1 and move2 is 0:
            return -1
        if move1 is 1:
            ww1.ammo += 1
        elif move1 is 0:
            ww1.ammo -= 1
        if move2 is 1:
            ww2.ammo += 1
        elif move2 is 0:
            ww2.ammo -= 1
    return 0


def playRand(net1, randMoves):
    ww1 = West(net1)
    randAmmo = 0
   # print("new match")
    for i in range(25):
        move1 = ww1.run(randAmmo)
        if move1 is -1:
            return -1
        move2 = randMoves[i]

       # print("aimove:", move1, " aiammo", ww1.ammo,
        #      " randmove", move2, " randammo", randAmmo)
        if move1 is 0 and move2 is 1:
            return 1
        elif move1 is 1 and move2 is 0:
            return -1
        if move1 is 1:
            ww1.ammo += 1
        elif move1 is 0:
            ww1.ammo -= 1
        if move2 is 1:
            randAmmo += 1
        elif move2 is 0:
            randAmmo -= 1
    return 0


def generateRand():
    moves = []
    ammo = 0
    for i in range(25):
        if ammo > 0:
            move = random.randint(0, 2)
        else:
            move = random.randint(1, 2)
        if move is 1:
            ammo += 1
        moves.append(move)

    return moves


def playPlayer(net):
    ww1 = West(net)
    yourAmmo = 0

    # 0 = shoot, 1 = reload, 2 = block
    while True:
        move1 = ww1.run(yourAmmo)
        move2 = int(input("Your move: "))
        print("aimove:", move1, " aiammo", ww1.ammo,
              " yourmove", move2, " yourammo", yourAmmo)
        if move1 is 0 and move2 is 1:
            return 1
        elif move1 is 1 and move2 is 0:
            return -1
        if move1 is 1:
            ww1.ammo += 1
        elif move1 is 0:
            ww1.ammo -= 1
        if move2 is 1:
            yourAmmo += 1
        elif move2 is 0:
            yourAmmo -= 1
    return 0


matches = []
for _ in range(amount):
    matches.append(generateRand())


for runs in range(10000):
    losses = []

    # for network in networks:
    # losses.append({"loss": 0, "network": network})
    for index1 in range(len(networks)):
        network1 = networks[index1]
        lossNum = 0
        for i in range(amount):
            result = playRand(network1, matches[i])
            if result is not 1:
                lossNum += 1
           # else:
            #    lossNum += 1
        losses.append({"loss": lossNum, "network": network1})
    bestNets = []
    for loss in losses:
        if len(bestNets) < 3:
            bestNets.append(loss)
        else:
            smallestIndex = -1
            biggestLoss = 0

            for index in range(len(bestNets)):
                best = bestNets[index]
                if loss["loss"] < best["loss"] and best["loss"] > biggestLoss:
                    smallestIndex = index
                    biggestLoss = best["loss"]
            if smallestIndex != -1:
                bestNets[smallestIndex] = loss

    if runs % 25 == 0:
        for best in bestNets:
            print(str(amount - best["loss"]) + f"/{amount} wins")
        print(runs, "\n")

    losse.append(bestNets[0]["loss"])

    yeet = bestNets[0]["network"]

    if bestNets[0]["loss"] is 0:
        break
    networks = []
    for best in bestNets:
        networks.append(best["network"].mutate(0.05, 0.5))
    while len(networks) < 10:
        net = random.randint(0, 2)
        networks.append(bestNets[net]
                        ["network"].duplicate().mutate(0.2, 5))


yeet.printData()
while True:
    print(playPlayer(yeet))
# console.log(network.run([0.1, 0.4]));
# console.log(network.run([0.4, 0.6]));
