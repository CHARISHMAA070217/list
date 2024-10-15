'''
def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 
  
# Driver Code 
A=list()
n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First  List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
splitevenodd(A) 
output:
Enter the size of the First List :: 8
Enter the Element of First  List ::
1
2
3
4
5
9
8
6
Even lists: [2, 4, 8, 6]
Odd lists: [1, 3, 5, 9]
'''
