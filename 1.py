#prwtos onomazetai ka8e 8etikos akeraios pou einai megalyteros tou 1
#kai exei mono 2 8etikes diairetes.To 1 kai ton euato tou


klio=1
#h listb 8a periexei olous tous ari8mous apo to 1-100
listb=[]
while klio<=100:
    #vazw sth lista olous tous ari8mous apo to 1-100
    listb.append(klio)
    klio=klio+1

def calculatefirstnumbers(start,end,listb):
    #h lista 8a exei tous prwtous ari8mous
    lista=[]
    count=0
    while(start<=end):
        if start==1 or start==2:
            lista.append(start)
        else:
            for i in listb[:start]:
                listc=listb[:start]
                if(listc[-1]%i==0):
                    count+=1
            
            if(count==2):
                print(str(start)+' is a prime number')
                lista.append(start)
        count=0
        start=start+1
    return lista
listbb=calculatefirstnumbers(1,100,listb)
print('#'*20)
print(listbb)
print('#'*20)
def calculatedistance(number):
    b=number-1
    d=100-number
    return max(b,d)
for kl in listbb:
    print('The max distance for the prime number:'+str(kl)+' is '+str(calculatedistance(kl)))
            
                    
            
        
