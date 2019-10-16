



#8a apo8hkeutoun oi grammes meta comments
lista=[]

with open('text.txt','r') as fp:
    for line in fp:
        if (line[0]=='/' and line[1]=='/'):
            print(line)
        elif(line[0]=='/' and line[1]=='*'):
            listv=[]
            listv.append(line)
            newlines=fp.readlines()
            for newline in newlines:
                listv.append(newline)
                if(newline[0]=='*' and newline[1]=='/'):
                    break
            for kl in listv:
                print(kl)
            
