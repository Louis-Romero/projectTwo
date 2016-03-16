import Tkinter as tk   # python
from Tkinter import *
import tkFileDialog

TITLE_FONT = ("Helvetica", 18, "bold")

class Text2PNG(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top")
        self.geometry("415x405")
        self.title("Text2PNG")
        #container.grid_rowconfigure(0, weight=1);container.grid_rowconfigure(1, weight=1);
        container.grid_columnconfigure(0, weight=1);container.grid_columnconfigure(1, weight=1);
        container.grid_columnconfigure(2, weight=1);
        self.frames = {}
        for F in (picframe, textframe, submitframe):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("picframe")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class submitframe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        submitpage = tk.Button(self, text="Hide text", height=2, width = 16,  
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,
                            command=lambda: controller.show_frame("textframe"))
        startencr = tk.Button(self, text="Start Hiding Process\n (will show picture when finished)", height = 8)
        saveimage = tk.Button(self, text="Save Encrypted Image", height = 8)
        submitpage.grid(row=0, column=2);imagepage.grid(row=0, column=0);textpage.grid(row=0, column =1);
        startencr.grid(row=1, column =0, columnspan = 3, sticky=N+E+W+S);saveimage.grid(row=2, column =0, columnspan = 3, sticky=N+E+W+S)


class picframe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        submitpage = tk.Button(self, text="Hide text", height=2, width = 16,  
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,
                            command=lambda: controller.show_frame("textframe"))
        browseimage = tk.Button(self, text="Browse Images", height = 8, command=self.onOpen)
        showimage = tk.Button(self, text="Show Image", height = 8)
        submitpage.grid(row=0, column=2)
        imagepage.grid(row=0, column=0);
        textpage.grid(row=0, column =1)
        browseimage.grid(row=1, column =0, columnspan = 3, sticky=W+E)
        showimage.grid(row=2, column =0, columnspan = 3, sticky=W+E)
    def onOpen(self):
      
        ftypes = [('PNG Files', '*.png')]
        pngimage = tkFileDialog.askopenfilename(filetypes = ftypes)
        

        
class textframe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        submitpage = tk.Button(self, text="Hide text", height=2, width = 16,  
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,
                            command=lambda: controller.show_frame("textframe"))
        browseimage = tk.Button(self, text="Browse Text Files", height = 8)
        showimage = tk.Button(self, text="Show Text File", height = 8)
        submitpage.grid(row=0, column=2)
        imagepage.grid(row=0, column=0);
        textpage.grid(row=0, column =1)
        browseimage.grid(row=1, column =0, columnspan = 3, sticky=W+E)
        showimage.grid(row=2, column =0, columnspan = 3, sticky=W+E)


if __name__ == "__main__":
    app = Text2PNG()
    app.mainloop()