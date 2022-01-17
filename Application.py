from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from PIL import Image, ImageTk

from Conditions import *
from Methods import *

functions = {'steepest_descent': steepest_descent, 'minimal_residual': minimal_residual,
             'conjugation_gradients': conjugation_gradients}
conditions = {'1': condition1, '2': condition2, '3': condition3, '4': condition4}
conditions_name = {'1': "maximum", '2': "sum", '3': "special 1", '4': "special 2"}


def read_file(filename):
    txt = open(filename, "r", encoding='utf-8')
    file = txt.readlines()
    txt.close()

    return file


def clean_frame(event):
    tex.delete(1.0, END)


def save_results(event):
    saver = asksaveasfilename()
    text = "With accuracy = " + ent.get() + ", " + conditions_name[str(var.get())] + " condition, " + combo.get() + \
           ":\n\n" + tex.get(1.0, END)

    file = open(saver, "w", encoding='utf-8')
    file.write(text)

    file.close()


def start(event):
    filename = askopenfilename()
    file = read_file(filename)

    coefficients = []
    function = []

    eps = float(ent.get())
    functciya = combo.get()
    conditciya = str(var.get())

    for i in range(len(file)):
        if file[i] != "%\n":
            array = file[i].split("|")
            coefficients.append(list(map(float, array[0].split(" "))))
            function.append(array[1].split("\n")[0])
        else:
            a = np.asmatrix(coefficients)
            b = np.asmatrix(list(map(float, function))).transpose()

            answer, iterations = functions[functciya](a.transpose().dot(a), a.transpose().dot(b), eps,
                                                      conditions[conditciya])

            tex.insert(END, answer)
            tex.insert(END, "\n")
            tex.insert(END, iterations)
            tex.insert(END, "\n\n")

            coefficients = []
            function = []

    a = np.asmatrix(coefficients)
    b = np.asmatrix(list(map(float, function))).transpose()

    answer, iterations = functions[functciya](a.transpose().dot(a), a.transpose().dot(b), eps,
                                              conditions[conditciya])
    tex.insert(END, answer)
    tex.insert(END, "\n")
    tex.insert(END, iterations)


file_name = "matrix.txt"

root = Tk()
root.title("Hehe")
root.geometry("570x700")

but1 = Button(root, width=20)
but1["text"] = "Очистить"
but1.bind("<Button-1>", clean_frame)
but1.grid(column=0, row=0)

but2 = Button(root, width=25)
but2["text"] = "Выбрать файл с СЛАУ"
but2.bind("<Button-1>", start)
but2.grid(column=1, row=0)

but3 = Button(root, width=20)
but3["text"] = "Сохарнить результат"
but3.bind("<Button-1>", save_results)
but3.grid(column=2, row=0)

ent = Entry(root)
ent.insert(0, "0.001")
ent.grid(column=1, row=1)

canvas1 = Canvas(root, height=84, width=130)
photo1 = ImageTk.PhotoImage(Image.open("1.png"))
image1 = canvas1.create_image(0, 0, anchor='nw', image=photo1)
canvas1.grid(column=0, row=2, rowspan=4)

var = IntVar()
var.set(1)
rad1 = Radiobutton(root, text='Первая норма', variable=var, value=1).grid(column=1, row=2)
rad2 = Radiobutton(root, text='Вторая норма', variable=var, value=2).grid(column=1, row=3)
rad3 = Radiobutton(root, text='Третья норма', variable=var, value=3).grid(column=1, row=4)
rad4 = Radiobutton(root, text='Четвёртая норма', variable=var, value=4).grid(column=1, row=5)

canvas2 = Canvas(root, height=84, width=130)
photo2 = ImageTk.PhotoImage(Image.open("2.png"))
image2 = canvas2.create_image(0, 0, anchor='nw', image=photo2)
canvas2.grid(column=2, row=2, rowspan=4)

combo = Combobox(root)
combo['values'] = ("steepest_descent", "minimal_residual", "conjugation_gradients")
combo.current(0)
combo.grid(column=1, row=6)

tex = Text(root, width=30, height=28, font="Courier 12")
tex.grid(column=1, row=7)

root.mainloop()
