#calculates the mean score of two output of the blastaaa1.py (against the same organism)
#output: transcript        media score


import argparse

parser = argparse.ArgumentParser(description="Do mean score")

parser.add_argument("-in1",dest="outputdoblast1",required=True,help="Provide the blast output")

parser.add_argument("-in2",dest="outputdoblast2",required=True,help="Provide the blast output2")

parser.add_argument("-out",dest="outputname",required=True,help="Provide the destination flie")

arg = parser.parse_args()


orgn= open (arg.outputdoblast1)

orgx= open (arg.outputdoblast2)

orgmed= open (arg.outputname , "w")


###########################################
array1=[]
array2=[]
arraynome=[]
arrayscore=[]
arrayscore2=[]
arrayscoref=[]
for i in orgn:
    j=i.split("\t")
    array1.append(j[0])
    arrayscore.append(j[2])

for i in orgx:
    x=i.split("\t")
    array2.append(x[0])
    arrayscore2.append(x[2])
    

s=0
for d in array1:
    u=0
    for e in array2:
        if (d==e):
            arraynome.append(d)
            if (arrayscore[s]!="na" and arrayscore2[u]!="na"):
                t= arrayscore[s].strip(" ")
                q= arrayscore2[u].strip(" ")
                o= (float(t))+(float(q))
                arrayscoref.append(o/2.0)
            if (arrayscore[s]=="na" and arrayscore2[u]!="na"):
                q= arrayscore2[u].strip(" ")
                arrayscoref.append(float(q)/2.0)
            if (arrayscore[s]!="na" and arrayscore2[u]=="na"):
                t= arrayscore[s].strip(" ")
                arrayscoref.append((float(t)/2.0))
            if (arrayscore[s]=="na" and arrayscore2[u]=="na"):
                arrayscoref.append(0)                           
        u+=1
    s+=1
p=0
while (p<len(arraynome)):
       orgmed.write(arraynome[p])
       orgmed.write("\t")
       orgmed.write(str (arrayscoref[p]))
       orgmed.write("\n")
       p+=1

orgn.close()
orgx.close()
orgmed.close()
