from vex import *

#motor defs
right_drive = Motor55(Ports.port2)
left_drive = Motor55(Ports.port8)
tower_rotation = Motor55(Ports.port12)
tower_elevator = Motor55(Ports.port8)


#general defs
brain = Brain()
controller = Controller(PRIMARY)

#spider
spider_open_pos = 100
spider_close_pos = -100

expander = Triport(Ports.PORT10)
spider = Servo(expander.d)

#arcade true tank false
drive_type = True
while True:
    #drive
    if drive_type:
        left_force = controller.axis3.position() - controller.axis4.position()
        right_force = controller.axis3.position() + controller.axis4.position()
        drive(left_drive, left_force)
        drive(right_drive, right_force)

        
        