import tt, numpy as np
from tt.cross import rect_cross as cross
import timing

D = [10, 25, 50, 100, 200]
n = 10

#vtheta = np.asarray([ x*(np.pi/n) for x in range(n)] )
vtheta = np.linspace(-np.pi, np.pi, n)

def getvtheta(x):
    return vtheta[int(x)]

vgetvtheta = np.vectorize(getvtheta)

def vsum(x):
    return vgetvtheta(x).sum(axis=1)

def vsin(x):
    return np.sin(vsum(x))

def numparams(tensor):
    s_tensor = 0
    for k in range(1,tensor.d):
        s_tensor += tensor.r[k-1] * tensor.n[k-1] * tensor.r[k]
    return s_tensor

functions = [vsum, vsin]

header = ["d","n","sizeFull"]
for f in functions:
    header.append("%s_ttSize" %(f.func_name))
    header.append("%s_tensorCrossApproxTime" %(f.func_name))
    
results = [] # Each dim: [d,n,sizefull,f1_ttSize,f1_sizeRatio,...]

for d in D:
    print("### DIMENSION %d ###" %(d))
    localResults = [d,n,"%d^%d"%(n,d)]

    for f in functions:
        t0 = timing.log("Cross-aproximating tensor to TT")
        tones = tt.ones(n,d)
        tensin = cross(f, tones, nswp=10)
        tFoo, tDiffCross = timing.log("Tensor compressed", t0)
        size = numparams(tensin)
        print("n = %d, d = %d, numparams = %d, tDiffCross = %s" %(n,d,size,tDiffCross))
        localResults.append(size)
        localResults.append(tDiffCross)
        
    results.append(localResults)

f = open("results_cross.csv", 'w')
f.write(";".join(header)+"\n")
for line in results:
    sLine = [str(x) for x in line]
    f.write(";".join(sLine)+"\n")
f.close()
        
#EOF

