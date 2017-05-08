import sys #for getsizeof()
import tt
import numpy as np

#Imporing module for timing found on http://stackoverflow.com/a/1557906
import timing

d = 7
n = 5

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

def ndm(*args):
    return [x[(None,)*i+(slice(None),)+(None,)*(len(args)-i-1)] for i, x in enumerate(args)]

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
    expx = [ np.exp(it) for it in x ]
    return vsum(expx)

def vsqrtabs(x):
    sqrtx = [ np.sqrt(np.abs(it)) for it in x ]
    return vsum(sqrtx)

functions = [vsum, vsinsum, vsumsin, vcossum, vsumcos, vsumsinxcos, vexp, vsqrtabs]

vtheta = np.linspace(-np.pi, np.pi, n)
# x1, x2, x3, x4, x5, x6, x7 = ndm(vtheta, vtheta, vtheta, vtheta, vtheta, vtheta, vtheta)
x1, x2, x3, x4, x5, x6, x7 = np.meshgrid(vtheta, vtheta, vtheta, vtheta, vtheta, vtheta, vtheta)

for f in functions:
    t0 = timing.log("Creating full tensor of function %s with n=%d, d=%d" %(f.func_name,n,d))
    tensor = f(np.asarray([x1,x2,x3,x4,x5,x6,x7]))
    timing.log("Full tensor created", t0)

    t0 = timing.log("Compressing tensor to TT")
    a = tt.tensor(tensor)
    timing.log("Tensor compressed", t0)

    s_tensor = n**d

    print("Size of full tensor: %d params" %(s_tensor))

    s_a = numparams(a)

    print("Size of tt representation: %d params" %(s_a))

    s_ratio = float(s_a) / s_tensor

    print("Size ratio (tt/full): %f" %(s_ratio))

    print("Dimensions of tensor: %s" %(a.n))
    print("TT-ranks of tensor: %s" %(a.r))
    print(tensor[0,1,2,3,4,0,3])
    print(a[0,1,2,3,4,0,3])
#EOF
