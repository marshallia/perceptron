import math
x=[5.1,3.5,1.4,0.2]
wji=[[0.1,0.7,-0.3,0.6],[0.3,0.4,-0.1,-0.2],[0.2,-0.5,0.8,0.4]]
bj=[0.3,-0.4,0.7]
wkj=[[0.2,-0.2,-0.3],[-0.2,0.4,0.7],[0.5,-0.1,-0.5]]
bk=[0.1,-0.7,0.5]
hj=[0,0,0]
ok=[0,0,0]
deltaO=[0,0,0]
deltah=[0,0,0]
t=[1,0,0]
'''calculate Hj and netj'''
def calcHj():
	for j in range(3):
		net=0
		for i in range(4):
			net+=x[i]*wji[j][i]
		net=net-bj[j]
		hj[j]=1/(1+math.exp(-1*net))
		print('net'+str(j)+'='+str(net)+'\t\t'+'H'+str(j)+'='+str(hj[j]))
	print('\n')

'''calculate Ok and delta'''
def calcOk():
	for k in range(3):
		net=0
		for j in range(3):
			net+=hj[j]*wkj[k][j]
		net=net-bk[k]
		#print('net'+str(k)+'='+str(net))
		ok[k]=1/(1+math.exp(-1*net))
		#print('O'+str(k)+'='+str(ok[k]))
		deltaO[k]=(t[k]-ok[k])*(1-ok[k])*ok[k]
		print('net'+str(k)+'='+str(net)+'\t\t'+'O'+str(k)+'='+str(ok[k])+'\t\t'+'deltaO'+str(k)+'='+str(deltaO[k]))
	print('\n')

'''calculate Wkj new'''
def calcWkj():
	for k in range(3):
		for j in range(3):
			wkj[k][j]=wkj[k][j]+(0.1*deltaO[k]*hj[j])
	print('wkj new :\n'+repr(wkj))


'''calculate Wji new'''
def calcWji():
	for j in range(3):
		for k in range(3):
			deltah[j]+=wkj[k][j]*deltaO[k]
		deltah[j]=hj[j]*(1-hj[j])*deltah[j]
		print('deltah'+str(j)+'='+str(deltah[j]))
		
		for i in range(4):
			wji[j][i]=wji[j][i]+(0.1*deltah[j]*x[i])
	print('wji new :\n'+repr(wji))
calcHj()
calcOk()
calcWkj()
calcWji()
