# array of tag instances corrosponding to the feild and sorted by id
from math import sqrt
from tag import Tag
tags = {0: Tag(0, 124, 100, 0), 1: Tag(1, 180, 101, 0), 2: Tag(2, 140, 160, 90)}

#turns pixels into distance in inches based on an undetermined function derrived from testing the realitive size of tags at diffrent distances, something like distance = real width times something over seen pixeles
def get_distance(width, hight):
    distance_constant = 50 #temp
    tag_dimension = 20 #temp
    distance= (tag_dimension*distance_constant)/width #random example test real
    return distance

#snapshot tags is a nested array, the first element is tag id the second is width third is hight fourth is rotation
def get_pose(snapshot_tags):
    distances = []
    for i in range(len(snapshot_tags)):
        distances.append(get_distance(snapshot_tags[i][1], snapshot_tags[i][2]))


    #circles
    # circle formula (x - tags[snapshot_tags[0][0]].get_x())**2 + (y + tags[snapshot_tags[0][0]].get_y())**2 == distances[0]**2
    #d is center distance between circles, |x0-x1|
    #formula for a is (r0^2-r1^2+d^2)/2d
    #a is x dimension of intersection, find y using pythagorean theorem
    #a^2+r0^2=h^2
    #final stuff i think, p0 is center of first circle = (x0, y0) p1 is center of second circle = (x1, y1) p2 
    #a2+b2=r02 first one last one two middle ones

    #pose estimation with two points, aligned on x axis needs to be adjusted for any orientation
    # d = abs(tags[snapshot_tags[0][0]].get_x()-tags[snapshot_tags[1][0]].get_x())
    # x = (distances[0]**2-distances[1]**2+d**2)/(2*d)
    # y = sqrt(distances[0]**2-x**2)

    #diffrent method based on line circle thing
    #circle decided as orgin x^2+y^2=r^2
    # circle formula (x - tags[snapshot_tags[0][0]].get_x())**2 + (y + tags[snapshot_tags[0][0]].get_y())**2 == distances[0]**2

    #circle one variableas
    a = tags[snapshot_tags[0][0]].get_x()
    b = tags[snapshot_tags[0][0]].get_y()
    r = distances[0]

    #second
    p = tags[snapshot_tags[1][0]].get_x()
    q = tags[snapshot_tags[1][0]].get_y()
    d = distances[1]

    #intersecting line equation y=mx+c
    m = (p-a)/(b-q)
    c = (a**2+b**2+d**2 - (p**2+q**2+r**2))/(2*(b-q))

    #quadratic for line circle intersection x value ax**2+bx+c use quad form to get x
    A = 1+m**2
    B = 2*(m*(c-b)-a)
    C = a**2+(c-b)**2-r**2

    X = (-B+sqrt(B**2-4*(A*C)))/(2*A)
    Y = m*X+c
    return [X, Y]


test_snapshot = [[0, 15, 15, 23], [2, 13, 13, 80]]
print(get_pose(test_snapshot))