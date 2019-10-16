#we import only random class
import random
#ypologizw prwta factorial
number=input('Please give the characters:')
def factorial(number):
    result=1
    for i in range(1,number+1):
        result=result*i
    return result
def splitstring(number):
    listb=[]
    for c in number:
        listb.append(c)
    return listb
#print(number)
n1=factorial(len(number))
#print(str(n1))
listb=splitstring(number)
#print(listb)
random.shuffle(listb)
#print(listb)
def shuffle_list(listbb):
    our_list=[]
    ko=1
    while True:
        if(len(our_list)==n1):
            break
        else:
            if(listbb in our_list):
               
                listbb=random.sample(listbb,len(listbb))
                
                
            else:
                
                our_list.append(listbb)
        ko=ko+1
    return our_list
my_list=shuffle_list(listb)
print(my_list)
            
