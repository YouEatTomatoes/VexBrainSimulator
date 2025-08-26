# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
size = [480,240]
sizeMultiplier = 1.5
pygame.init()
pygame.event.get()
pygame.font.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
joysticksReconnected = 0
if len(joysticks) > 0:
  joysticksReconnected = 1
  j = joysticks[0]
  print('joystick connected!')
  wantJoystick = True
else:
  print('no joystick :(')
  wantJoystick = False
  class j:
    def get_hat(int):
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
    def get_button(int):
      if (int == 0):
        return (pygame.key.get_pressed()[pygame.K_b])
      if (int == 1):
        return (pygame.key.get_pressed()[pygame.K_a])
      if (int == 2):
        return (pygame.key.get_pressed()[pygame.K_y])
      if (int == 3):
        return (pygame.key.get_pressed()[pygame.K_x])
      if (int == 4):
        return (pygame.key.get_pressed()[pygame.K_SEMICOLON])
      if (int == 5):
        return (pygame.key.get_pressed()[pygame.K_QUOTE])
      if (int == 6):
        return (pygame.key.get_pressed()[pygame.K_COMMA])
      if (int == 7):
        return (pygame.key.get_pressed()[pygame.K_PERIOD])
    def get_axis(int):
      #if (int < 3.1):
        #return (0)
      if (int == 0):
        if (pygame.key.get_pressed()[pygame.K_d]):
          return (-1.00)
        elif (pygame.key.get_pressed()[pygame.K_g]):
          return (1.00)
        else:
          return (0)
      if (int == 1):
        if (pygame.key.get_pressed()[pygame.K_r]):
          return (-1.00)
        elif (pygame.key.get_pressed()[pygame.K_f]):
          return (1.00)
        else:
          return (0)
      if (int == 2):
        if (pygame.key.get_pressed()[pygame.K_j]):
          return (-1.00)
        elif (pygame.key.get_pressed()[pygame.K_l]):
          return (1.00)
        else:
          return (0)
      if (int == 3):
        if (pygame.key.get_pressed()[pygame.K_i]):
          return (-1.00)
        elif (pygame.key.get_pressed()[pygame.K_k]):
          return (1.00)
        else:
          return (0)
      if (int == 4):
        if (pygame.key.get_pressed()[pygame.K_LEFTBRACKET]):
          return (0.5)
        else:
          return (-0.5)
      if (int == 5):
        if (pygame.key.get_pressed()[pygame.K_RIGHTBRACKET]):
          return (0.5)
        else:
          return (-0.5)
screen = pygame.display.set_mode([size[0] * sizeMultiplier, size[1] * sizeMultiplier])
brainCursor = [1,1]
controllerCursor = [1,1]
controllerScreen = pygame.Surface((128, 64))
brainScreen = pygame.Surface((480 * sizeMultiplier, 240 * sizeMultiplier))
renderCalled = False
pygame.display.set_caption("vexV5 Simulator")
clock = pygame.time.Clock()
running = True
brainPos = ((0, 0))
brainCursor = ((1, 1))
controllerCursor = ((1, 1))
timer = 0
timerBench = 0
oldHat = j.get_hat(0)
oldButton = [j.get_button(0), j.get_button(1), j.get_button(2), j.get_button(3), j.get_button(4), j.get_button(5)]
oldL2 = False
oldR2 = False
oldAxis = [j.get_axis(2), j.get_axis(3), j.get_axis(1), j.get_axis(0)]
oldMouse = pygame.mouse.get_pressed()[0]
fontnum = 20

#GAME EVENT HANDLER
xPos = 240
yPos = 120
dx = 0
dy = 0

#define wait
MSEC = 'MSEC'
SECONDS = 'SECONDS'
def wait(number, timeType):
    if timeType == 'MSEC':
        pygame.time.wait(number)
    if timeType == 'SECONDS':
        pygame.time.wait(number * 1000)

'''
def backgroundPREPARE(chosenColor):
    screen.fill(chosenColor)

def backgroundDISPLAY():
    pygame.display.flip()
'''

#brain setup
class Brain:
    def __init__(self):
        self.timer = vexbrainTIMER()
        self.screen = vexbrainSCREEN()
        self.battery = vexbrainBATTERY()

    def program_stop(self):
        pygame.quit()

class color:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.ORANGE = (255, 165, 0)
        self.PURPLE = (128, 0, 128)
        self.CYAN = (0, 255, 255)
        self.TRANSPARENT = (0, 0, 0, 0)

Color = color()

class fonts:
  def __init__(self):
    self.MONO12 = 12
    self.MONO15 = 15
    self.MONO20 = 20
    self.MONO30 = 30
    self.MONO40 = 40
    self.MONO60 = 60
    self.PROP20 = -20
    self.PROP30 = -30
    self.PROP40 = -40
    self.PROP60 = -60

FontType = fonts()

class vexbrainSCREEN:
    def render(self):
        global renderCalled
        if renderCalled:
          screen.blit(brainScreen, (0,0))
        else:
          brainScreen.fill((0,0,0))
          renderCalled = True
    def set_fill_color(self, fill):
        global fillColor
        fillColor = fill
    def set_pen_width(self, width):
        global penWidth
        penWidth = width
    def set_pen_color(self, color):
        global penColor
        penColor = color
    def draw_line(self, x, y, x2, y2):
        pygame.draw.line(brainScreen, penColor, (x * sizeMultiplier, y * sizeMultiplier), (x2 * sizeMultiplier, y2 * sizeMultiplier), penWidth)
    def draw_rectangle(self, x, y, w, h):
        pygame.draw.rect(brainScreen, penColor, ((x * sizeMultiplier) - (penWidth * sizeMultiplier), (y * sizeMultiplier) - (penWidth * sizeMultiplier), (w * sizeMultiplier) + (penWidth * sizeMultiplier * 2), (h * sizeMultiplier) + (penWidth * sizeMultiplier * 2)))
        pygame.draw.rect(brainScreen, fillColor, (x * sizeMultiplier, y * sizeMultiplier, w * sizeMultiplier, h * sizeMultiplier))
    def draw_pixel(self, x, y):
        pygame.draw.rect(brainScreen, penColor, (x * sizeMultiplier, y * sizeMultiplier, 1, 1))
    def draw_circle(self, x, y, r):
        pygame.draw.circle(brainScreen, penColor, (x * sizeMultiplier, y * sizeMultiplier), (r * sizeMultiplier) + (penWidth * sizeMultiplier))
        pygame.draw.circle(brainScreen, fillColor, (x * sizeMultiplier, y * sizeMultiplier), r * sizeMultiplier)
    def pressing(self):
        return(pygame.mouse.get_pressed()[0])
    def x_position(self):
        return(brainPos[0] / sizeMultiplier)
    def y_position(self):
        return(brainPos[1] / sizeMultiplier)


    def column(self):
      return(brainCursor[0])
    def row(self):
      return(brainCursor[1])
    def get_string_width(self, stringthing):
      if fontnum > 0:
        return(NotoMono.size(stringthing)[0])
      else:
        return(NotoSans.size(stringthing)[0])
    def get_string_height(self, stringthing):
      if fontnum > 0:
        return(NotoMono.size(stringthing)[1])
      else:
        return(NotoSans.size(stringthing)[1])
    def set_font(self, fontname):
        global fontnum
        global NotoMono
        global NotoSans
        if fontname > 0:
          NotoMono = pygame.font.Font('NotoMono-Regular.ttf',abs(fontname))
        else:
          NotoSans = pygame.font.Font('NotoSans-Regular.ttf',abs(fontname))
        fontnum = fontname
    def print(self, whatWeDoin, precision=6):
        if fontnum > 0:
          text_surface = NotoMono.render(whatWeDoin, False, penColor)
        else:
          text_surface = NotoSans.render(whatWeDoin, False, penColor)
        brainScreen.blit(text_surface, ((brainCursor[0] - 1),(brainCursor[1] - 1)))
        


class vexbrainTIMER:
    def clear(self):
        timerBench = pygame.time.get_ticks()
    def time(self, timeType):
        if timeType == 'MSEC':
            return(time - timeBench)
        if timeType == 'SECONDS':
            return((time - timeBench) * 1000)
           
VOLT = 14.4
class CurrentUnits:
  def AMP(self):
    return(20.0)
class vexbrainBATTERY:
  def voltage(self, VoltAge):
    return(VoltAge)
  def current(self, currentness):
    return(currentness)
  def capacity(self):
    return(100)
  def temperature(self):
    return(100)


driver_control = 29
autonomous = 30
def Competition(driver_control, autonomous):
    #im not really sure what this is supposed to do but i dont want it to break lol
    return(driver_control + autonomous)
brain = Brain()

class vexCONTROLLER:
  def __init__(self):
    self.axis1 = vexAxis1()
    self.axis2 = vexAxis2()
    self.axis3 = vexAxis3()
    self.axis4 = vexAxis4()
    self.buttonUp = vexButtonUp()
    self.buttonDown = vexButtonDown()
    self.buttonLeft = vexButtonLeft()
    self.buttonRight = vexButtonRight()
    self.buttonA = vexButtonA()
    self.buttonB = vexButtonB()
    self.buttonX = vexButtonX()
    self.buttonY = vexButtonY()
    self.buttonL1 = vexButtonL1()
    self.buttonL2 = vexButtonL2()
    self.buttonR1 = vexButtonR1()
    self.buttonR2 = vexButtonR2()
    self.buttonADMINL = vexButtonAL()
    self.buttonADMINR = vexButtonAR()
class vexAxis1:
  def position(self):
    return j.get_axis(2) * 100
class vexAxis2:
  def position(self):
    return j.get_axis(3) * 100
class vexAxis3:
  def position(self):
    return j.get_axis(1) * 100
class vexAxis4:
  def position(self):
    return j.get_axis(0) * 100
class vexButtonUp:
  def pressing(self):
    if j.get_hat(0)[1] == 1:
      return True
    else:
      return False
class vexButtonDown:
  def pressing(self):
    if j.get_hat(0)[1] == -1:
      return True
    else:
      return False
class vexButtonLeft:
  def pressing(self):
    if j.get_hat(0)[0] == -1:
      return True
    else:
      return False
class vexButtonRight:
  def pressing(self):
    if j.get_hat(0)[0] == 1:
      return True
    else:
      return False
class vexButtonA:
  def pressing(self):
    return j.get_button(1)
class vexButtonB:
  def pressing(self):
    return j.get_button(0)
class vexButtonX:
  def pressing(self):
    return j.get_button(3)
class vexButtonY:
  def pressing(self):
    return j.get_button(2)
class vexButtonL1:
  def pressing(self):
    return j.get_button(4)
class vexButtonL2:
  def pressing(self):
    if j.get_axis(4) > 0:
      return True
    else:
      return False
class vexButtonR1:
  def pressing(self):
    return j.get_button(5)
class vexButtonR2:
  def pressing(self):
    if j.get_axis(5) > 0:
      return True
    else:
      return False
class vexButtonAL:
  def pressing(self):
    return j.get_button(6)
class vexButtonAR:
  def pressing(self):
    return j.get_button(7)

#some controller stuff
def onevent_controller_1buttonRight_pressed_0():
    pass
def onevent_controller_1buttonLeft_pressed_0():
    pass
def onevent_controller_1buttonUp_pressed_0():
    pass
def onevent_controller_1buttonDown_pressed_0():
    pass
def onevent_controller_1buttonA_pressed_0():
    pass
def onevent_controller_1buttonB_pressed_0():
    pass
def onevent_controller_1buttonX_pressed_0():
    pass
def onevent_controller_1buttonY_pressed_0():
    pass
def onevent_controller_1buttonL1_pressed_0():
    pass
def onevent_controller_1buttonL2_pressed_0():
    pass
def onevent_controller_1buttonR1_pressed_0():
    pass
def onevent_controller_1buttonR2_pressed_0():
    pass
def onevent_controller_1buttonRight_released_0():
    pass
def onevent_controller_1buttonLeft_released_0():
    pass
def onevent_controller_1buttonUp_released_0():
    pass
def onevent_controller_1buttonDown_released_0():
    pass
def onevent_controller_1buttonA_released_0():
    pass
def onevent_controller_1buttonB_released_0():
    pass
def onevent_controller_1buttonX_released_0():
    pass
def onevent_controller_1buttonY_released_0():
    pass
def onevent_controller_1buttonL1_released_0():
    pass
def onevent_controller_1buttonL2_released_0():
    pass
def onevent_controller_1buttonR1_released_0():
    pass
def onevent_controller_1buttonR2_released_0():
    pass
def onevent_controller_1axis1Changed_0():
    pass
def onevent_controller_1axis2Changed_0():
    pass
def onevent_controller_1axis3Changed_0():
    pass
def onevent_controller_1axis4Changed_0():
    pass
def onevent_brainScreen_pressed_0():
    pass
def onevent_brainScreen_released_0():
    pass

class Pneumatic1:
    def set(toggle):
        global isPneumatic1
        isPneumatic1 = toggle
class Pneumatic2:
    def set(toggle):
        global isPneumatic2
        isPneumatic2 = toggle
class Pneumatic3:
    def set(toggle):
        global isPneumatic3
        isPneumatic3 = toggle
class Pneumatic4:
    def set(toggle):
        global isPneumatic4
        isPneumatic4 = toggle

controller_1 = vexCONTROLLER()


#defaulting things
brain.timer.clear()
brain.screen.set_pen_width(1)
brain.screen.set_pen_color(Color.WHITE)
brain.screen.set_fill_color(Color.BLACK)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    #get input from user
    pressed = pygame.key.get_pressed()
    if pygame.mouse.get_pressed()[0]:
        brainPos = ((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
    
    if event.type == pygame.JOYHATMOTION or event.type == pygame.KEYDOWN  or event.type == pygame.KEYUP:
        if j.get_hat(0)[0] == 1 and oldHat[0] == 0:
            onevent_controller_1buttonRight_pressed_0()
        if j.get_hat(0)[0] == -1 and oldHat[0] == 0:
            onevent_controller_1buttonLeft_pressed_0()
        if j.get_hat(0)[1] == 1 and oldHat[1] == 0:
            onevent_controller_1buttonUp_pressed_0()
        if j.get_hat(0)[1] == -1 and oldHat[1] == 0:
            onevent_controller_1buttonDown_pressed_0()
       
        if j.get_hat(0)[0] == 0 and oldHat[0] == 1:
            onevent_controller_1buttonRight_released_0()
        if j.get_hat(0)[0] == 0 and oldHat[0] == -1:
            onevent_controller_1buttonLeft_released_0()
        if j.get_hat(0)[1] == 0 and oldHat[1] == 1:
            onevent_controller_1buttonUp_released_0()
        if j.get_hat(0)[1] == 0 and oldHat[1] == -1:
            onevent_controller_1buttonDown_released_0()

    if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.KEYDOWN:
        if j.get_button(1) and not oldButton[1]:
            onevent_controller_1buttonA_pressed_0()
        if j.get_button(0) and not oldButton[0]:
            onevent_controller_1buttonB_pressed_0()
        if j.get_button(2) and not oldButton[2]:
            onevent_controller_1buttonY_pressed_0()
        if j.get_button(3) and not oldButton[3]:
            onevent_controller_1buttonX_pressed_0()
        if j.get_button(4) and not oldButton[4]:
            onevent_controller_1buttonL1_pressed_0()
        if j.get_button(5) and not oldButton[5]:
            onevent_controller_1buttonR1_pressed_0()

    if event.type == pygame.JOYBUTTONUP or event.type == pygame.KEYUP:

        if oldButton[1] and not j.get_button(1):
            onevent_controller_1buttonA_released_0()
        if oldButton[0] and not j.get_button(0):
            onevent_controller_1buttonB_released_0()
        if oldButton[2] and not j.get_button(2):
            onevent_controller_1buttonY_released_0()
        if oldButton[3] and not j.get_button(3):
            onevent_controller_1buttonX_released_0()
        if oldButton[4] and not j.get_button(4):
            onevent_controller_1buttonL1_released_0()
        if oldButton[5] and not j.get_button(5):
            onevent_controller_1buttonR1_released_0()

    if event.type == pygame.JOYAXISMOTION:
        if controller_1.buttonL2.pressing() and not oldL2:
            onevent_controller_1buttonL2_pressed_0()
        if controller_1.buttonR2.pressing() and not oldR2:
            onevent_controller_1buttonR2_pressed_0()
        if oldL2 and not controller_1.buttonL2.pressing():
            onevent_controller_1buttonL2_released_0()
        if oldR2 and not controller_1.buttonR2.pressing():
            onevent_controller_1buttonR2_released_0()
        if not oldAxis[0] == j.get_axis(2):
            onevent_controller_1axis1Changed_0()
        if not oldAxis[1] == j.get_axis(3):
            onevent_controller_1axis2Changed_0()
        if not oldAxis[2] == j.get_axis(1):
            onevent_controller_1axis3Changed_0()
        if not oldAxis[3] == j.get_axis(0):
            onevent_controller_1axis4Changed_0()
    
    if not wantJoystick:
      class j:
        def get_hat(int):
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
        def get_button(int):
          if (int == 0):
            return (pygame.key.get_pressed()[pygame.K_b])
          if (int == 1):
            return (pygame.key.get_pressed()[pygame.K_a])
          if (int == 2):
            return (pygame.key.get_pressed()[pygame.K_y])
          if (int == 3):
            return (pygame.key.get_pressed()[pygame.K_x])
          if (int == 4):
            return (pygame.key.get_pressed()[pygame.K_SEMICOLON])
          if (int == 5):
            return (pygame.key.get_pressed()[pygame.K_QUOTE])
          if (int == 6):
            return (pygame.key.get_pressed()[pygame.K_COMMA])
          if (int == 7):
            return (pygame.key.get_pressed()[pygame.K_PERIOD])
        def get_axis(int):
          #if (int < 3.1):
            #return (0)
          if (int == 0):
            if (pygame.key.get_pressed()[pygame.K_d]):
              return (-1.00)
            elif (pygame.key.get_pressed()[pygame.K_g]):
              return (1.00)
            else:
              return (0)
          if (int == 1):
            if (pygame.key.get_pressed()[pygame.K_r]):
              return (-1.00)
            elif (pygame.key.get_pressed()[pygame.K_f]):
              return (1.00)
            else:
              return (0)
          if (int == 2):
            if (pygame.key.get_pressed()[pygame.K_j]):
               return (-1.00)
            elif (pygame.key.get_pressed()[pygame.K_l]):
              return (1.00)
            else:
              return (0)
          if (int == 3):
            if (pygame.key.get_pressed()[pygame.K_i]):
              return (-1.00)
            elif (pygame.key.get_pressed()[pygame.K_k]):
              return (1.00)
            else:
              return (0)
          if (int == 4):
            if (pygame.key.get_pressed()[pygame.K_LEFTBRACKET]):
              return (0.5)
            else:
              return (-0.5)
          if (int == 5):
            if (pygame.key.get_pressed()[pygame.K_RIGHTBRACKET]):
              return (0.5)
            else:
              return (-0.5)

    if pygame.joystick.get_count() == 0:
      wantJoystick = False

    if event.type == pygame.JOYDEVICEADDED:
      wantJoystick = True
      j = pygame.joystick.Joystick(event.device_index)
      
    if pygame.mouse.get_pressed()[0] and not oldMouse:
            onevent_brainScreen_pressed_0()
    if oldMouse and not pygame.mouse.get_pressed()[0]:
            onevent_brainScreen_released_0()

    timer = timerBench - pygame.time.get_ticks()
    oldHat = j.get_hat(0)
    oldButton = [j.get_button(0), j.get_button(1), j.get_button(2), j.get_button(3), j.get_button(4), j.get_button(5)]
    oldL2 = controller_1.buttonL2.pressing()
    oldR2 = controller_1.buttonR2.pressing()
    oldAxis = [j.get_axis(2), j.get_axis(3), j.get_axis(1), j.get_axis(0)]
    oldMouse = pygame.mouse.get_pressed()[0]

    

































    # RENDER YOUR GAME HERE
    # fill the screen with a color to wipe away anything from last frame
    #brain.screen.render()

    brainScreen.fill((0,0,0))
    brain.screen.set_fill_color(Color.PURPLE)
    brain.screen.set_pen_width(5)
    brain.screen.draw_line(240, 0, 240, 240)
    brain.screen.draw_rectangle(25, 25, 40, 40)
    brain.screen.draw_pixel(360, 120)
    brain.screen.draw_circle(240, 120, controller_1.axis1.position())
    #if brain.screen.pressing():
    if controller_1.buttonB.pressing():
        Pneumatic1.set(True)
        brain.screen.draw_rectangle(240 + controller_1.axis4.position(), 120 + controller_1.axis3.position(), 60, 60)
    if controller_1.buttonA.pressing():
        Pneumatic1.set(False)
    dx = controller_1.axis4.position() / 50
    dy = controller_1.axis3.position() / 50
    xPos += dx
    yPos += dy
    if controller_1.buttonADMINR.pressing() or controller_1.buttonADMINL.pressing():
        xPos = 240
        yPos = 120
        print(controller_1.axis4.position())
        print(clock)
    if controller_1.buttonR2.pressing():
        xPos += dx * 5
        yPos += dy * 5
    if controller_1.buttonL2.pressing():
        xPos += dx * 3
        yPos += dy * 3
    brain.screen.draw_circle(xPos, yPos, 10)
    brain.screen.draw_circle(brain.screen.x_position(), brain.screen.y_position(), 10)
    brain.screen.set_font(60)
    brain.screen.print('whats up dawg')
    pygame.draw.circle(controllerScreen, fillColor, (60, 60), 8 * 2)

    def onevent_controller_1buttonR1_released_0():
      print(wantJoystick)
    def onevent_controller_1buttonL1_released_0():
      print(j)
    def onevent_controller_1buttonX_released_0():
      print(pygame.joystick.get_count)
    def onevent_controller_1buttonY_released_0():
      print(brain.screen.get_string_width(''))
    # RENDER YOUR GAME HERE











    # flip() the display to put your work on screen
    ####screen.blit(controllerScreen, (200, 100))
    #brain.screen.render()
    if not renderCalled:
      screen.blit(brainScreen, (0,0))
      pygame.display.flip()

    clock.tick(60)  # limits FPS to 60



'''
Thank you for choosing to use my simulator!
All you have to do is copy and paste your code below,
and I'll take care of the rest.

Make sure that you only copy from above the weird comment vex made.
# create a function for handling the starting and stopping of all autonomous tasks
Yeah that one,
otherwise there's gonna be some weird stuff that we don't recognize.

LIMITATIONS:
-There is only support for one of each hat block for
  -each controller button pressed/released
  -each controller axis changed
  -Brain screen pressed/released
-"broadcast ___ and wait" hat block is not supported
-"when timer > 0" seconds" hat block is not supported

DEVICES:
Motor and pneumatics names are limited unless you change the code.
Controllers must be named Controller1 (in block code) OR Controller_1 (in python text code)
In order to tune them to your names for the devices, you have two options.
You can either change the names in your code, or go through here.
In both programs, motor groups and single motors are treated identically.
In this simulator, the supported names are written below.
pneumatic_1, pneumatic_2, pneumatic_3, pneumatic_4,
motor_1, motor_2, motor_3, motor_4, motor_5, motor_6, motor_7, motor_8,
controller_1,
Sensors are not yet supported
Multiple Controllers are not yet supported

CONTROLS:
The supported controller was programmed with:
Buttons: a, b, y, x, L1, R1,
Hat: Right, Left, Up, Down,
Axis: x1, y1, x2, y2, L2, R2,
Admin Buttons: Left, Right,

The keyboard has less accuracy, but is still supported:
Left joystick: RDFG
Right Joystick: IJKL
(It's easy if you remember the H is left alone in the middle.)
a, b, y, x, Right, Left, Up, Down
L1 & R1: ; and ' keys
L2 & R2: [ and ] keys
AdminL & AdminR: , and . keys

POSSIBLE BUGS:
-All event blocks based on user input (pressed, released, moved) MUST be named correctly.
-Translation between joystick and keyboard are not exact, so some directions on joysticks are given priority over others.
-Mouse movement is only tracked when the mouse is down, to accuratley replicate the brain screen.
-Not all USB controllers are programmed the same. This was programmed with a logitech controller. You will have to change it to use your unique one.
-The default fill color isn't purple. If it is, I messed something up :P.
-The buttons on vex controllers are switched from traditional ones. This code accounts for it. Make sure you do too.
'''
