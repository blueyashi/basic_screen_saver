from tkinter import *
from random import *
class Balls:
    def __init__(self,canvas):
        self.canvas = canvas;
        self.screenWidth = canvas.winfo_screenwidth()
        self.screenHeight = canvas.winfo_screenheight()
        self.randValues()
        self.createBall()

    def randValues(self):
        self.radius = randint(50, 100)
        self.x_coord = randint(self.radius,self.screenWidth-self.radius)
        self.y_coord = randint(self.radius,self.screenHeight-self.radius)
        self.x_speed=randint(5,15)
        self.y_speed=randint(5,15)
        self.color = self.randColors();

    def randColors(self):
        randVal = lambda : randint(0,0xffff)
        return "#{:4x}{:4x}{:4x}".format(randVal(),randVal(),randVal())

    def createBall(self):
        x1 = self.x_coord - self.radius
        y1 = self.y_coord - self.radius
        x2 = self.x_coord + self.radius
        y2 = self.y_coord + self.radius
        self.ball = self.canvas.create_oval(x1,y1,x2,y2, fill =self.color, outline=self.color)

    def moveBall(self):
        self.findBound()
        self.x_coord += self.x_speed
        self.y_coord += self.y_speed
        self.canvas.move(self.ball,self.x_speed,self.y_speed)

    def findBound(self):
        if not self.radius<self.x_coord<self.screenWidth-self.radius:
            self.x_speed = -self.x_speed
        if not self.radius<self.y_coord<self.screenHeight-self.radius:
            self.y_speed = -self.y_speed
class Screen:
    balls = []
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha",0.3)
        self.canvas=Canvas(self.root)
        self.canvas.pack(expand=1,fill="both")
    
        for ball in range(15):
            self.balls.append(Balls(self.canvas))
        self.moveBalls()
        self.root.mainloop()

    def moveBalls(self):
        #self.ball.moveBall()
        for ball in self.balls:
            ball.moveBall()
        self.root.after(15, self.moveBalls)
Screen()
