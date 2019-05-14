from tkinter import *
from os import listdir,getcwd,path
import psutil
buttons=[]

class window():
    def __init__(self):pass
        
    def start(dir_path):    
        root=Tk()
        #{top frame
        topframe=Frame(root,height=100,width=1000)
        topframe.pack(side=TOP,padx=5,pady=3)#}
        #{back buton
        back_img=PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\form\\back.gif")
        back_btn=Button(topframe,padx=10,pady=10,height=30,width=40,image=back_img)
        back_btn.pack(side=LEFT)#}
        #{dir text box
        directory_entry=Entry(topframe,text=getcwd,width=170)
        directory_entry.pack(side=LEFT,padx=10)#}
        
        #{go button
        def go():pass
                
        go_img=PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\form\\go.png")
        go_btn=Button(topframe,padx=10,pady=10,height=30,width=40,image=go_img,command=go)
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
        frame=Frame(canvas,width=canvas.winfo_height(),height=canvas.winfo_width()) #}
        #{folder btns functions
        def button_check(buttonName):
            print(buttonName)
        icons={'mp3':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\mp3.gif'),
        'jpg':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\jpg.gif'),
        'mp4':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\mp4.gif'),
        'pdf':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\pdf.gif'),
        'png':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\png.gif'),
        'txt':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\txt.gif'),
        'docx':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\docx.gif'),
        'alt':PhotoImage(file='C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\alt.gif'),
        'folder_img':PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\folder.gif")}
       
        window.files_folders(root,frame,dir_path,icons)
        
        #{scroll bar        
        scroll=Scrollbar(bottomframe,orient="vertical", command=canvas.yview)
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll.set)
        scroll.config(command=canvas.yview)
        canvas.pack(fill=Y, expand=True, side='left')
        scroll.pack(fill='y', side='right')#}
        #{left frame
        leftframe=Frame(root)
        leftframe.pack(side=LEFT)#}
        scroll_frame=Frame(leftframe)
        scroll_frame.pack(side=RIGHT)
        #{canvas frame
        leftcanvas=Canvas(leftframe,width=130,height=1000)
        frame_left=Frame(leftcanvas) #}
        #{drive btn command
        def go_dir(dir_name):
            print(dir_name)#}
        #{drives
        button=0
        drive_img=PhotoImage(file="C:\\Users\\little_dev\\Desktop\\file_explorer\\icons\\Folder&File\\drive.gif")
        for num,name in enumerate(psutil.disk_partitions()):
            num+=1
            dir_btn=Button(frame_left,image=drive_img,command=lambda dir_name = str(name):go_dir(dir_name))
            dir_btn.pack(side=TOP)
            dir_lbl=Label(frame_left,text=name[0])
            dir_lbl.pack(side=TOP)
        #{scroll left
        leftscroll=Scrollbar(scroll_frame,orient="vertical", command=leftcanvas.yview)
        leftcanvas.create_window(0, 0, anchor='nw', window=frame_left)
        leftcanvas.update_idletasks()
        leftcanvas.configure(scrollregion=leftcanvas.bbox('all'),yscrollcommand=leftscroll.set)
        leftscroll.config(command=leftcanvas.yview)
        leftcanvas.pack(fill=Y, expand=True, side='left')
        leftscroll.pack(fill=Y, side=RIGHT)#}
         
        root.mainloop()
        
    def Exit():
        quit()
        
    def label(root,frame,r):
            for num,name in enumerate(buttons):
                button_lbl=Label(frame,width=10,height=5,text=name,wraplength=70)
                button_lbl.grid(row=r+1,column=num)

    def file_image(ex):
        if ex=='mp3'or ex=='jpg'or ex=='mp4' or ex=='pdf' or ex=='png' or ex=='txt'or ex=='docx':
            return ex
        else:
            return 'alt'
    def files_folders(root,frame,dir_path,icons):
        #{files in dir
        r=0
        c=0
        button=0
        for num,files in enumerate(listdir(dir_path)):
            path_var=dir_path+files
            if path.isfile(path_var):
                filename, file_extension = path.splitext(path_var)
                
                if button==6:
                    window.label(root,frame,r)
                    buttons.clear()
                    button=0
                    r+=2
                    c=0
                folder_button =Button(frame,text=files,command=lambda buttonName = files:button_check(buttonName),width=120,height=120,image=icons[window.file_image(file_extension[1:].lower())])
                button+=1
                folder_button.grid(row=r,column=c)
                buttons.append(files)
                c+=1
        window.label(root,frame,r)#}
         #{folders in dir
        r=0
        c=0
        button=0

        for i,folders in enumerate(listdir(dir_path)):
            path_var=dir_path+folders
            if path.isdir(path_var):  
                if button==6:
                    window.label(root,frame,r)
                    buttons.clear()
                    button=0
                    r+=2
                    c=0
                folder_button =Button(frame,text=folders,command=lambda buttonName = folders:button_check(buttonName),width=120,height=120,image=icons['folder_img'])
                button+=1
                folder_button.grid(row=r,column=c)
                buttons.append(folders)
                c+=1
        window.label(root,frame,r)#}
window.start('F:\\') 
