#user can create and view 2d coordinates /done
#user can find out the distance between 2 coordinates / done
#user can view distance of a coordiinates from origin / done
#user can check if a point lies on the given line /
#user can find the distnace betwwn a given 2 d point and a given line /

class Point:

  def __init__(self,x,y):
    self.x_cod=x
    self.y_cod=y


  def __str__(self):
    return'<{},{}>'.format(self.x_cod,self.y_cod)
  

  def euclidean_distance(self,other):
    return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
  
  def distance_from_origin(self):
    return (self.x_cod**2 + self.y_cod**2)**0.5
   # return self.euclidean_distance(Point(0,0))


class line:
  def __init__(self, a,b,c):
    self.a=a
    self.b=b
    self.c=c

  def __str__(self):
    return '<{},{}>'.format(self.a,self.b,self.c)
  
  def point_on_line(line,point):
    if line.a*point.x_cod +line.b*point.y_cod +line.c ==0:
      return "lies on thr line"
    else:
      return "does not lie on line "
    
  def shortest_dist(line,point):
    abs(line.a*point.x_cod+line.b*point.y_cod+line.c)/(line.a**2+line.b**2)


p1=Point(0,0)
p2=Point(1,2)
l1= line(1,1,-2)

print(p1.euclidean_distance(p2))
print(l1.point_on_line(p2))
print(l1.shortest_dist(p1))