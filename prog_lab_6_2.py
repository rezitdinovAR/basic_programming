from tkinter import *
import time

c = Canvas(width=1000,height=1000,bg='white')
c.pack()
base=c.create_polygon(425,400,575,400,575,800,425,800,fill='gray63')
c1=c.create_oval(450,425,550,525,fill='gray25')
c2=c.create_oval(450,550,550,650,fill='gray25')
c3=c.create_oval(450,675,550,775,fill='gray25')
def traffic_light(event):
    c11=c.create_oval(450, 425, 550, 525, fill='red')
    c.update()
    time.sleep(28)
    c12=c.create_oval(450, 550, 550, 650, fill='yellow')
    c.update()
    time.sleep(2)
    c.delete(c11)
    c.update()
    c.delete(c12)
    c.update()
    c13=c.create_oval(450,675,550,775,fill='green')
    c.update()
    time.sleep(30)
    c.delete(c13)
    c.update()

c.tag_bind(base,'<Button-1>',traffic_light)
mainloop()