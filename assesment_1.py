import csv

class NoData(Exception):  #custom exception for empty file
    pass

def loadData():
        try:
            global name
            name = input("Enter file name:")
            print()
            new_name = name +'.csv' #concat the file format
            global fptr
            fptr = open(new_name,'r')
            global a
            a=fptr.read()
            if len(a) <= 1: #Check for file is empty
                raise NoData
            print("Data loaded sucessfully!\n")
        
        except FileNotFoundError:
            print("file not found")
        
        except NoData:
            print("This file has no data/empty\n")
            

d={}

def displayData():
    new_name = name + '.csv'
    fptr = open(new_name,'r')
    
    for line in fptr:
        l = line.split(',')
        key = l[0] #Dataset nam
        val = l[1:] #Data
        d[key] = val
    
    global l1
    global l2
    l1 = list(d.keys())
    l2 = list(d.values())
    
    if d == 0:
        print("No datasets to display!")
    
    else:
        for key,val in d.items(): #Display the data
            print(key)
            print("-"*len(key))
            print(*val)
    
def renameSet():
    print("Which set you want to rename?")
    
    for i in l1:
        print("\t",l1.index(i)+1,"->",i)
    
    try:
        choice = inputForChoice()   
    except:
        print("Error! Please enter proper input\n")
        choice = inputForChoice()
    
    new_name = str(input("Please enter a new name would like to replace:\n "))
    l1[choice-1] = new_name
    
    d = zip(l1,l2)
    d = dict(d)
    
    for key,val in d.items():
        print(key)
        print("-"*len(key))
        print(*val)
    
    return d

def sortSet(data):
    print("Which set you want to sort\n")
    
    global l1
    for i in l1:
        print("\t",l1.index(i) + 1,"->",i)
    
    try:
        choice=inputForChoice()    
    except:
        print("Error! Please enter proper input\n")
        choice=inputForChoice()
    
    l1 = list(data.keys())
    l2 = list(data.values())
    
    new_list=[[int(x) for x in list ]for list in l2] #Here data inside nested list is of type,
    #string format which is converted to int format
    
    l3 = new_list[choice-1]
    l3.sort()
    new_list[choice-1] = l3
    
    global d
    d = zip(l1,new_list)
    d = dict(d)
    
    for key,val in d.items():
        print(key)
        print("-"*len(key))
        print(*val)

def analyzeSet():
    print("Which set you want to analyze\n")
    
    for i in l1:
        print("\t",l1.index(i)+1,"->",i)
    
    try:
        choice = inputForChoice()    
    except:
        print("Error! Please enter proper input\n")
        choice=inputForChoice()
           
    key = l1[choice-1]
    print(key)
    print('-'*len(key))
    
    l3 = d[key]
    l4 = [int(i) for i in l3] #For converting data into int format, by default is in str format
    print(l4)
    
    s = sum(l4)
    n = len(l4)
    mean = s/n #calculates mean
    
    l4.sort()
    if n%2 == 0:
        med1 = l4[n//2]
        med2 = l4[n//2-1]
        med = (med1+med2)/2 # Median
    else:
        med = l4[n//2]
    
    def mode(data):
        d = {} 
        for i in data: 
            d[i] = data.count(i)
        
        return(max(d, key=d.get))
    
    def standardDeviation(data):
        mean = sum(data)/len(data) 
        variance = sum([((x - mean) ** 2) for x in data]) / len(data) 
        res = variance ** 0.5
        return res
    
    print("number of values (n):",len(l4))
    print("minimum:",min(l4))
    print("maximum:",max(l4))
    print("mean:",mean)
    print("median:",med)
    print("mode:",mode(l4))
    print("standard deviation:",round(standardDeviation(l4),2))
    print()
    fptr.close()

def save(z):
    new_file_name = input("enter new file name:")
    new_file_name=new_file_name + ".csv"
    with open(new_file_name, 'w') as csv1:  
        fptr = csv.writer(csv1)
        for key,val in d.items():
            fptr.writerow([key,val])
    print("Data saved into new csv file")



def get_valid_option(): #user input
   try:
       x = input()
       x = int(x)
       while x < 1 or x > 9:
           print('Invalid option!! Please choose any among 1 to 9:')
           x = input()
           x = int(x)

       return x
   except ValueError:
       print("Please enter input in integer format only")
       
def inputForChoice():
    while True:
        x = input(">>> ")
        x = int(x)
        if x <= 0 and x > len(l1):
            print("Invalid Input! Please Choose b/w 1 and {}".format(len(l1)))
            continue
        else:
            return x

print('Welcome to The Smart Statistician!')
print('Programmed by Steevan Lenson Moras \n')



while True:
    
    print()
    print('Please choose from the following options:')
    print('\t1 - Load data from a file')
    print('\t2 - Display the data to the screen')
    print('\t3 - Rename a set')
    print('\t4 - Sort a set')
    print('\t5 - Analyze a set')
    print('\t6-Save data to file')
    print('\t7-Compare two datasets')
    print('\t8-Edit a set')
    print('\t9 - Quit')
    print(">>>")
    
    option = get_valid_option()  #To collect user input
   
    if option == 1:
        loadData() 
    
    elif option == 2:
        displayData() 
    
    elif option == 3:
        res=renameSet()
        d=res       
    
    elif option == 4:
        sortSet(d) 
    
    elif option == 5:
        analyzeSet()   
    
    elif option == 6:
        save(d)
        break
    

