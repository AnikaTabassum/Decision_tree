import math

class Decision:
    def __init__(self):
        "do "

    def calculateRootEntropy(self):
        with open("IRISFinal.txt", 'r') as f:
            for txt in f:
                x = txt.split(",")
                data.append(x)
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
        #print(data)

    def Count(self,sett,listt):
        #root=[0 for k in range(3)]
        #print(listt.__len__())
        root = {}
        for value in sett:
            i=0
            cnt = 0

            while i<listt.__len__():
                if value==play[i]:
                    cnt+=1

                root[value] = cnt
                i += 1
            #print(cnt)
            #print(int(value))
            #root[int(value)-1]=cnt

        print(root)

        self.calculateEntropy(root)
        return root
    def calculateEntropy(self,root):
        #sentro = -cn1 * math.log2(cn1 / cnt) - cn2 * math.log2(cn2 / cnt) - cn3 * math.log2(cn3 / cnt)

        entro=0.0
        i=1
        while i<=root.__len__():
            #print(value/play.__len__()
            print(root.get(i))
            value=root.get(i)
            i+=1
            entro-=(value/play.__len__())*math.log2(value/play.__len__())

        print(entro)

    def Split(self):
        calculateRootEntropy=self.Count(playSet,play)
        #print(calculateRoot)
        #calculateOutEntropy=self.rootCalc(outSet,out)

    def divideRoot(self):
        left=list()
        right=list()

        for value in outSet:
            i=0
            while i < out.__len__():
                if value<out[i]:
                    left.append(data[i])
                else:
                    right.append(data[i])
                i+=1

        print(left)
        print(right)


data=list()
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
#Decision().rootCalc()
Decision().Split()
Decision().divideRoot()