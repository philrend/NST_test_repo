import numpy as np

with open('c:/Users/psr1/Desktop/data/combi_V2O5_V2O5HfO2_20140312.PLD', 'r') as fin:
	txt = fin.readlines()

p=[]
v=[]
cindex = 0
currun = 0
ite=0

weirdstuff= ""

for i, line in enumerate(txt):
	if('=' in line and 'STEP' not in line):
		a,b = txt[i].split('=')
		p.append(a)
		v.append(b)
		cindex+=1
	elif('STEP' in line and '=' not in line):
		print('Step found===========================')
		currun+=1
		cindex=0
	else:
		pass
		#print('\n**************Huh?**************\n' + line)
		weirdstuff += line
		#a,b = txt[i].split('=')
		#p.append(a)
		#v.append(b)
		#cindex =0
		
mat = np.zeros((cindex,currun)).astype(object)
pat = np.zeros((cindex,currun)).astype(object)

for i in range (0,currun):
	for j in range (0, cindex):
		mat[j][i] = v[ite]
		pat[j][i] = p[ite]
		ite+=1

		
#CSV export
with open('c:/Users/psr1/Desktop/data/expo1.txt', 'w') as fout:
	if (pat.shape == mat.shape):
		for i in range (0,pat.shape[0]):
			fout.write(str(pat[i][0])+',')
			for j in range(0,pat.shape[1]):
				mat[i][j] = str(mat[i][j]).rstrip('\n')
				fout.write(str(mat[i][j])+',')
			fout.write('\n')
	else:
		print('***parameter-value mismatch***\n')
 