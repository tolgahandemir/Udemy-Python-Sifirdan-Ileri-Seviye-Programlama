from turtle import *

color('red','yellow')
speed(10)
begin_fill()
while True :
    forward(500)
    left(170)
    if abs(pos()) < 1 :
        break
end_fill()
done()