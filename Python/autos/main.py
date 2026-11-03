#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
# AI Vision Color Descriptions
# AI Vision Code Descriptions
ai_vision_1 = AiVision(Ports.PORT1, AiVision.ALL_TAGS)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
# array of tag instances corrosponding to the feild and sorted by id
from vex import *
from math import sqrt

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

tags = {19: Tag(19, 0, 20, 0), 20: Tag(20, 0, 52.5, 0)}

#turns pixels into distance in inches based on an undetermined function derrived from testing the realitive size of tags at diffrent distances, something like distance = real width times something over seen pixeles
def get_distance(hight):
    distance_constant = 160.3521 #desmos regression https://www.desmos.com/calculator/ul74kkrtmd
    tag_dimension = 4.25 #inside black square
    distance= (tag_dimension*distance_constant)/hight #random example test real
    return distance

#snapshot tags is a nested array, the first element is tag id the second is width third is hight fourth is rotation
def get_pose(snapshot_tags):

    if len(snapshot_tags) < 2:
        return "Not enough tags"

    distances = []

    for i in range(len(snapshot_tags)):
        distance = get_distance(snapshot_tags[i].height)

        if distance is None:
            return "Invalid tag height"

        distances.append(distance)

    if snapshot_tags[0].id not in tags or snapshot_tags[1].id not in tags:
        return "Unknown tag"

    #first tag
    a = tags[snapshot_tags[0].id].get_x()
    b = tags[snapshot_tags[0].id].get_y()
    r = distances[0]

    #second tag
    p = tags[snapshot_tags[1].id].get_x()
    q = tags[snapshot_tags[1].id].get_y()
    d = distances[1]

    #intersecting line equation y=mx+c
    m = (p-a)/(b-q)
    c = (a**2+b**2+d**2 - (p**2+q**2+r**2))/(2*(b-q))

    #quadratic
    A = 1+m**2
    B = 2*(m*(c-b)-a)
    C = a**2+(c-b)**2-r**2

    discriminant = B**2-4*(A*C)

    if discriminant < 0:
        return "No intersection"

    X = (-B+sqrt(discriminant))/(2*A)
    Y = m*X+c

    return [X, Y]
ai_objects = ai_vision_1.take_snapshot(AiVision.ALL_TAGS)

#test_snapshot = [[0, 15, 15, 23], [2, 13, 13, 80]]
#print(get_pose(test_snapshot))
while True:
    ai_objects = ai_vision_1.take_snapshot(AiVision.ALL_TAGS)
    brain.screen.set_cursor(1, 1)

    brain.screen.clear_screen()
    brain.screen.print(get_pose(ai_objects))
    wait(1, SECONDS)
