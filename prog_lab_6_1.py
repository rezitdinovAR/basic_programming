'''Реализуйте движение (анимацию) геометрической фигуры по
холсту.'''

from tkinter import *
import time
import _thread
c=Canvas(width=500,height=500,bg='white')
c.pack()
oval = c.create_oval(245, 245, 255, 255, fill="black")
def make_waves(event):
    _thread.start_new_thread(waves,())
def waves():
    x=5
    y=5
    while x<250:
        oval=c.create_oval(250-x,250-y,250+x,250+y,outline='black')
        c.update()
        time.sleep(0.05)
        c.delete(oval)
        c.update()
        x+=5
        y+=5
    _thread.exit()
c.tag_bind(oval,'<Button-1>',make_waves)
mainloop()
