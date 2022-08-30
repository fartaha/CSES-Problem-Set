"""
    This code get an integer input from the user and generate a sequence as follows:
    If n is even, it is divided by two and if it is odd, it is multiplied by 3 plus one
    untill the seq reaches 1. Time limit: 1.00 s Memory limit: 512 MB
        Example:
            input = 3
            output = 3 10 5 16 8 4 2 1
"""
#import time
#start_time = time.time()

#import tracemalloc
#tracemalloc.start() # It traces the memodary usage by the alogrithm
n = int(input())
N = [n]

if 1<=n<=10**6: # Applying the constraint on input value
    while n!=1: # Stop running the loop after reaching n = 1
        if n%2==0: 
            n=n/2
            N.append(int(n))
            #print(int(n))
        else:
            n = n*3 + 1
            N.append(int(n))
            #print(int(n))
            
print(*N) # Printing the list items separated by space

#print(tracemalloc.get_traced_memory())
#tracemalloc.stop()
#print("--- %s seconds ---" % (time.time() - start_time))
