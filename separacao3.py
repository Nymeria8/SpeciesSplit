#Calculates the X value based on two outputs of mediascore2.py
#Outputs 3  files: 2 with the certainly classified and one non classified
#organized with: gene-X value

import argparse

parser = argparse.ArgumentParser(description="X calculation")

parser.add_argument("-in1",dest="orgmed",required=True,help="Provide the the mean file of specie1")

parser.add_argument("-in2",dest="fungmed",required=True,help="Provide the the mean file of specie2")

parser.add_argument("-out1",dest="outputnameplant",required=True,help="Provide the destination file for the classified as specie1")

parser.add_argument("-out2",dest="outputnamefungus",required=True,help="Provide the destination file for the classified as specie2")

parser.add_argument("-outincert",dest="outputnameunknown",required=True,help="Provide the destination file for the non classified")

arg = parser.parse_args()

orgmed = open (args.orgmed)

fungmed= open (args.fungmed)

saidafungo = open (args.outputnamefungus, "w")

saidaplanta= open (args. outputnameplant, "w")

incertos= open (args.outputnameunknown, "w")


array1=[]
array2=[]
arrayscore=[]
arrayscore2=[]


for i in orgmed:
    j=i.split("\t")
    array1.append(j[0])
    arrayscore.append(j[1])

for i in fungmed:
    x=i.split("\t")
    array2.append(x[0])
    arrayscore2.append(x[1])


s=0
for d in array1:
    u=0
    for e in array2:
            if (d==e):
                o= (float(arrayscore[s]))-(float(arrayscore2[u]))
                if (o>=100):
                    saidaplanta.write(d)
                    saidaplanta.write("\t")
                    saidaplanta.write(str (o))
                    saidaplanta.write("\n")
                if (o<=-100):
                    saidafungo.write(d)
                    saidafungo.write("\t")
                    saidafungo.write(str (o))
                    saidafungo.write("\n")
                if(-100<o<100):
                    incertos.write(d)
                    incertos.write("\t")
                    incertos.write(str (o))
                    incertos.write("\n")
            u+=1
    s+=1



orgmed.close()
fungmed.close()
saidafungo.close()
saidaplanta.close()
incertos.close()
