import Tkinter as tk   # python
from Tkinter import *
import tkFileDialog
from PIL import Image
import os
import webbrowser
import functions
import hideTextInImage
import unhideTextInImage

TITLE_FONT = ("Helvetica", 18, "bold")
pathvar = ""
textpathvar = ""
encimage = ""




class Text2PNG(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top")
        self.title("Text2PNG")
        container.grid_columnconfigure(0, weight=1);container.grid_columnconfigure(1, weight=1);
        container.grid_columnconfigure(2, weight=1); 
        self.frames = {}
        for F in (picframe, textframe, submitframe,decryptframe):
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
        submitpage = tk.Button(self, text="Hide text", height=2, width = 16, bg = "springgreen4", fg = "white",  
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,
                            command=lambda: controller.show_frame("textframe"))
        decryptpage = tk.Button(self, text = "Decrypt the Image",height =2, width=16,
                            command=lambda: controller.show_frame("decryptframe"))
        startencr = tk.Button(self, text="Start Hiding Process\n (will show picture when finished)", height = 8, activebackground = "turquoise2", 
                            command=self.encryptPic)
        saveimage = tk.Button(self, text="Save Encrypted Image", height = 8, activebackground = "turquoise2")
        submitpage.grid(row=0, column=2);imagepage.grid(row=0, column=0);textpage.grid(row=0, column =1); decryptpage.grid(row = 0, column = 3)
        startencr.grid(row=1, column =0, columnspan = 4, sticky=N+E+W+S);saveimage.grid(row=2, column =0, columnspan = 4, sticky=N+E+W+S)
    def encryptPic(self):
        global pathvar
        global textpathvar
        hideTextInImage.processingImage(pathvar, textpathvar)





class picframe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        submitpage = tk.Button(self, text="Hide text", height=2, width = 16,  
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,bg = "springgreen4", fg = "white",
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,
                            command=lambda: controller.show_frame("textframe"))
        decryptpage = tk.Button(self, text = "Decrypt the Image",height =2, width=16,
                            command=lambda: controller.show_frame("decryptframe"))
        browseimage = tk.Button(self, text="Browse Images", height = 8, command=self.onOpen, activebackground = "turquoise2")
        showimage = tk.Button(self, text="Show Image", height = 8, command=self.openPic, activebackground = "turquoise2")
        submitpage.grid(row=0, column=2)
        imagepage.grid(row=0, column=0);
        textpage.grid(row=0, column =1)
        decryptpage.grid(row = 0, column =3)
        browseimage.grid(row=1, column =0, columnspan = 4, sticky=W+E)
        showimage.grid(row=2, column =0, columnspan = 4, sticky=W+E)

    def onOpen(self):
        ftypes = [('PNG Files', '*.png')]
        pngimage = tkFileDialog.askopenfilename(filetypes = ftypes)

        pngimage = str(pngimage)
        self.pathvar = tk.StringVar()
        self.pathvar.set(pngimage)
        global pathvar
        pathvar = pngimage

    def openPic(self):
        filepath = self.pathvar.get()
        showpng = Image.open(filepath)
        showpng.show()



        

        
class textframe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        submitpage = tk.Button(self, text="Hide text", height=2, width = 16,  
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,bg = "springgreen4", fg = "white",
                            command=lambda: controller.show_frame("textframe"))
        decryptpage = tk.Button(self, text = "Decrypt the Image",height =2, width=16,
                            command=lambda: controller.show_frame("decryptframe"))
        

        browsetext = tk.Button(self, text="Browse Text Files", height = 8, command=self.onOpen, activebackground = "turquoise2")
        showtext = tk.Button(self, text="Show Text File", height = 8, command=self.openText, activebackground = "turquoise2")
        submitpage.grid(row=0, column=2)
        imagepage.grid(row=0, column=0);
        textpage.grid(row=0, column =1)
        decryptpage.grid(row = 0, column = 3)
        browsetext.grid(row=1, column =0, columnspan = 4, sticky=W+E)
        showtext.grid(row=2, column =0, columnspan = 4, sticky=W+E)

    def onOpen(self):
      
        ftypes = [('Text Files', '*.txt')]
        txtfile = tkFileDialog.askopenfilename(filetypes = ftypes)
        txtfile = str(txtfile)
        self.textpathvar = tk.StringVar()
        self.textpathvar.set(txtfile)
        global textpathvar
        textpathvar = txtfile

    def openText(self):
        filepath = self.pathvar.get()
        webbrowser.open(filepath)


class decryptframe(tk.Frame):
    def nOpen(self):
            ftypes = [('PNG Files', '*.png')]
            pngimage = tkFileDialog.askopenfilename(filetypes = ftypes)
            pngimage = str(pngimage)
            global encimage
            encimage = pngimage
            
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        submitpage = tk.Button(self, text="Hide text", height=2, width = 16,  
                            command=lambda: controller.show_frame("submitframe"))
        imagepage = tk.Button(self, text="Choose an image", height=2, width=16,
                            command=lambda: controller.show_frame("picframe"))
        textpage = tk.Button(self, text="Choose a text file",height =2, width=16,
                            command=lambda: controller.show_frame("textframe"))
        decryptpage = tk.Button(self, text = "Decrypt the Image",height =2, width=16, bg = "springgreen4", fg = "white", 
                            command=lambda: controller.show_frame("decryptframe"))
        browsedeimage = tk.Button(self, text = "Browse for the Encrypted Image", height = 8, command=self.nOpen, activebackground = "turquoise2")
        showmess = tk.Button(self, text = "Show the Decrypted Message" , height = 8,command=self.showMessage, activebackground = "turquoise2")
        browsedeimage.grid(row = 1, column = 0, columnspan = 4, sticky=W+E)
        showmess.grid(row = 2, column = 0, columnspan = 4, sticky=W+E)
        submitpage.grid(row=0, column=2)
        imagepage.grid(row=0, column=0);
        textpage.grid(row=0, column =1)
        decryptpage.grid(row = 0, column = 3)
    def showMessage(self):
        global encimage
        print encimage
        unhideTextInImage.decryptImage(encimage)



if __name__ == "__main__":
    app = Text2PNG()
    app.mainloop()