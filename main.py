import turtle, random, time, keyboard

sc = turtle.Screen()
sc.setup(500, 500)
sc.bgpic("bg.gif")
sc.register_shape("floofy.gif")
sc.register_shape("paddle.gif")
sc.title("Floooooofy's Pong Game")
sc.tracer(0)

ball = turtle.Turtle()
ball.shape("floofy.gif")
ball.up()
ballx = random.choice([-6, 6])
bally = random.choice([-6, -1.2, 1.2, 6])
right_paddle = turtle.Turtle()
right_paddle.up()
right_paddle.shape("paddle.gif")
right_paddle.goto(200, 0)

left_paddle = turtle.Turtle()
left_paddle.up()
left_paddle.shape("paddle.gif")
left_paddle.goto(-200, 0)

sk = turtle.Turtle()
sk.speed(0)
sk.up()
sk.ht()
sk.goto(0, -200)

left_score = 0
right_score = 0
def update_score():
  global left_score
  global right_score
  sk.clear()
  sk.goto(0, -200)
  sk.write(f"Score: {left_score} | {right_score}", align="center", font=("Courier", 20, "bold"))
update_score()

speed = 20
def left_up():
  global speed
  y = left_paddle.ycor()
  y += speed
  left_paddle.sety(y)
def left_down():
  global speed
  y = left_paddle.ycor()
  y -= speed
  left_paddle.sety(y)
def right_up():
  global speed
  y = right_paddle.ycor()
  y += speed
  right_paddle.sety(y)
def right_down():
  global speed
  y = right_paddle.ycor()
  y -= speed
  right_paddle.sety(y)

sc.listen()
sc.onkey(left_up, "w")
sc.onkey(left_down, "s")
sc.onkey(right_up, "Up")
sc.onkey(right_down, "Down")

while True:
  sc.update()
  time.sleep(0.1)
  ball.setx(ball.xcor()+ballx)
  ball.sety(ball.ycor()+bally)
  
  #check if the ball hits the top & bottom walls
  if ball.ycor()>250 - 20 or ball.ycor()<-250 + 20:
    bally = bally*-1.1

  #check if the ball hits the left/right wall
  if ball.xcor() > 250:
    ball.goto(0,0)
    left_score += 1
    update_score()
    ballx = random.choice([-6, 6])
    bally = random.choice([-6, -1.2, 1.2, 6])
  elif ball.xcor() < -250:
    ball.goto(0,0)
    right_score += 1
    update_score()
    ballx = random.choice([-6, 6])
    bally = random.choice([-6, -1.2, 1.2, 6])

  #collision between ball & paddle
  if ball.xcor()<left_paddle.xcor()+40 and ball.xcor()>left_paddle.xcor()-40 and ball.ycor()<left_paddle.ycor()+80 and ball.ycor()>left_paddle.ycor()-80:
    ballx *= -1.2
    bally *= 1.2
  if ball.xcor()<right_paddle.xcor()+40 and ball.xcor()>right_paddle.xcor()-40 and ball.ycor()<right_paddle.ycor()+80 and ball.ycor()>right_paddle.ycor()-80:
    ballx *= -1.2
    bally *= 1.2

  #detect winners
  if left_score > 5 or right_score > 5:
    break

#code for when you win
sc.bgpic("win.gif")
left_paddle.ht()
right_paddle.ht()
ball.goto(-180,-200)
sk.clear()
if left_score > 5:
  sk.goto(0, 130)
  sk.write("Left Player WINS!", align="center",
     font=("Courier",15,"normal"))
else:
  sk.goto(0, 130)
  sk.write("Right Player WINS!", align="center",
     font=("Courier",15,"normal"))
sc.update()