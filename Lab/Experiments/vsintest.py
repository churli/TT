import tt, numpy as np
from tt.cross import rect_cross as cross

d = 7
n = 5

#vtheta = np.asarray([ x*(np.pi/n) for x in range(n)] )
vtheta = np.linspace(-np.pi, np.pi, n)

def getvtheta(x):
        return vtheta[int(x)]

vgetvtheta = np.vectorize(getvtheta)

def vsum(x):
        return vgetvtheta(x).sum(axis=1)

def vsin(x):
	return np.sin(vsum(x))

functions = [vsum, vsin]

for f in functions:
        # funct = lambda x : np.asarray( [ f(v) for v in x ] )

        tones = tt.ones(n,d)
        tensin = cross(f, tones, nswp=10)
        
        print(vsin([[0,1,2,3,4,0,3]]))
        print(tensin[0,1,2,3,4,0,3])

#EOF

