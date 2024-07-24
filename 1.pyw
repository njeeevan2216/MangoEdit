import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import scrolledtext
from tkinter import ttk
import subprocess as sp
import pickle as p

pad= 2

class np:
    def func(a):
        f_var.set("File")
        h_var.set("Help")
        o_var.set("Format")
        if (a=="About MangoEdit"):
            np.abou()
        elif (a=="New"):
            np.newf()
        elif (a=="New Window"):
            sp.Popen("pythonw 1.pyw",shell=False)
        elif (a=="Save"):
            np.savef()
        elif (a=="Open"):
            np.openf()
        elif (a=="Save As"):
            np.saveasf()
        elif (a=="Font"):
            np.fontf()
        return
    def abou():
        mb.showinfo("About MangoEdit", "This MangoEdit is developed by Jeevan N.")
    
    def newf():
        global nf        
        nf="Untitled"
        win.title(nf+" - "+"MangoEdit")
        text_area.delete(1.0,tk.END)

    def newwf():
        global nf
        nf= ""
        win.mainloop()
    
    def openf():
        global nf
        nf=fd.askopenfilename(defaultextension="txt",filetypes=[("Mango Files", "*.mg"), ("All Files", "*.*")])
        if nf=="":
            return
        win.title(nf+" - "+"MangoEdit")
        with open(nf,"rb") as f:
            input=""
            try:
                while True:
                    input+=str(p.load(f))
                    print(input)
            except EOFError:
                pass
            text_area.delete(1.0,tk.END)
            text_area.insert(tk.END,input)
    
    def savef():
        global nf
        if (nf==""):
            nf= fd.asksaveasfilename(defaultextension="txt",filetypes=[("Mango Files", "*.mg"), ("All Files", "*.*")])
            if nf=="":
                return
        win.title(nf+" - "+"MangoEdit")
        with open(nf,"wb") as f:
            output= text_area.get(1.0,tk.END)
            #f.write(output)
            p.dump(output,f)
        return
    
    def saveasf():
        global nf
        nf= fd.asksaveasfilename(defaultextension="txt",filetypes=[("Mango Files", "*.mg"), ("All Files", "*.*")])
        if nf=="":
            return
        win.title(nf+" - "+"MangoEdit")
        with open(nf,"wb") as f:
            output= text_area.get(1.0,tk.END)
            #f.write(output)
            p.dump(output,f)
        return
    
    def fontf():
        global a, fontw, font_size, promptsize,wrapBool
        wrapBool= tk.BooleanVar()
        fontw= tk.Tk()
        fontw.title("Fonts")
        fontw.geometry("200x250")
        fontframe=tk.Frame(fontw)
        ttk.Label(fontframe, text="Select Font:").pack(side="left")
        a=tk.Listbox(fontframe,)
        fontList=["Times New Roman", "Consolas", "Cooper", "Constantia", "Gabriola", "Lucida Sans", "Comic Sans MS", ]
        for f in fontList:
            a.insert(tk.END,f)
        a.pack(side="left")
        fontframe.pack()
        exb=ttk.Button(fontw,text="Done",command=np.fontf_done)
        exb.pack(side="bottom")
        size= tk.Frame(fontw)
        sizeprompt=ttk.Label(size, text="Font Size:")
        sizeprompt.pack(side="left")
        promptsize= tk.StringVar(size, "12")
        ttk.OptionMenu(size, promptsize,"2","4","6","8","10","12","14","16","18","20","22","24","26","28","30","32","34","36","38","40","42","44","46","48","50","52","54","56","58","60","62","64","66","68","70","72").pack(side="left")
        size.pack(side="bottom")
        checkBtnFrame= tk.Frame(fontw)
        wrap= ttk.Checkbutton(checkBtnFrame, text= "Word Wrap", variable=wrapBool)
        wrap.pack()
        checkBtnFrame.pack(side="bottom")
        fontw.mainloop()
        return

    def fontf_done():
        global a, fontw, promptsize,wrapBool
        font_name = a.get("active")
        font_size = promptsize.get()
        print(wrapBool.get())
        fontw.destroy()
        text_area.config(font=(font_name,int(font_size)))
        fontDis.config(text="Font: " + font_name + ',' + str(font_size))
        return

a=None
font_name="Arial"
font_size= 12
nf=""
win = tk.Tk()
win.title("MangoEdit")
win.geometry("720x400")
tk.Menu(win,cnf={},title="hello",type="menubar").pack()


frame = tk.Frame(win)
frame.pack(fill="x", padx=pad, pady=pad)



f_var= tk.StringVar(win, "File")
h_var= tk.StringVar(win, "Help")
o_var= tk.StringVar(win, "Format")
o_file = ttk.OptionMenu(frame, f_var, "File",
                                     "New", 
                                     "New Window", 
                                     "Open", 
                                     "Save", 
                                     "Save As",
                                     "Exit", command=np.func)
o_option = ttk.OptionMenu(frame, o_var, "Format", "Font", command=np.func)
o_help = ttk.OptionMenu(frame, h_var, "Help", "About MangoEdit", command=np.func)
o_file.pack(side="left")
o_option.pack(side="left")
o_help.pack(side="left")

list=tk.Variable(frame)

status_bar= tk.Frame(win)

fontDis= tk.Label(status_bar, text="Font: " + font_name + ',' + str(font_size))
fontDis.pack(side='left')

status_bar.pack(side=tk.BOTTOM, fill="x")

textFrame= tk.Frame(win)
text_area= scrolledtext.ScrolledText(textFrame)
text_area.config(height=2000)
text_area.pack(fill="both")


h_scroll= tk.Scrollbar(textFrame, orient= tk.HORIZONTAL, command= text_area.xview)
h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

text_area.config(wrap="none", xscrollcommand=h_scroll.set)
textFrame.pack(fill="both", padx=pad, pady=pad+2)



win.mainloop()