def setup():
    global cx
    global cy
    global px
    global py
    global r
    global c
    global theta
    size(1000,1000)
    cx = width / 2
    cy = height / 2
    
    px = cx
    py = cy
    
    colorMode(RGB)
    
    background (0)
    
    
cx = 0
cy = 0
r = 100
theta = 0

px = 0
py = 0
c = 0
x = 0
y = 0

def draw():
    global cx
    global cy
    global px
    global py
    global r
    global c
    global theta
    
    x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    
    stroke(c, c, 255, c)
    strokeWeight(10)
    line(px, py, x, y)
    
    r = r + 1
    c = (c + 20) % 256
    theta = theta + 15
    
    px = x
    py = y
    x = x + 1
    
    
    
    
    
    
    
