import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")

class Text2PNG(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top")
        self.geometry("418x405")
        self.title("Text2PNG")
        #container.grid_rowconfigure(0, weight=1);container.grid_rowconfigure(1, weight=1);
        container.grid_columnconfigure(0, weight=1);container.grid_columnconfigure(1, weight=1);
        container.grid_columnconfigure(2, weight=1);
        self.frames = {}
        for F in (mainframe, picframe, textframe, submitframe):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("mainframe")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class mainframe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        submitpage = tk.Button(self, text="Hide text", height=2, width = 16,
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,
                            command=lambda: controller.show_frame("textframe"))
        browseimage = tk.Button(self, text="Browse Images", height = 8, width = 51)
        showimage = tk.Button(self, text="Show Image", height = 8, width = 51)
        submitpage.grid(row=0, column=0)
        imagepage.grid(row=0, column=1);
        textpage.grid(row=0, column =2)
        browseimage.grid(row=1, column =0, columnspan = 3)
        showimage.grid(row=2, column =0, columnspan = 3)



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
        startencr = tk.Button(self, text="Start Hiding Process\n (will show picture when finished)", height = 8, width = 51)
        saveimage = tk.Button(self, text="Save Encrypted Image", height = 8, width = 51)
        submitpage.grid(row=0, column=0);imagepage.grid(row=0, column=1);textpage.grid(row=0, column =2);
        startencr.grid(row=1, column =0, columnspan = 3);saveimage.grid(row=2, column =0, columnspan = 3)


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
        browseimage = tk.Button(self, text="Browse Images", height = 8, width = 51)
        showimage = tk.Button(self, text="Show Image", height = 8, width = 51)
        submitpage.grid(row=0, column=0)
        imagepage.grid(row=0, column=1);
        textpage.grid(row=0, column =2)
        browseimage.grid(row=1, column =0, columnspan = 3)
        showimage.grid(row=2, column =0, columnspan = 3)
        
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
        browseimage = tk.Button(self, text="Browse Text Files", height = 8, width = 51)
        showimage = tk.Button(self, text="Show Text File", height = 8, width = 51)
        submitpage.grid(row=0, column=0)
        imagepage.grid(row=0, column=1);
        textpage.grid(row=0, column =2)
        browseimage.grid(row=1, column =0, columnspan = 3)
        showimage.grid(row=2, column =0, columnspan = 3)


if __name__ == "__main__":
    app = Text2PNG()
    app.mainloop()