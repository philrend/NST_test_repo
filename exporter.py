with open('c:/Users/psr1/Desktop/data/combi_V2O5_V2O5HfO2_20140312.PLD', 'r') as fin:
	txt = fin.readlines()

fout = open('c:/Users/psr1/Desktop/data/exported.txt', 'w')

params = []
values = []
dropcount = 0
filer={}

for i, line in enumerate(txt):
	if("=" in line and 'STEP' not in line):
		a,b = txt[i].split("=")
		params.append(a)
		values.append(b)
		
		fout.write(str(i)+',')
		fout.write(str(params[i-dropcount])+',')
		fout.write(str(values[i-dropcount]))
		
	else:
		fout.write('\n'+'no value this line: '+str(i)+'\n\n')
		dropcount+=1

		filer = dict(zip(params, values))

fout.close()

for t in range(0,len(txt)-dropcount): #check for repeating parameters
	if not(params[t] == params[(t+59)%(len(txt)-dropcount)]):
		print('Unique parameter found')
