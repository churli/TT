import sys #for getsizeof()
import tt
import numpy as np

#Imporing module for timing found on http://stackoverflow.com/a/1557906
import timing

D = [3,4,5,6,7]
n = 10

checkElemIndex = (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)

eps = 1e-12

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

def getvtheta(x):
    return vtheta[x]
    
def vsum(x):
    s = 0
    for item in x:
        s = s + item
    return s
    
def vsinsum(x):
    return np.sin(vsum(x))

def vsumsin(x):
    sinx = [ np.sin(it) for it in x]
    return vsum(sinx)

def vcossum(x):
    return np.cos(vsum(x))

def vsumcos(x):
    cosx = [ np.cos(it) for it in x]
    return vsum(cosx)
    
def vsumsinxcos(x):
    sinxcos = [ np.sin(it) * np.cos(it) for it in x]
    return vsum(sinxcos)

def vexp(x):
    expx = [ np.power(x[i],i) for i in range(len(x)) ]
    return vsum(expx)

def vsqrtabs(x):
    sqrtx = [ np.sqrt(np.abs(it)) for it in x ]
    return vsum(sqrtx)

#functions = [vsum, vsinsum, vsumsin, vcossum, vsumcos, vsumsinxcos, vexp, vsqrtabs]
functions = [vsum, vsinsum, vexp, vsqrtabs]

vtheta = np.linspace(-np.pi, np.pi, n)

header = ["d","n","sizeFull"]
for f in functions:
    header.append("%s_ttSize" %(f.func_name))
    header.append("%s_sizeRatio" %(f.func_name))
    header.append("%s_tensorCreationTime" %(f.func_name))
    header.append("%s_tensorCompressionTime" %(f.func_name))
    
results = [] # Each dim: [d,n,sizefull,f1_ttSize,f1_sizeRatio,...]

for d in D:
    print("### DIMENSION %d ###" %(d))
    xVec = np.meshgrid(*tuple([vtheta for x in range(d)]))

    localResults = [d,n,n**d]

    for f in functions:
        t0 = timing.log("Creating full tensor of function %s with n=%d, d=%d" %(f.func_name,n,d))
        tensor = f(np.asarray(xVec))
        tFoo, tDiffCreation = timing.log("Full tensor created", t0)
        
        t0 = timing.log("Compressing tensor to TT")
        a = tt.tensor(tensor)
        tFoo, tDiffCompression = timing.log("Tensor compressed", t0)
        
        s_tensor = n**d
        
        print("Size of full tensor: %d params" %(s_tensor))
        
        s_a = numparams(a)
        
        print("Size of tt representation: %d params" %(s_a))
        
        s_ratio = float(s_a) / s_tensor
        
        print("Size ratio (tt/full): %f" %(s_ratio))
        
        print("Dimensions of tensor: %s" %(a.n))
        print("TT-ranks of tensor: %s" %(a.r))
        cIndex = checkElemIndex[:d]
        print("Check element at "+str(cIndex))
        print(tensor[cIndex])
        print(a[cIndex])

        localResults.append(s_a)
        localResults.append(s_ratio)
        localResults.append(tDiffCreation)
        localResults.append(tDiffCompression)
        
    results.append(localResults)

f = open("results.csv", 'w')
f.write(";".join(header)+"\n")
for line in results:
    sLine = [str(x) for x in line]
    f.write(";".join(sLine)+"\n")
f.close()
#EOF
