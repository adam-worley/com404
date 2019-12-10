from tkinter import *
import time

# the class
class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.umbrella_image = PhotoImage(file="umbrella.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.umbrella_x_pos = 200
        self.umbrella_y_pos = 20
        self.umbrella_x_change = 10
        self.umbrella_y_change = 10
        
        # add components
        self.add_umbrella_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.umbrella_x_pos = self.umbrella_x_pos + self.umbrella_x_change
        self.umbrella_y_pos = self.umbrella_y_pos + self.umbrella_y_change
        self.umbrella_image_label.place(x=self.umbrella_x_pos, 
                                    y=self.umbrella_y_pos)

        if (self.umbrella_x_pos <= 0 or self.umbrella_x_pos >= (500 - self.umbrella_image_label.winfo_width())):
            self.umbrella_x_change = -self.umbrella_x_change

        if (self.umbrella_y_pos <= 0 or self.umbrella_y_pos >= (500 - self.umbrella_image_label.winfo_height())):
            self.umbrella_y_change = -self.umbrella_y_change
            
        self.after(100, self.tick)

    # the umbrella image
    def add_umbrella_image_label(self):
        self.umbrella_image_label = Label()
        self.umbrella_image_label.place(x=self.umbrella_x_pos,
                                    y=self.umbrella_y_pos)
        self.umbrella_image_label.configure(image=self.umbrella_image)
     
# the object
gui = Gui()    
gui.mainloop() 