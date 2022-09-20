
print("Starting...")

#This calculates the area of a shape####################################
def area_calc():
    while True:
        shape = input("Enter C for Circle or T for Triangle: ").lower()

        if shape == "c":
            pi = 22 / 7.0
            radius = float(input("Enter Radius: "))
            area = pi * radius * radius
            print(area)
            print("Goodbye")
            break

        if shape == "t":
            base = float(input("Enter Base: "))
            height = float(input("Enter Height: "))
            area = base * height / 2
            print(area)
            print("Goodbye")
            break

        print("Invalid Input")


#This converts farenheit to celcius and vice versa######################## 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return round(c_temp, 1)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return round(f_temp, 1)

#f100_in_celcius = f_to_c(100)
#print(f100_in_celcius)

#c0_in_farenheit = c_to_f(0)
#print(c0_in_farenheit)


#This calculates force####################################################
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass * acceleration

#train_force = get_force(train_mass, train_acceleration)
#print("The GE train supplies %s Newtons of force." % (train_force))

def get_energy(mass, c=3*10**8):
  return mass * c

#bomb_energy = get_energy(bomb_mass)
#print("A 1kg bomb supplies %s Joules." % (bomb_energy))

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

#train_work = get_work(train_mass, train_acceleration, train_distance)
#print("The GE train does %s Joules of work over %s meters" % (train_work, train_distance))


#This calculates the radius of a circle############################################################
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def __repr__(self):
        return "Circle with radius {}".format(self.radius)

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

#medium_pizza = Circle(12)
#teaching_table = Circle(36)
#round_room = Circle(11460)


#This calculates the area of a triangle###############################################################
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  number_of_sides = 3
  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False

class Equilateral(Triangle):
  angle = 60
  def __init__(self, angle1, angle2, angle3):
    super().__init__(angle1, angle2, angle3)
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

#my_triangle = Triangle(90, 30, 60)
#print(my_triangle.number_of_sides)
#print(my_triangle.check_angles())


#None Class version of an area calculator####################################
def area_calc():
    while True:
        shape = input("Enter C for Circle or T for Triangle: ").lower()

        if shape == "c":
            pi = 22 / 7.0
            radius = float(input("Enter Radius: "))
            area = pi * radius * radius
            print(area)
            print("Goodbye")
            break

        if shape == "t":
            base = float(input("Enter Base: "))
            height = float(input("Enter Height: "))
            area = base * height / 2
            print(area)
            print("Goodbye")
            break

        print("Invalid Input")



#This converts HEX to RGB and vice versa######################################
def rgb_hex():
    invalid_msg = "Error"
    red = int(input("Please Enter Red Value: "))
    if red < 0 or red > 255:
        print(invalid_msg)
        return
    green = int(input("Please Enter Green Value: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return
    blue = int(input("Please Enter blue Value: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return

    val = (red << 16) + (green << 8) + blue
    print("%s" % (hex(val)[2:]).upper())


def hex_rgb():
    hex_val = input("Enter the six digit hexidecimal value: ")
    if len(hex_val) != 6:
        print("Must be six digits long, yours was: %s" % len(hex_val))
        return
    else:
        hex_val = int(hex_val, 16)
    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print("blue: %s, green: %s, red: %s" % (blue, red, green))


def convert():
    while True:
        option = input("Enter 1 to convert RGB to HEX, Enter 2 to convert HEX to rgb, Enter 3 to Exit: ")
        if option == "1":
            print("RGB to HEX....")
            rgb_hex()
        elif option == "2":
            print("HEX to RGB....")
            hex_rgb()
        elif option == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input")


#convert()

