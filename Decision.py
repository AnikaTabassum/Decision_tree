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
                play.append(int(x[4]))
                playSet.add(int(x[4]))
        #print(out[2])

    def rootCalc(self):
        root=[0 for k in range(3)]
        for value in playSet:
            i=0
            cnt = 0

            while i<play.__len__():
                if value==play[i]:
                    cnt+=1
                i+=1
            print(cnt)
            print(int(value))
            root[int(value)-1]=cnt

        print(root)
        self.calculateEntropy(root)
    def calculateEntropy(self, root):
        #sentro = -cn1 * math.log2(cn1 / cnt) - cn2 * math.log2(cn2 / cnt) - cn3 * math.log2(cn3 / cnt)

        entro=0.0
        for value in root:
            print(value/play.__len__())
            entro-=(value/play.__len__())*math.log2(value/play.__len__())

        print(entro)


out = list()
outSet = set()
hum = list()
humSet = set()
temp = list()
tempSet = set()
wind = list()
windSet = set()
play = list()
playSet = set()
Decision().calculateRootEntropy()
Decision().rootCalc()