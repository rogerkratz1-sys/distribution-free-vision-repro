import numpy as np
def pooled_sd(x,y):
    sd1,sd2 = x.std(ddof=1), y.std(ddof=1)
    return (((len(x)-1)*sd1*sd1 + (len(y)-1)*sd2*sd2)/(len(x)+len(y)-2))**0.5
c = np.loadtxt("d_cluster_clean.csv", ndmin=1)
n = np.loadtxt("d_null_clean.csv", ndmin=1)
for k in (2,4,5,10,20):
    m = min(len(c)//k, len(n)//k)
    if m == 0:
        print(f"k={k} not applicable")
        continue
    csub = c[:m*k].reshape(m,k).mean(axis=1)
    nsub = n[:m*k].reshape(m,k).mean(axis=1)
    psd = pooled_sd(csub,nsub)
    d = (csub.mean()-nsub.mean())/psd
    J = 1 - (3.0/(4.0*(len(csub)+len(nsub))-9.0))
    print(f"k={k} per-subj n={len(csub)} mean_diff={(csub.mean()-nsub.mean()):.6g} pooled_sd={psd:.6g} d={d:.6g} g={d*J:.6g}")
