from turtle import *


speed(4)
shape('turtle')
pensize(4)
color("Purple")
for count in range(1):
    forward(500)
    right(90)
    forward(200)
    right(90)
    forward(500)
    right(90)
    forward(200)
    right(35)
    forward(205)
    
# Telhado
    color("brown")
    right(55)
    forward(330)
    right(70)
    forward(168)
# Levanta a caneta
    penup()
    right(132)
    forward(413)
# Giro para equerda    
    left(135)
# Baixa a caneta
    pendown()
    forward(180)
    right(22.9)
    
# Parede que divide a sala do quarto
    color("green")
    forward(195)
    right(90)
    penup()
    forward(150)
    right(90)
    pendown()
    
# Porta
    color("blue")
    forward(150)
    right(90)
    forward(70)
    right(90)
    forward(150)
    left(130)
    penup()
    forward(230)
    right(40)
    pendown()
    color("red")
    
# Janela
for count in range(4):
    forward(50)
    right(90)
left(140)
penup()
pendown()

color("yellow")
# Folha esquerda da janela
forward(25)
left(130)
forward(80)
left(131.11)
forward(25)
right(42)
penup()
forward(50)
right(35)
pendown()

# Folha direita da janela
forward(25)
left(125.8)
forward(80)
left(130)
forward(25)
penup()
right(87)
color("black")

# Começando o telhado
forward(275)
left(180)
pendown()
forward(30)
left(95)

for count in range(5):
    forward(40)
    right(90)
    forward(40)
    left(90)
 
penup()
right(220)
forward(290)
left(130)
pendown()
for count in range(5):
    forward(40)
    left(90)
    forward(40)
    right(90)

right(120)
penup()
forward(255)
left(120)
pendown()
for count in range(5):
    forward(40)
    left(90)
    forward(40)
    right(90)
right(150)
penup()
forward(750)
pendown()
color("yellow")


# Sol
for count in range(6):
    forward(90)
    right(130)
    forward(90)
    left(90)
    left(130)

left(50)
penup()
forward(300)
pendown()

  




    
    
    
