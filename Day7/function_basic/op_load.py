class centroid:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        result=centroid(x/2,y/2)
        return(result)
c1=centroid(10,5)
c2=centroid(20,10)
c3=c1+c2
print(c3.x,c3.y)
    