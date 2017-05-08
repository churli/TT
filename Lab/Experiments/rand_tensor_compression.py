#Prova

import sys #for getsizeof()
import tt
import numpy as np
import random
import cPickle as pickle

#Imporing module for timing found on http://stackoverflow.com/a/1557906
import timing

d = 100
n = 10
r = 2

sparseness = 1e-3
maxexp = 3
eps = 1e-3

def numfullparams(tensor):
    s = 1
    for i in range(1,tensor.d):
        s = s * tensor.n[i]
    return s

def numparams(tensor):
    s_tensor = 0
    for k in range(1,tensor.d):
        s_tensor += tensor.r[k-1] * tensor.n[k-1] * tensor.r[k]
    return s_tensor


#Shape is given as an array long as the number of dimensions d
#and having as i-th value the 'length' of the i-th dimension
# timing.log("Creating shape")
# shape = n * np.ones(d, dtype=np.int)

#Now initializing a tensor of such shape with all 0
# timing.log("Init 0 tensor")
# tensor = np.zeros(shape)

# #Here initializing also an array of 0 long d
# z = np.zeros(d, dtype=np.int)

#Now populating the tensor:
# Populating rng number of elements in the tensor
# rng = random.randint(1,round((n**d) * sparseness))
# timing.log("Number of elements to populate: %d" %rng)
# t0 = timing.log("Start populating tensor")
# for i in range(rng):
#     #Calculating value
#     val = random.random() * 10 ** random.randrange(maxexp+1)
#     #Calculating position array (indices)
#     pos = tuple( [ random.randrange(n) for x in range(d) ] )
#     #Setting val at position pos in tensor
#     tensor.itemset(pos, val)
# timing.log("End populating tensor", t0)

t0 = timing.log("Creating random tensor with n=%d, d=%d, r=%d" %(n,d,r))
a = tt.rand(n, d, r)
timing.log("Tensor created", t0)
#s_tensor = numfullparams(a)
s_tensor = n**d

# fd = open("full_tensor.pkl",'wb')
# pickle.dump(tensor, fd)
# fd.close()

print("Size of full tensor: %d params" %(s_tensor))
#print(tensor)

# t1 = timing.log("Starting compression")
# a = tt.tensor(tensor, eps)
# timing.log("End compression", t1)

s_a = numparams(a)

# fd = open("tt_tensor.pkl",'wb')
# pickle.dump(a, fd)
# fd.close()

print("Size of tt representation: %d params" %(s_a))

s_ratio = float(s_a) / s_tensor

print("Size ratio (tt/full): %f" %(s_ratio))

timing.log("Dumping tensor to file...")
a.write("tt_tensor.dump")

#EOF
