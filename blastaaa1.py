#uses the blastn outfmt=1 output and organizes it in 
#contig_name    blast_result    score    evalue

import argparse

parser = argparse.ArgumentParser(description="blast output organization")

parser.add_argument("-in",dest="outputdoblast",required=True,help="Provide the blast output")

parser.add_argument("-out",dest="outputname",required=True,help="Provide the destination flie")

arg = parser.parse_args()


blast= open (arg.outputdoblast)

listanomes= open (arg.outputname , "w")


arraynomes=[]
arrayblast=[]
arrayscore=[]
arrayevalue=[]
arrayetc=[]
segundaparte=[]
for t in blast:
    if (t.startswith("Query=")==True):
        u=0
        s= t.strip('Query= ' "\n")
        l= s + "\t"
        arraynomes.append(l)
    if (t.startswith("emb")==True or t.startswith("gb")==True and u==0):
        if (u==0):
            e=t.rstrip("  \n")
            g= e.rsplit("  ",1)
            print g
            f=g[0].rsplit("   ",1)
            print f
            nome= f[0]+ "\t"
            arrayblast.append(nome)
            score=f[1]+ "\t"
            arrayscore.append(score)
            arrayevalue.append(g[1])
            u+=1    
    if (t.startswith("*")==True):
        arrayblast.append("na\t")
        arrayscore.append("na\t")
        arrayevalue.append("na")
print arraynomes

s=0
while (s<len (arrayblast)):
    listanomes.write(arraynomes[s])
    listanomes.write(arrayblast[s])
    listanomes.write(arrayscore[s])
    listanomes.write(arrayevalue[s])
    listanomes.write("\n")
    s+=1

blast.close()
listanomes.close()
