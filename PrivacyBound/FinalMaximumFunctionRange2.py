from mainfunctions import *
from multiprocessing import Pool, Lock, Manager

gcoleps = []
gcolm = []
gcolM = []
gcolDiffEvol = []
gcolHypValue = []
gcolDiff = []

### eps between 2 and 9.9 (step 0.1)
with Pool(64) as p:
    results = p.map(iteration,[ep/10 for ep in range(20,100)])

    for r in results:
        gcoleps.extend(r[0])
        gcolm.extend(r[1])
        gcolM.extend(r[2])
        gcolDiffEvol.extend(r[3])
        gcolHypValue.extend(r[4])
        gcolDiff.extend(r[5])

d={'Epsilon': gcoleps, 'm': gcolm, 'M': gcolM, 'DiffEvol': gcolDiffEvol, 'HypValue': gcolHypValue, 'Difference': gcolDiff}
df = pd.DataFrame(data=d)
df.to_csv('output_range2.csv',index=False,sep=';')

print("Minimum difference: ", df["Difference"].min())
print("Maximum difference: ", df["Difference"].max())  

