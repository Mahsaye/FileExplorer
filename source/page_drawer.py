from tkinter import *
from os import listdir,getcwd,path
class window():
    def __init__(self):pass
        
    def start():    
        root=Tk()
        #{top frame
        topframe=Frame(root,height=100,width=1000)
        topframe.pack(side=TOP,padx=5,pady=3)#}
        #{back buton
        back_img=PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\form\\back.gif")
        back_btn=Button(topframe,padx=10,pady=10,height=30,width=40,image=back_img)
        back_btn.pack(side=LEFT)#}
        #{dir text box
        directory=Entry(topframe,text=getcwd,width=170)
        directory.pack(side=LEFT,padx=10)#}
        #{go button
        go_img=PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\form\\go.png")
        go_btn=Button(topframe,padx=10,pady=10,height=30,width=40,image=go_img)
        go_btn.pack(side=LEFT)#}
        #{toolbar
        toolbar=Menu(topframe)
        root.config(menu=toolbar)
        file=Menu(topframe)
        file.add_command(label='exit',command= window.Exit)
        toolbar.add_cascade(label="File", menu=file)
        view=Menu(topframe)
        toolbar.add_cascade(label='View',menu=view)
        #{bottom frame
        bottomframe=Frame(root,height=935,width=1000)
        bottomframe.pack(side=RIGHT,padx=5,pady=3)#}
        #{canvas frame
        canvas=Canvas(bottomframe,width=935,height=1000)
        frame=Frame(canvas) #}
        #{hoveron  & leave effect for folder btns
        def on_leave(folders):
            folder_button['image']=folder_img
        def on_hover(folders):
            folder_button['image']=folder_hover
        def button_check(buttonName):
            print(folders)
        #{files in dir
        r=0
        c=0
        button=0
        folder_img=PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\folder.gif")
        folder_hover=PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\folder_h.gif")
        for i,folders in enumerate(listdir("C:\\")):
            if path.isdir('C:\\'+folders):
                folder_button =Button(frame,text=folders,command=lambda buttonName = '%s' % folders:button_check(buttonName),width=70,height=70,image=folder_img)
                folder_button.bind("<Enter>",on_hover)
                folder_button.bind('<Leave>',on_leave)
                if button==12:
                    button=0
                    r+=1
                    c=0
                button+=1
                folder_button.grid(row=r,column=c)
                c+=1#}
        
        #{scroll bar        
        scroll=Scrollbar(bottomframe,orient="vertical", command=canvas.yview)
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll.set)
        scroll.config(command=canvas.yview)
        canvas.pack(fill=Y, expand=True, side='left')
        scroll.pack(fill='y', side='right')#}
        #{left frame
        leftframe=Frame(root,width=40,height=1200)
        leftframe.pack(side=LEFT)#}
        
        root.mainloop()
    def Exit():
        quit()
        
window.start()

        
