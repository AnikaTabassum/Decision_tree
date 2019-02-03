import math

class Decision:
    def __init__(self):
        "do "

    def calculateRootEntropy(self):
        with open("IRISFinal.txt", 'r') as f:
            for txt in f:
                x = txt.split(",")
                out.append(x[0])
                outSet.add(x[0])
                hum.append(x[1])
                humSet.add(x[1])
                temp.append(x[2])
                tempSet.add(x[2])
                wind.append(x[3])
                windSet.add(x[3])
                play.append(x[4])
                playSet.add(x[4])
        print(out)

    def rootCalc(self):
        


out=list()
outSet=set()
hum=list()
humSet=set()
temp=list()
tempSet=set()
wind=list()
windSet=set()
play=list()
playSet=set()
Decision().calculateRootEntropy()
