import time
def sum_of_n(n):
   start = time.time()
   the_sum = 0
   for i in range(0, n+1):
       the_sum = the_sum + i
   end = time.time()
   return the_sum, end-start
#for i in range(5):
 #      print sum_of_n("Sum is %d required %10.7f seconds" % sum_of_n(10000))
