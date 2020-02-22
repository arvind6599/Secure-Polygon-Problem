import math
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #return shifted point
    def shift(self,m,n):
        return point(self.x+m,self.y+n)

    def __str__(self):
        a=int(self.x*100)/100
        b=int(self.y*100)/100
        return "x="+str(a)+" y="+str(b)
    
    #return mirrored point
    def mirror_right(self):
        return point(2-self.x,self.y)
    
    def mirror_top(self):
        return point(self.x,2-self.y)

    def mid(self,p):
        return point(0.5*(self.x+p.x),0.5*(self.y+p.y))

    def reverse_translate(self):
        
        x=math.floor(self.x)%2
        y=math.floor(self.y)%2
        #print(x,y)
        #lattic 1
        if(x==0 and y==0):
            #print("lattice 1")
            return point(self.x%2,self.y%2)
		#lattice 2
        elif(x==0 and y==1):
            #print("lattice 2")
            return point(self.x%2,2-self.y%2)
		#lattice 3
        elif(x==1 and y==0):
            #print("lattice 3")
            return point(2-self.x%2,self.y%2)
		
		#lattice 4
        else:
            #print("lattice 4")
            return point(2-self.x%2,2-self.y%2)

    #remove the redundant blocks that lie on the boundary
    def redundant(self):
        k=1
        if(self.x==0 or self.x==1 or self.y==0 or self.y==1):
            k=0
        return k
print(" enter the coordinates for the assasin and target between 0 and 1")
'''
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
'''
x1,y1=[0.5,0.1]
x2,y2=[0.6,0.1]
ass=point(x1,y1)
t1=point(x2,y2)
t2=t1.mirror_top()
t3=t1.mirror_right()
t4=t3.mirror_top()

print("TARGET : ",t1)
print("ASSASIN : ",ass)

ts=[t1,t2,t3,t4]
r1=[]
r2=[]
r3=[]
ps=[]
ms=[]
b=[]
k=[]
for i in range(4):
	for j in range(4):
		r1.append(j)
		r2.append(j)
		r3.append(j)
	ps.append(r1)
	ms.append(r2)
	b.append(r3)
	r1=[]
	r2=[]
	r3=[]
#print(ps)

n=0
#prining all 16 target images we are concerned with

print("co-ordinates are :")
for i in range(4):
	for j in range(4):
		if(i==0):
			ps[i][j]=ts[j]
		if(i==1):
			ps[i][j]=ts[j].shift(-2,0)
		if(i==2):
			ps[i][j]=ts[j].shift(0,-2)
		if(i==3):
			ps[i][j]=ts[j].shift(-2,-2)
		#print(ps[i][j])
		
		ms[i][j]=ass.mid(ps[i][j])
		b[i][j]=ms[i][j].reverse_translate()
		if(b[i][j].redundant()==1):
			n+=1
			print(b[i][j])
#print(ps)

print(" number of blocks = ",n)

		
		
		

