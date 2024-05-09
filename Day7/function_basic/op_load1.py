class centroid:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __radd__(self,other):
        x=self.x+other
        y=self.y+other
        
        result=centroid(x,y)
        return(result)
c1=centroid(2,4)
print(c1.x,c1.y)