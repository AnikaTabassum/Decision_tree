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
        print(listt)
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

        entropy=self.calculateEntropy(root)
        print("en "+str(entropy))
        return root,entropy
    def calculateEntropy(self,root):
        #sentro = -cn1 * math.log2(cn1 / cnt) - cn2 * math.log2(cn2 / cnt) - cn3 * math.log2(cn3 / cnt)

        entro=0.0
        i=1
        while i<=root.__len__():
            #print(value/play.__len__()
            print(root.get(i))
            if root.get(i)!=0:
                value=root.get(i)
            i+=1
            entro-=(value/play.__len__())*math.log2(value/play.__len__())

        print(entro)
        return entro

    def Split(self):
        print("sfas")
        #calculateRootEntropy=self.Count(playSet,play)
        #print(calculateRoot)
        #calculateOutEntropy=self.rootCalc(outSet,out)

    def divideRoot(self):

        diction={}

        i=0
        indx=0
        for value in outSet:
            leftData = list()
            rightData = list()
            left = list()
            right = list()
            print("i")
            print(i)
            j=0
            print(value)
            while j<out.__len__():
                if out[j]<value:
                    leftData.append(data[j])
                    left.append(out[j])

                    #ekhan theke class ber kore entropy ber korar function ke call korbo
                    #entropy paile right tar o ber kore average kore information gain ber korbo
                    #jodi ei info gain ager cheye beshi hoi tahole ei pura data list ta ke max e dhukai rakhbo
                    #sathe kar jonno hoitese setao ber kore rakhbo
                else:
                    rightData.append(data[j])
                    right.append(out[j])
                j+=1
            leftDict,leftEntropy=self.Count(playSet, left)
            RightDict,rightEntropy=self.Count(playSet, right)
            #print(leftDict)
            avg=(leftEntropy+rightEntropy)/2
            print(avg)
            #self.Count(playSet, right)
            #print(right.__len__())
            i+=1
            #print(left.__len__())


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
mainEntropy=Decision().Count(playSet,play)
Decision().divideRoot()