from vex import *
from math import sqrt
from tag import Tag

#tag class cuz friken vex is poopy
#Tag class
class Tag:
    # id is april tag id, x and y are feild location in inches from undecided referance, rot is what  what direction the tag is facing, 360 degrees even though they only face 0 90 180 270 degrees 
    def __init__(self, id, x, y, rot):
        self.id = id
        self.x = x
        self.y = y
        self.rot = rot

    def get(self):
        return [self.id, self.x, self.y, self.rot]

    def get_x(self):
        return self.x
    def get_y(self):
            return self.y
    def get_id(self):
            return self.id
    def get_rot(self):
            return self.rot

tags = {
    # tables: 3 x 3 grid, 36 in apart, centered on the field (flat, face up)
    0: Tag(0, 105, 177, None),
    1: Tag(1, 141, 177, None),
    2: Tag(2, 177, 177, None),
    3: Tag(3, 105, 141, None),
    4: Tag(4, 141, 141, None),
    5: Tag(5, 177, 141, None),
    6: Tag(6, 105, 105, None),
    7: Tag(7, 141, 105, None),
    8: Tag(8, 177, 105, None),
    # blue/red-side short wall (y = 207), facing -y toward the tables
    9: Tag(9, 123, 207, 270),
    10: Tag(10, 159, 207, 270),
    # red/green-side long wall (x = 207), facing -x toward the tables
    11: Tag(11, 207, 195, 180),
    12: Tag(12, 207, 159, 180),
    13: Tag(13, 207, 123, 180),
    14: Tag(14, 207, 87, 180),
    # yellow/green-side short wall (y = 75), facing +y toward the tables
    15: Tag(15, 159, 75, 90),
    16: Tag(16, 123, 75, 90),
    # blue/yellow-side long wall (x = 75), facing +x toward the tables
    17: Tag(17, 75, 87, 0),
    18: Tag(18, 75, 123, 0),
    19: Tag(19, 75, 159, 0),
    20: Tag(20, 75, 195, 0),
}

#turns pixels into distance in inches based on an undetermined function derrived from testing the realitive size of tags at diffrent distances, something like distance = real width times something over seen pixeles
def get_distance(width, hight):
    distance_constant = 160.3521 #desmos regression https://www.desmos.com/calculator/ul74kkrtmd
    tag_dimension = 4.25 #inside black square
    distance= (tag_dimension*distance_constant)/hight #random example test real
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