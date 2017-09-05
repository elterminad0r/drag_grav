from GravityBall import GravityBall

balls = 50
cooldown = 30

def setup():
    size(800, 800)

def draw():
    global balls, cooldown
    if balls :
        if not cooldown:
            cooldown = 30
            balls -= 1
            print(balls)
            GravityBall()
        else:
            cooldown -= 1
    translate(0, height)
    scale(1, -1)
    colorMode(HSB, 255, 255, 255)
    background(0)
    GravityBall.update()
    GravityBall.fade()
    GravityBall.draw()

def mousePressed():
    GravityBall(PVector(mouseX, height - mouseY))
    print(len(GravityBall.inst))

def keyPressed():
    if keyCode == ord(' '):
        GravityBall()
    elif keyCode == ord('\b'):
        if GravityBall.inst:
            GravityBall.inst.pop()
    print(len(GravityBall.inst))