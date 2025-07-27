# # list
# l = [ i ** 2 for i in range(10000000)] # 10 million

# # generator
# l = ( i ** 2 for i in range(10000000))# 10 million



# for list
import time
t1 = time.time()
l = [ i ** 2 for i in range(10000000)]
t2 =time.time() 
print(t2 - t1)


# for gen
import time
t1 = time.time()
l = ( i ** 2 for i in range(10000000))
t2 =time.time() 
print(t2 - t1)