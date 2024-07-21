from tkinter import*
window = Tk()
window.title('Анкета')
window.geometry('700x500')
label = Label(text = 'Расскажите о себе', font =('Arial', 20) )
label.place(x=10,y=10)
about = Message(text='Добро пожаловать что то там', font= ('Arial',20))
about.configure(justify=CENTER)
about.place(x=5,y=70)

label_name = Label(text='ФИО', font=('Arial',20))
label_name.place(x=5,y=175)
window.mainloop()