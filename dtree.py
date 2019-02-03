import math

class Decision:
    def __init__(self):
        "do "

    def makeFile(self):
        cnt=0
        cntComma=0
        cn1 = 0
        cn2 = 0
        cn3 = 0
        line=list()
        with open("iris.txt", 'r') as f:
            for txt in f:
                i=0
                cntComma=0
                for i in txt:
                    if i==',':
                        cntComma+=1

                x = txt.split(",")

                if x[cntComma]=="Iris-setosa\n":
                    x[cntComma]=1
                    cn1+=1
                elif x[cntComma]=="Iris-versicolor\n":
                    x[cntComma]=2
                    cn2+=1
                elif x[cntComma]=="Iris-virginica\n" or  x[cntComma]=="Iris-virginica" :
                    x[cntComma]=3
                    cn3+=1
                line.append(x)
                #mylist = list(set(line))


                strig=str(x[0])+","+str(x[1])+","+str(x[2])+","+str(x[3])+","+str(x[4])+"\n"
                classSet.add(x[4])
                with open ("IRISFinal.txt",'a') as file:
                    file.write(strig)
                # print(txt)

                dataSet.insert(cnt, x)
                cnt = cnt + 1

        print(classSet)
        self.entropy(cn1,cn2,cn3,cnt)
    def entropy(self,cn1,cn2,cn3,cnt):
        print(cn1)
        entro=-cn1*math.log2(cn1/cnt)-cn2*math.log2(cn2/cnt)-cn3*math.log2(cn3/cnt)
        print(entro)

dataSet = list()
classSet=set()
Decision().makeFile()
#Decision().entropy()