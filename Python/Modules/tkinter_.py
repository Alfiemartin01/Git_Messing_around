import tkinter 

def file_r() -> None:
    '''
    Reads the contents of the given file in the filepath inputted into the textbox
    creates a label, containing the contents.'''
    global fcont_lbl
    filepath = path_txt.get()
    fcont_lbl.destroy()
    filef = open(filepath,'r')
    
    filelist = filef.readlines()
    contents = "".join(f"{i+1}. {j}" for i,j in enumerate(filelist))
    fcont_lbl = tkinter.Label(root,text=contents)
    
    fcont_lbl.grid(row=2,column = 0)




root=tkinter.Tk()

path_lbl = tkinter.Label(root, text='Please input a file path')
path_txt = tkinter.Entry(root)
read_btn = tkinter.Button(root,text = 'display contents', command=file_r)
path_lbl.grid(row=0,column=0)
path_txt.grid(row=0,column=1)
read_btn.grid(row=1,column=0)
fcont_lbl = tkinter.Label()



root.mainloop()