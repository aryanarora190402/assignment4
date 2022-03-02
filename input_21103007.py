#Q1
print("Q1")
def Towerofhanoi(n,initial,extra,final):
    if n==1:
        print ("Move disk 1 from rod",initial,"to rod",final)
        return
    Towerofhanoi(n-1,initial,final,extra)
    print("Move disk",n, "from rod",initial,"to rod",final)
    Towerofhanoi(n-1,extra,initial,final)
        
Towerofhanoi(3,"A","B","C") #3 disks are used as given in the problem  
                          	#A is the initial rod
							#B is the extra rod 
							#C is the final rod 
print()

#Question 2
print("Q2")
n=int(input("Enter the number of rows: "))

#using recursion:
def pascalsTriangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        newRow = [1]
        result = pascalsTriangle(n-1) #recursive statement
        lastRow = result[-1]
        for i in range(len(lastRow)-1):
            newRow.append(lastRow[i] + lastRow[i+1])
        newRow += [1]
        result.append(newRow)
    return result

print("Recursion:")
for i in pascalsTriangle(n): #returns list of lists of rows of pascal's triangle
    for j in i:              
        print(j,end=' ') #required format
    print('')

#Using iteration
def factorial(n):  #defining factorial
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return factorial(n-1)*n

def C(n,r): #defining nCr 
    return int(factorial(n)/((factorial(n-r))*(factorial(r))))

print("Iteration: ")
i=0
while i<n:
    for j in range(0,i+1):
        print(C(i,j),end=' ') #required format
    print('')
    i+=1
    print()

#Question 3
print('Q3')
while True:
    a,b=map(int,input('Enter value of a and b: ').split())
    if b==0:
        print('Division by zero is not defined!')
    else:
        break

print('(Quotient, Remainder):', divmod(a,b)) #built-in divmod function returns a tuple (a//b,a%b), i.e. quotient and remainder
print()
print("3a)")
print('Function is callable:',callable(divmod(a,b))) #callable() returns True or False for the function 
print("3b)")
print('Values entered are non-zero:', end=' ')
if max(divmod(a,b))==0: 
    print('No')
else:
    print('Yes')
print("3c)")
print('After addition:',end=' ')
lst=list(divmod(a,b)) #converts tuple into a list
lst=lst+[4,5,6]
tup=tuple(lst) #converts the list back into a tuple
print(tup, end=' ')
print('and after filtering:',end=' ')
new_lst=[] #empty list
for i in lst:
    if i<=4:
        new_lst+=[i] 
new_tup=tuple(new_lst) #new tuple from list with values <=4 using built-in tuple function
print(new_tup)
print("3d)")
print(set(new_tup)) #converts into set
print("3e)")
print(frozenset(set(new_tup))) #converts into immutable set
print("3f)")
print("Max value is: ",max(frozenset(set(new_tup))), 'and its Hash value is:',hash(max(frozenset(set(new_tup))))) #max() gives the max value and hash() gives the hash value
print()

#Q4
print("Q4")
class Student:
    def __init__(self,name,sid):
        self.name=name
        self.sid=sid
    def show(self):
        print("Name: ",self.name)
        print("SID: ",self.sid)
    def __del__(self):
        print("The object has been destroyed.")

name=input("Enter name of the student: ")
sid=int(input("Enter SID of the student: "))
stud1=Student(name,sid)
stud1.show()
del stud1
print()

#Q5
print("Q5")
class Employee: #creates new class
    def __init__(self,name,salary): #constructor
        self.name=name #records name
        self.salary=salary #records salary

E1=Employee("Mehak",40000)
E2=Employee("Ashok",50000)
E3=Employee("Viren",60000)

print("5a)")
E1.salary=70000 #salary changed
print("Updated Salary of Mehak: ",E1.salary)
print("5b)")
del E3 #deletes E3's records(name and salary)
print("Viren's record deleted.")
print()

#Q6
print("Q6")
def anagram(word):
    if len(word)==1:
        return [word]
    partial=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
        return result

george=input("Enter a word: ")
possible=anagram(george)
barbie=input("Enter another word: ")
print("The possible words are: ",possible)
if barbie in possible:
    print("The friendship is real")
else: 
    print("The friendship is fake")
