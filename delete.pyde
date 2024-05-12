def setup():
    size(600,600)
    background(0)
def draw():
    strokeWeight(4)
    stroke(255)
    point(random(600),random(600))
    if mousePressed==True:
        clear()
