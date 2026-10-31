#Tag class
class Tag:
    # id is april tag id, x and y are feild location in feet from undecided referance, rot is what  what direction the tag is facing, 360 degrees even though they only face 0 90 180 270 degrees 
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

#example tag
def main():
    tag = Tag(12, 13.75, 10, 0)
    print(tag.get())

main()