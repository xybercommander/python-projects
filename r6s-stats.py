import tkinter as tk

root = tk.Tk()

HEIGHT = 500
WIDTH = 500

def test_func(entry):
    print("This is the Entry:",entry)

canvas = tk.Canvas(root,height = HEIGHT,width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='black-and-white-grunge.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth = 1,relheight = 1)


frame = tk.Frame(root,bg = '#5588a3',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text = "Get Stats",bg = 'gray',fg = 'white',font=40,command = lambda: test_func(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

lower_frame = tk.Frame(root,bg = '#5588a3',bd = 10)
lower_frame.place(relx = 0.5,rely = 0.25,relwidth = 0.75, relheight = 0.6,anchor = 'n')

label = tk.Label(lower_frame)
label.place(relwidth=1,relheight=1)

root.mainloop()
