import pygame
import time
import random
import threading
import multiprocessing
import math
import __main__
from pathlib import Path

pygame.init()
pygame.event.get()
pygame.font.init()
pygame.joystick.init()

#MY VARIABLES
size = [480,240]
sizeMultiplier = 1
screen = pygame.display.set_mode([size[0] * sizeMultiplier, size[1] * sizeMultiplier])
clock = pygame.time.Clock()
brainScreen = pygame.Surface((480 * sizeMultiplier, 240 * sizeMultiplier))
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
NotoMono = pygame.font.Font('NotoMono-Regular.ttf',round(17 * sizeMultiplier))
NotoSans = pygame.font.Font('NotoSans-Regular.ttf',round(17 * sizeMultiplier))
NotoSansController = pygame.font.Font('NotoSans-Regular.ttf',round(25 * sizeMultiplier))
pygame.display.set_caption(Path(__main__.__file__).stem)
if len(joysticks) > 0:
    j = joysticks[0]
    print('joystick connected!')
else:
    print('no joystick :(')
    class j:
        def get_hat(num):
            leftRightHat = 0
            upDownHat = 0
            if (pygame.key.get_pressed()[pygame.K_RIGHT]):
                leftRightHat = 1
            elif (pygame.key.get_pressed()[pygame.K_LEFT]):
                leftRightHat = -1
            if (pygame.key.get_pressed()[pygame.K_UP]):
                upDownHat = 1
            elif (pygame.key.get_pressed()[pygame.K_DOWN]):
                upDownHat = -1
            return(leftRightHat, upDownHat)
        def get_button(num):
            if (num == 0):
                return (pygame.key.get_pressed()[pygame.K_b])
            if (num == 1):
                return (pygame.key.get_pressed()[pygame.K_a])
            if (num == 2):
                return (pygame.key.get_pressed()[pygame.K_y])
            if (num == 3):
                return (pygame.key.get_pressed()[pygame.K_x])
            if (num == 4):
                return (pygame.key.get_pressed()[pygame.K_SEMICOLON])
            if (num == 5):
                return (pygame.key.get_pressed()[pygame.K_QUOTE])
        def get_axis(num):
            if (num == 0):
                if (pygame.key.get_pressed()[pygame.K_d]):
                    return (-1.00)
                elif (pygame.key.get_pressed()[pygame.K_g]):
                    return (1.00)
                else:
                    return (0)
            if (num == 1):
                if (pygame.key.get_pressed()[pygame.K_r]):
                    return (-1.00)
                elif (pygame.key.get_pressed()[pygame.K_f]):
                    return (1.00)
                else:
                    return (0)
            if (num == 2):
                if (pygame.key.get_pressed()[pygame.K_j]):
                    return (-1.00)
                elif (pygame.key.get_pressed()[pygame.K_l]):
                    return (1.00)
                else:
                    return (0)
            if (num == 3):
                if (pygame.key.get_pressed()[pygame.K_i]):
                    return (-1.00)
                elif (pygame.key.get_pressed()[pygame.K_k]):
                    return (1.00)
                else:
                    return (0)
            if (num == 4):
                if (pygame.key.get_pressed()[pygame.K_LEFTBRACKET]):
                    return (0.5)
                else:
                    return (-0.5)
            if (num == 5):
                if (pygame.key.get_pressed()[pygame.K_RIGHTBRACKET]):
                    return (0.5)
                else:
                    return (-0.5)
timeBench = 0
brainCursor = [1,1]
brainX = 0
brainY = 0
controllerCursor = [1,1]
controllerCursorOffset = 2
currentFont = 20
callbackList = []
xOffset = 0
yOffset = 0
renderMode = False
keyboardTranslation = ['b', 'a', 'y', 'x', ';', "'", '[', ']', 'DOWN', 'UP', 'LEFT', 'RIGHT', ('j','l'), ('i','k'), ('r','f'), ('d','g'), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
keyboardTranslation = [98, 97, 121, 120, 59, 39, 91, 93, 1073741905, 1073741906, 1073741904, 1073741903, (106,108), (105,107), (114,102), (100,103), 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
joystickHat = [j.get_hat(0)[0], j.get_hat(0)[1]]
joystickTriggers = [j.get_axis(4), j.get_axis(5)]
competitionMode = 1

#ENUMS
CELSIUS = 25
FAHRENHEIT = 75
MV = 12800
VOLT = 12.8
AMP = 20
MSEC = 1000
SECONDS = 1
PERCENT = 100
FORWARD = 1
REVERSE = -1
DEGREES = 1
TURNS = 360
RPM = 1
BRAKE = 0
COAST = 1
HOLD = -1
PRIMARY = 1
PARTNER = 2

class currentunits:
    def __init__(self):
        self.AMP = 20
CurrentUnits = currentunits()
class voltageunits:
    def __init__(self):
        self.MV = 12800
        self.VOLT = 12.8
VoltageUnits = voltageunits()
class tempunits:
    def __init__(self):
        self.CELSIUS = 25
        self.FAHRENHEIT = 75
TemperatureUnits = tempunits()
class timeunits:
    def __init__(self):
        self.SECONDS = 1
        self.MSEC = 1000
class voltunits:
    def __init__(self):
        self.MV = 12800
        self.VOLT = 12.8
VoltageUnits = voltunits()
class fonts:
    def __init__(self):
        self.MONO12 = 10
        self.MONO15 = 13
        self.MONO20 = 17
        self.MONO30 = 25
        self.MONO40 = 34
        self.MONO60 = 50
        self.PROP20 = -17
        self.PROP30 = -25
        self.PROP40 = -34
        self.PROP60 = -50
FontType = fonts()
class color:
    def __init__(self):
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.ORANGE = (255, 165, 0)
        self.PURPLE = (255, 0, 255)
        self.CYAN = (0, 255, 255)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.TRANSPARENT = (0, 0, 0, 0)
Color = color()
class ports:
    def __init__(self):
        self.PORT1 = 1
        self.PORT2 = 2
        self.PORT3 = 3
        self.PORT4 = 4
        self.PORT5 = 5
        self.PORT6 = 6
        self.PORT7 = 7
        self.PORT8 = 8
        self.PORT9 = 9
        self.PORT10 = 10
        self.PORT11 = 11
        self.PORT12 = 12
        self.PORT13 = 13
        self.PORT14 = 14
        self.PORT15 = 15
        self.PORT16 = 16
        self.PORT17 = 17
        self.PORT18 = 18
        self.PORT19 = 19
        self.PORT20 = 20
        self.PORT21 = 21
Ports = ports()
class gearsetting:
    def __init__(self):
        self.RATIO_6_1 = 6
        self.RATIO_18_1 = 18
        self.RATIO_36_1 = 36
GearSetting = gearsetting()
class braketype:
    def __init__(self):
        self.COAST = 1
        self.BRAKE = 0
        self.HOLD = -1
BrakeType = braketype()
class controllertype:
    def __init__(self):
        self.PRIMARY = 1
        self.PARTNER = 2
ControllerType = controllertype()
class directiontype:
    def __init__(self):
        self.FORWARD = 1
        self.REVERSE = -1
DirectionType = directiontype()
class rotationunits:
    def __init__(self):
        self.DEG = 1
        self.REV = 360
RotationUnits = rotationunits()
class torqueunits:
    def __init__(self):
        self.NM = 1
        self.INLB = 8.85
TorqueUnits = torqueunits()
class velocityunits:
    def __init__(self):
        self.PCT = 1
        self.DPS = 360
        self.RPM = 2
VelocityUnits = velocityunits()

    

        
def wait(time, units=MSEC):
    pygame.time.wait(round((time * 1000) / units))
class Thread:
    def __init__(self, callback, *arg):
        MYTHREAD = threading.Thread(target=callback, args=arg,)
        MYTHREAD.start()
    def stop(self):
        #this is unfortunately marked as impossible at this time
        pass
    def sleep_for(self, duration, units=MSEC):
        #this is also unfortunately marked as impossible as well
        pass
class Event:
    def __call__(self, callback, *arg):
        self.iteration = 0
        self.myevent = threading.Thread(target=callback, args=arg, name=str(self.iteration))
    def __init__(self, callback=None, *arg):
        if not callback == None:
            self.myevent = threading.Thread(target=callback, args=arg, name=str(self.iteration))
    def set(self, callback, *arg):
        self.myevent = threading.Thread(target=callback, args=arg, name=str(self.iteration))
    def broadcast(self):
        self.myevent.start()
        self.iteration += 1
        self.myevent = threading.Thread(target=self.myevent._target, args=self.myevent._args, name=str(self.iteration))
    def broadcast_and_wait():
        self.myevent.start()
        self.myevent.join()
        self.iteration += 1
        self.myevent = threading.Thread(target=self.myevent._target, args=self.myevent._args, name=str(self.iteration))

class Brain:
    def __init__(self):
        self.battery = Battery()
        self.timer = timer()
        self.screen = Screen()
        self.sdcard = Sdcard()
        self.three_wire_port = ThreeWirePort()
    def program_stop(self):
        pygame.quit()

class Battery:
    def capacity(self):
        return(100)
    def temperature(self, units=TemperatureUnits.CELSIUS):
        return(units)
    def voltage(self, units=MV):
        return(units)
    def current(self, units=20000):
        return(units)

class timer:
    def time(self, units=MSEC):
        return(((pygame.time.get_ticks() - timeBench) / 1000) * units)
    def clear(self):
        global timeBench
        timeBench = pygame.time.get_ticks()
    def reset(self):
        global timeBench
        timeBench = pygame.time.get_ticks()
    def system(self):
        return(round(time.time() * 100))
    def system_high_res(self):
        return(round(time.time() * 1000))
    def event(self, callback, delay, *arg):
        pygame.time.set_timer(pygame.event.Event(pygame.USEREVENT + len(callbackList), {'tag': delay}), delay, loops=1)
        tag = 'timer'
        tag += str(delay)
        callbackList.append([callback, *arg, tag])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
        
class Screen:
    def __init__(self):
        self.currentPenWidth = 1
        self.currentPenColor = (255, 255, 255)
        self.currentFillColor = (0, 0, 0)
    def print(self, *text, sep=" ", precision=2):
        global brainCursor
        printme = ''
        for arg in text:
            if (type(arg) is float) or (type(arg) is int):
                printme += str(f"{arg:.{precision}f}")
            else:
                printme += arg
            printme += sep
        printme = printme[:(len(printme) - len(sep))]
        if currentFont > 0:
            text_surface = NotoMono.render(printme, False, self.currentPenColor)
        else:
            text_surface = NotoSans.render(printme, False, self.currentPenColor)
        brainScreen.blit(text_surface, ((brainCursor[1] - 1) * (currentFont * 0.60) * sizeMultiplier,(brainCursor[0] - 1) * currentFont * sizeMultiplier))
        brainCursor[1] += (len(printme))
    def print_at(self, *text, x=0, y=0, sep=" ", precision=2, opaque=True):
        printme = ''
        for arg in text:
            if (type(arg) is float) or (type(arg) is int):
                printme += str(f"{arg:.{precision}f}")
            else:
                printme += arg
            printme += sep
        printme = printme[:(len(printme) - len(sep))]
        if currentFont > 0:
            text_surface = NotoMono.render(printme, False, self.currentPenColor)
        else:
            text_surface = NotoSans.render(printme, False, self.currentPenColor)
        if opaque == True:
            pygame.draw.rect(brainScreen, self.currentFillColor, (x * sizeMultiplier,(y - currentFont) * sizeMultiplier,NotoMono.size(printme)[0],(currentFont * sizeMultiplier) - (1 * sizeMultiplier)))
        brainScreen.blit(text_surface, (x * sizeMultiplier,(y - currentFont) * sizeMultiplier))
    def set_cursor(self, x, y):
        global brainCursor
        brainCursor = [x,y]
    def set_origin(self, x, y):
        global xOffset
        global yOffset
        xOffset = x
        yOffset = y
    def set_font(self, fontname):
        global currentFont
        global NotoMono
        global NotoSans
        if fontname > 0:
          NotoMono = pygame.font.Font('NotoMono-Regular.ttf',abs(fontname) * sizeMultiplier)
        else:
          NotoSans = pygame.font.Font('NotoSans-Regular.ttf',abs(fontname) * sizeMultiplier)
        currentFont = fontname
    def set_pen_width(self, width):
        self.currentPenWidth = 1
        if width >= 1:
            self.currentPenWidth = width
    def set_pen_color(self, color):
        self.currentPenColor = color
    def set_fill_color(self, color):
        self.currentFillColor = color
    def column(self):
      return(brainCursor[1])
    def row(self):
      return(brainCursor[0])
    def get_string_width(self, string):
      if currentFont > 0:
        return(NotoMono.size(string)[0])
      else:
        return(NotoSans.size(string)[0])
    def get_string_height(self, string):
      if currentFont > 0:
        return(NotoMono.size(string)[1])
      else:
        return(NotoSans.size(string)[1])
    def clear_screen(self, color=(0,0,0)):
        brainScreen.fill(color)
    def clear_line(self, row=brainCursor[0], color=(0,0,0)):
        pygame.draw.rect(brainScreen, color, (0,((row * currentFont) - currentFont) * sizeMultiplier,480 * sizeMultiplier,currentFont * sizeMultiplier))
    def clear_row(self):
        pygame.draw.rect(brainScreen, color, (0,((row * currentFont) - currentFont) * sizeMultiplier,480 * sizeMultiplier,currentFont * sizeMultiplier))
    def new_line(self):
        global brainCursor
        brainCursor = [brainCursor[0] + 1, 1]
    def next_row(self):
        global brainCursor
        brainCursor = [brainCursor[0] + 1, 1]
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def x_position(self):
        global brainX
        if pygame.mouse.get_pressed()[0] == True and round(pygame.mouse.get_pos()[0] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[0] / sizeMultiplier) <= 480 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) <= 240:
            brainX = round(pygame.mouse.get_pos()[0] / sizeMultiplier)
        return(brainX)
    def y_position(self):
        global brainY
        if pygame.mouse.get_pressed()[0] == True and round(pygame.mouse.get_pos()[1] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) <= 240 and round(pygame.mouse.get_pos()[0] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[0] / sizeMultiplier) <= 480:
            brainY = round(pygame.mouse.get_pos()[1] / sizeMultiplier)
        return(brainY)
    def pressing(self):
        return(pygame.mouse.get_pressed()[0] == True and round(pygame.mouse.get_pos()[0] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[0] / sizeMultiplier) <= 480 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) <= 240)
        #return(pygame.mouse.get_pressed()[0])
    def draw_pixel(self, x, y):
        pygame.draw.rect(brainScreen, self.currentPenColor, (x * sizeMultiplier, y * sizeMultiplier, 1 * sizeMultiplier, 1 * sizeMultiplier))
    def draw_line(self, x1, y1, x2, y2):
        pygame.draw.line(brainScreen, self.currentPenColor, (x1 * sizeMultiplier, y1 * sizeMultiplier), (x2 * sizeMultiplier, y2 * sizeMultiplier), self.currentPenWidth)
        #p1v = pygame.math.Vector2(x1 * sizeMultiplier, y1 * sizeMultiplier)
        #p2v = pygame.math.Vector2(x2 * sizeMultiplier, y2 * sizeMultiplier)
        #lv = (p2v - p1v).normalize()
        #lnv = pygame.math.Vector2(-lv.y, lv.x) * self.currentPenWidth // 2
        #pts = [p1v + lnv, p2v + lnv, p2v - lnv, p1v - lnv]
        #pygame.draw.polygon(brainScreen, self.currentPenColor, pts)
        pygame.draw.circle(brainScreen, self.currentPenColor, (x1 * sizeMultiplier, y1 * sizeMultiplier), round(self.currentPenWidth / 3))
        pygame.draw.circle(brainScreen, self.currentPenColor, (x2 * sizeMultiplier, y2 * sizeMultiplier), round(self.currentPenWidth / 3))


#these following commands may be wrong, because pygame draws outlines inside the thing. We'll test that in person
    def draw_rectangle(self, x, y, width, height, color=None):
        if color == None:
            color = self.currentFillColor
        rectangle = pygame.Surface((480 * sizeMultiplier, 240 * sizeMultiplier),pygame.SRCALPHA)
        pygame.draw.rect(rectangle, color, (x * sizeMultiplier, y * sizeMultiplier, width * sizeMultiplier, height * sizeMultiplier))
        pygame.draw.rect(rectangle, self.currentPenColor, ((x - (self.currentPenWidth * 0.5)) * sizeMultiplier, (y - (self.currentPenWidth * 0.5)) * sizeMultiplier, (width + self.currentPenWidth) * sizeMultiplier, (height + self.currentPenWidth) * sizeMultiplier), self.currentPenWidth)
        brainScreen.blit(rectangle, (0, 0))
    def draw_circle(self, x, y, radius, color=None):
        if color == None:
            color = self.currentFillColor
        circle = pygame.Surface((480 * sizeMultiplier, 240 * sizeMultiplier),pygame.SRCALPHA)
        pygame.draw.circle(circle, color, (x * sizeMultiplier, y * sizeMultiplier), radius * sizeMultiplier)
        pygame.draw.circle(circle, self.currentPenColor, (x * sizeMultiplier, y * sizeMultiplier), (radius + (self.currentPenWidth * 0.5)) * sizeMultiplier, self.currentPenWidth)
        brainScreen.blit(circle, (0, 0))
    def draw_image_from_file(self, filename, x, y):
        brainScreen.blit(pygame.image.load(filename), (x * sizeMultiplier,y * sizeMultiplier))
    def render(self):
        global renderMode
        renderMode = True
        pygame.time.wait(16)
        screen.blit(brainScreen, (xOffset, yOffset))
        return(True)
    def set_clip_region(self, x, y, width, height):
        print('yeah bro idk what this does either someone please help me')
     
class Sdcard:
    pass

class ThreeWirePort:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        self.c = 'c'
        self.d = 'd'
        self.e = 'e'
        self.f = 'f'
        self.g = 'g'
        self.h = 'h'

class Controller:
    #(75, 70, 60)
    def __init__(self, role=PRIMARY):
        size = [480,240 + (64 * 2)]
        screen = pygame.display.set_mode([size[0] * sizeMultiplier, size[1] * sizeMultiplier])
        pygame.draw.rect(screen, (245, 255, 255), (0, 240 * sizeMultiplier, 128 * 2 * sizeMultiplier, 64 * 2 * sizeMultiplier))
        pygame.draw.rect(screen, (75, 70, 60), (1 * sizeMultiplier, 241 * sizeMultiplier, 127 * 2 * sizeMultiplier, 15 * 2 * sizeMultiplier))
        pygame.draw.rect(screen, (75, 70, 60), (1 * sizeMultiplier, 273 * sizeMultiplier, 127 * 2 * sizeMultiplier, 30 * 2 * sizeMultiplier), 3)
        self.axis1 = Axis1()
        self.axis2 = Axis2()
        self.axis3 = Axis3()
        self.axis4 = Axis4()
        self.buttonA = ButtonA()
        self.buttonB = ButtonB()
        self.buttonX = ButtonX()
        self.buttonY = ButtonY()
        self.buttonDown = ButtonDown()
        self.buttonUp = ButtonUp()
        self.buttonLeft = ButtonLeft()
        self.buttonRight = ButtonRight()
        self.buttonL1 = ButtonL1()
        self.buttonL2 = ButtonL2()
        self.buttonR1 = ButtonR1()
        self.buttonR2 = ButtonR2()
        self.screen = ControllerScreen()
        
    def rumble(self, pattern):
        rumblePattern = ''
        for i in range(len(pattern)):
            if pattern[i] == '.':
                rumblePattern += 'short '
            if pattern[i] == '-':
                rumblePattern += 'long '
        rumblePattern = rumblePattern.rstrip(' ')
        if len(rumblePattern) > 0:
            print(f'Controller rumbled:   {rumblePattern}')
        
class Axis1:
    def position(self):
        return round(j.get_axis(2) * 100)
    def changed(self, callback, *arg):
        callbackList.append([callback, *arg, 'changed2'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
class Axis2:
    def position(self):
        return round(j.get_axis(3) * 100)
    def changed(self, callback, *arg):
        callbackList.append([callback, *arg, 'changed3'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
class Axis3:
    def position(self):
        return round(j.get_axis(1) * 100)
    def changed(self, callback, *arg):
        callbackList.append([callback, *arg, 'changed1'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
class Axis4:
    def position(self):
        return round(j.get_axis(0) * 100)
    def changed(self, callback, *arg):
        callbackList.append([callback, *arg, 'changed4'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
class ButtonA:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed1'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released1'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_button(1)
class ButtonB:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed0'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released0'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_button(0)
class ButtonX:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed3'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released3'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_button(3)
class ButtonY:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed2'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released2'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_button(2)
class ButtonDown:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed8'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released8'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_hat(0)[1] == -1
class ButtonUp:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed9'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released9'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_hat(0)[1] == 1
class ButtonLeft:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed10'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released10'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_hat(0)[0] == -1
class ButtonRight:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed11'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released11'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_hat(0)[0] == 1
class ButtonL1:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed4'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released4'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_button(4)
class ButtonL2:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed6'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released6'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return (j.get_axis(4) > 0)
        print(j.get_axis(4) > 0)
class ButtonR1:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed5'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released5'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return j.get_button(5)
class ButtonR2:
    def pressed(self, callback, *arg):
        callbackList.append([callback, *arg, 'pressed7'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        callbackList.append([callback, *arg, 'released7'])
        if not arg:
            callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        return (j.get_axis(5) > 0)

class ControllerScreen:
    def print(self, *text, sep=" ", precision=2):
        global controllerCursor
        printme = ''
        for arg in text:
            if (type(arg) is float) or (type(arg) is int):
                printme += str(f"{arg:.{precision}f}")
            else:
                printme += arg
            printme += sep
        printme = printme[:(len(printme) - len(sep))]
        screen.blit(NotoSansController.render(printme, False, (75, 70, 60)), (((controllerCursor[1] - 1) * 16 * sizeMultiplier),((controllerCursor[0] + controllerCursorOffset - 0.3) * 32 * sizeMultiplier) + (240 * sizeMultiplier)))
        controllerCursor = [controllerCursor[0], controllerCursor[1] + (NotoSansController.size(printme)[0] / 16)]
    def set_cursor(self, row, col):
        global controllerCursor
        controllerCursor = [row, col]
    def column(self):
        return(round(controllerCursor[1]))
    def row(self):
        return(controllerCursor[0])
    def clear_screen(self):
        global controllerCursorOffset
        pygame.draw.rect(screen, (245, 255, 255), (0, 240 * sizeMultiplier, 128 * 2 * sizeMultiplier, 64 * 2 * sizeMultiplier))
        pygame.draw.rect(screen, (75, 70, 60), (1 * sizeMultiplier, 241 * sizeMultiplier, 127 * 2 * sizeMultiplier, 15 * 2 * sizeMultiplier))
        controllerCursorOffset = 0
    def clear_row(self, row=None):
        if row == None:
            row = controllerCursor[0]
        row += controllerCursorOffset
        #pygame.draw.rect(screen, (245, 255, 255), (0, ((controllerCursor[0]) * 8 * sizeMultiplier) + (240 * sizeMultiplier), 128 * 2 * sizeMultiplier, 64 * 2 * sizeMultiplier))
        pygame.draw.rect(screen, (245, 255, 255), (0, ((controllerCursor[0] + controllerCursorOffset) * sizeMultiplier * 16 * 2) + (240 * sizeMultiplier), 128 * 2 * sizeMultiplier, 64 * 2 * sizeMultiplier))
    def next_row(self):
        global controllerCursor
        controllerCursor = [controllerCursor[0] + 1, 1]

class Motor:
    def __init__(self, port, gear, reverse=1):
        self.CURRENTSPEED = 0
        self.CURRENTPOS = 0
        self.CURRENTVELOCITY = 0
        self.reverse = reverse
        self.brake = 1
        self.gear = gear
        self.port = port
        self.timeout = 0
        self.maxtorque = 100
    def spin(self, direction, velocity=None, units=RPM):
        if velocity == None:
            velocity = self.CURRENTVELOCITY
        if units == 1:
            self.CURRENTSPEED = velocity * direction * self.reverse
        else:
            self.CURRENTSPEED = velocity * (3600 / self.gear) * direction * self.reverse
    def spin_to_position(self, rotation, units=DEGREES, velocity=None, units_v=None, wait=True):
        #DO THE THING HERE IT JUST HAS TO BE A WAIT COMMAND THAT CALCULATES HOW LONG ITLL TAKE
        if velocity == None:
            velocity = self.CURRENTVELOCITY
        if units_v == None:
            units_v = RPM
        if wait == True:
            pass
            #pygame.time.wait(round((rotation * units) / (velocity * units_v) * 1000))
        self.CURRENTPOS = rotation * units
    def spin_for(self, direction, value, units=DEGREES, velocity=None, units_v=None, wait=True):
        #AND WAIT HERE TOO
        if velocity == None:
            velocity = self.CURRENTVELOCITY
        if units_v == None:
            units_v = RPM
        if wait == True:
            pass
            #pygame.time.wait(round((value * units) / (velocity * units_v) * 1000))
        self.CURRENTPOS = direction * value * units * self.reverse
    def stop(self):
        self.CURRENTSPEED = 0
    def set_velocity(self, velocity, units=None):
        if not units == None:
            velocity *= (3600 / self.gear)
        self.CURRENTVELOCITY = velocity
    def set_reversed(self, value):
        if value == True:
            self.reverse = -1
        else:
            self.reverse = 1
    def set_stopping(self, mode=COAST):
        self.brake = mode
    def reset_position(self):
        self.CURRENTPOS = 0
    def set_position(self, value, units=DEGREES):
        self.CURRENTPOS = value * units
    def set_timeout(self, value, units=MSEC):
        self.timeout = (value * 1000) / units
    def get_timeout(self):
        return(self.timeout)
    def is_spinning(self):
        return(not self.CURRENTSPEED == 0)
    def is_done(self):
        return(self.CURRENTSPEED == 0)
    def set_max_torque(self, value, units):
        self.maxtorque = value * units
    def direction(self):
        if self.CURRENTSPEED >= 0:
            return(FORWARD)
        else:
            return(REVERSE)
    def position(self, units=DEGREES):
        return(self.CURRENTPOS / units)
    def velocity(self, units=RPM):
        return(self.CURRENTSPEED / units)
    def current(self):
        return(100)
    def power(self):
        return(100)
    def torque(self, units=1):
        return(self.maxtorque / units)
    def efficiency(self):
        return(100)
    def temperature(self, units=1):
        return(40)
    def command(self):
        return(self.CURRENTVELOCITY / units)
    def installed(self):
        return(True)
    def timestamp(self):
        return(0)

class MotorGroup:
    def __init__(self, *ports):
        self.CURRENTSPEED = 0
        self.CURRENTPOS = 0
        self.CURRENTVELOCITY = 0
        self.reverse = 1
        self.brake = 1
        self.gear = 18
        self.timeout = 0
        self.maxtorque = 100
    def spin(self, direction, velocity=None, units=RPM):
        if velocity == None:
            velocity = self.CURRENTVELOCITY
        if units == 1:
            self.CURRENTSPEED = velocity * direction
        else:
            self.CURRENTSPEED = velocity * (3600 / self.gear) * direction * self.reverse
    def spin_to_position(self, rotation, units=DEGREES, velocity=None, units_v=None, wait=True):
        #DO THE THING HERE IT JUST HAS TO BE A WAIT COMMAND THAT CALCULATES HOW LONG ITLL TAKE
        if velocity == None:
            velocity = self.CURRENTVELOCITY
        if units_v == None:
            units_v = RPM
        if wait == True:
            pass
            #pygame.time.wait(round((rotation * units) / (velocity * units_v) * 1000))
        self.CURRENTPOS = rotation * units
    def spin_for(self, direction, value, units=DEGREES, velocity=None, units_v=None, wait=True):
        #AND WAIT HERE TOO
        if velocity == None:
            velocity = self.CURRENTVELOCITY
        if units_v == None:
            units_v = RPM
        if wait == True:
            pass
            #pygame.time.wait(round((value * units) / (velocity * units_v) * 1000))
        self.CURRENTPOS = direction * value * units * self.reverse
    def stop(self):
        self.CURRENTSPEED = 0
    def set_velocity(self, velocity, units=None):
        if units == None:
            velocity *= (3600 / self.gear)
        self.CURRENTVELOCITY = velocity
    def set_reversed(self, value):
        if value == True:
            self.reverse = -1
        else:
            self.reverse = 1
    def set_stopping(self, mode=COAST):
        self.brake = mode
    def reset_position(self):
        self.CURRENTPOS = 0
    def set_position(self, value, units=DEGREES):
        self.CURRENTPOS = value * units
    def set_timeout(self, value, units=MSEC):
        self.timeout = (value * 1000) / units
    def get_timeout(self):
        return(self.timeout)
    def is_spinning(self):
        return(not self.CURRENTSPEED == 0)
    def is_done(self):
        return(self.CURRENTSPEED == 0)
    def set_max_torque(self, value, units):
        self.maxtorque = value * units
    def direction(self):
        if self.CURRENTSPEED >= 0:
            return(FORWARD)
        else:
            return(REVERSE)
    def position(self, units=DEGREES):
        return(self.CURRENTPOS / units)
    def velocity(self, units=RPM):
        return(self.CURRENTSPEED / units)
    def current(self):
        return(100)
    def power(self):
        return(100)
    def torque(self, units=1):
        return(self.maxtorque / units)
    def efficiency(self):
        return(100)
    def temperature(self, units=1):
        return(40)
    def command(self):
        return(self.CURRENTVELOCITY / units)
    def installed(self):
        return(True)
    def timestamp(self):
        return(0)
    
class DigitalOut:
    def __init__(self, port):
        pass
    def set(self, value):
        pass

class Potentiometer:
    def __init__(self, port):
        pass
    def angle(self, units):
        return(0)
    def changed(self, callback, *arg):
        pass

class Bumper:
    def __init__(self, port, ADMINNUMBERBUTTON=None):
        self.BUMPERBUTTON = ADMINNUMBERBUTTON
    def pressed(self, callback, *arg):
        if not self.BUMPERBUTTON == None:
            callbackList.append([callback, *arg, ('pressed' + str(16 + self.BUMPERBUTTON))])
            if not arg:
                callbackList[(len(callbackList) - 1)].insert(1, ())
    def released(self, callback, *arg):
        if not self.BUMPERBUTTON == None:
            callbackList.append([callback, *arg, ('released' + str(16 + self.BUMPERBUTTON))])
            if not arg:
                callbackList[(len(callbackList) - 1)].insert(1, ())
    def pressing(self):
        if not self.BUMPERBUTTON == None:
            return(pygame.key.get_pressed()[keyboardTranslation[16 + self.BUMPERBUTTON]])
        else:
            return(False)
    

class Competition:
    def __init__(self, callback1, callback2):
        callbackList.append([callback1, (), 'DRIVER'])
        callbackList.append([callback2, (), 'AUTONOMOUS'])
    def is_enabled(self):
        global competitionMode
        return not competitionMode == 0
    def is_driver_control(self):
        global competitionMode
        return (competitionMode == 1)
    def is_autonomous(self):
        global competitionMode
        return (competitionMode == -1)
    def is_competition_switch(self):
        return False
    def is_field_control(self):
        return False




        


def initiateVexSimulator():
    global competitionMode, brainX, brainY
    pygame.display.set_caption(Path(__main__.__file__).stem + ' - INITIATED')
    if competitionMode == 1:
        pygame.display.set_caption(Path(__main__.__file__).stem + ' - INITIATED - DRIVER')
    elif competitionMode == -1:
        pygame.display.set_caption(Path(__main__.__file__).stem + ' - INITIATED - AUTONOMOUS')
    for i in range(len(callbackList)):
        if callbackList[i - 1][2] == 'DRIVER':
            threading.Thread(target=callbackList[i - 1][0]).start()
    while True:
        if competitionMode == 1:
            pygame.display.set_caption(Path(__main__.__file__).stem + ' - INITIATED - DRIVER')
        elif competitionMode == -1:
            pygame.display.set_caption(Path(__main__.__file__).stem + ' - INITIATED - AUTONOMOUS')
        if not renderMode:
            screen.blit(brainScreen, (xOffset,yOffset))
        pygame.display.flip()
        clock.tick(60)
        joystickHat = [j.get_hat(0)[0], j.get_hat(0)[1]]
        joystickTriggers = [j.get_axis(4), j.get_axis(5)]
        if pygame.mouse.get_pressed()[0] == True and round(pygame.mouse.get_pos()[0] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[0] / sizeMultiplier) <= 480 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) <= 240:
            brainX = round(pygame.mouse.get_pos()[0] / sizeMultiplier)
        if pygame.mouse.get_pressed()[0] == True and round(pygame.mouse.get_pos()[1] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[1] / sizeMultiplier) <= 240 and round(pygame.mouse.get_pos()[0] / sizeMultiplier) >= 0 and round(pygame.mouse.get_pos()[0] / sizeMultiplier) <= 480:
            brainY = round(pygame.mouse.get_pos()[1] / sizeMultiplier)
        for event in pygame.event.get():
            if event.type in range(32866, 32866 + 32667):
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2][:5] == 'timer':
                        if event.tag == int(callbackList[i - 1][2][5:]):
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2] == 'pressed':
                        threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2] == 'released':
                        threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2][:7] == 'pressed' and not callbackList[i - 1][2][7:] == '':
                        if int(callbackList[i - 1][2][7:]) == event.button:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                    if callbackList[i - 1][2] == 'DRIVER' and event.button == 6:
                            threading.Thread(target=callbackList[i - 1][0]).start()
                            #callbackList[i - 1][0]()
                            competitionMode = 1
                    if callbackList[i - 1][2] == 'AUTONOMOUS' and event.button == 7:
                            threading.Thread(target=callbackList[i - 1][0]).start()
                            #callbackList[i - 1][0]()
                            competitionMode = -1
            if event.type == pygame.JOYBUTTONUP:
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2][:8] == 'released' and not callbackList[i - 1][2][8:] == '':
                        if int(callbackList[i - 1][2][8:]) == event.button:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
            if event.type == pygame.JOYAXISMOTION:
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2][:7] == 'changed' and not callbackList[i - 1][2][7:] == '':
                        if int(callbackList[i - 1][2][7:]) == event.axis:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                    elif callbackList[i - 1][2][:7] == 'pressed' and not callbackList[i - 1][2][7:] == '':
                        if int(callbackList[i - 1][2][7:]) == 6 and event.axis == 4:
                            if  j.get_axis(4) > 0 and not joystickTriggers[0] > 0 :
                                threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][7:]) == 7 and event.axis == 5:
                            if  j.get_axis(5) > 0 and not joystickTriggers[1] > 0 :
                                threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                    elif callbackList[i - 1][2][:8] == 'released' and not callbackList[i - 1][2][8:] == '':
                        if int(callbackList[i - 1][2][8:]) == 6 and event.axis == 4:
                            if  j.get_axis(4) < 0 and not joystickTriggers[0] < 0:
                                threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][8:]) == 7 and event.axis == 5:
                            if  j.get_axis(5) < 0 and not joystickTriggers[1] < 0:
                                threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
            if event.type == pygame.JOYHATMOTION:
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2][:7] == 'pressed' and not callbackList[i - 1][2][7:] == '':
                        if int(callbackList[i - 1][2][7:]) == 8 and j.get_hat(0)[1] == -1 and not joystickHat[1] == -1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][7:]) == 9 and j.get_hat(0)[1] == 1 and not joystickHat[1] == 1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][7:]) == 10 and j.get_hat(0)[0] == -1 and not joystickHat[0] == -1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][7:]) == 11 and j.get_hat(0)[0] == 1 and not joystickHat[0] == 1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                    elif callbackList[i - 1][2][:8] == 'released' and not callbackList[i - 1][2][8:] == '':
                        if int(callbackList[i - 1][2][8:]) == 8 and j.get_hat(0)[1] == 0 and joystickHat[1] == -1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][8:]) == 9 and j.get_hat(0)[1] == 0 and joystickHat[1] == 1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][8:]) == 10 and j.get_hat(0)[0] == 0 and joystickHat[0] == -1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                        if int(callbackList[i - 1][2][8:]) == 11 and j.get_hat(0)[0] == 0 and joystickHat[0] == 1:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
            if event.type == pygame.KEYDOWN:
                for i in range(len(callbackList)):
                    if callbackList[i - 1][2][:7] == 'pressed' and not callbackList[i - 1][2][7:] == '':
                        if keyboardTranslation[int(callbackList[i - 1][2][7:])] == event.key:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                    if callbackList[i - 1][2][:7] == 'changed' and not callbackList[i - 1][2][7:] == '':
                        if keyboardTranslation[int(callbackList[i - 1][2][7:]) + 10][0] == event.key or keyboardTranslation[int(callbackList[i - 1][2][7:]) + 10][1] == event.key:
                            threading.Thread(target=callbackList[i - 1][0], args=(callbackList[i - 1][1])).start()
                    if callbackList[i - 1][2] == 'DRIVER' and event.key == 44:
                        threading.Thread(target=callbackList[i - 1][0]).start()
                        #callbackList[i - 1][0]()
                        competitionMode = 1
                    if callbackList[i - 1][2] == 'AUTONOMOUS' and event.key == 46:
                        threading.Thread(target=callbackList[i - 1][0]).start()
                        #callbackList[i - 1][0]()
                        competitionMode = -1
            if event.type == 256:
                pygame.quit()

