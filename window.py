import tkinter as tk
import find


def name():
    inp = entry_name.get()
    p = entry_path.get()
    if inp:
        if p:
            res = find.find_by_name(namef=inp, path=p)
        else:
            res = find.find_by_name(namef=inp)
        var = tk.StringVar(value=res[:-1])
        listbox = tk.Listbox(listvariable=var)
        listbox.grid(column=0, row=7, stick='we', columnspan=6, rowspan=5)
        lab = tk.Label(win, text=res[-1])
        lab.grid(column=0, row=13)
    else:
        pass


def regex():
    inp = entry_regex.get()
    p = entry_path.get()
    if inp:
        if p:
            res = find.find_by_regex(regex=inp, path=p)
        else:
            res = find.find_by_regex(regex=inp)
        var = tk.StringVar(value=res[:-1])
        listbox = tk.Listbox(listvariable=var)
        listbox.grid(column=0, row=6, stick='we', columnspan=6, rowspan=5)
        lab = tk.Label(win, text=res[-1])
        lab.grid(column=0, row=12)
    else:
        pass


def date():
    inp1 = entry_date1.get()
    inp2 = entry_date2.get()
    p = entry_path.get()
    if inp1 and inp2:
        if p:
            res = find.find_by_date(first_date=inp1, second_date=inp2, path=p)
        else:
            res = find.find_by_date(first_date=inp1, second_date=inp2)
        var = tk.StringVar(value=res[:-1])
        listbox = tk.Listbox(listvariable=var)
        listbox.grid(column=0, row=6, stick='we', columnspan=6, rowspan=5)
        lab = tk.Label(win, text=res[-1])
        lab.grid(column=0, row=12)
    else:
        pass


def size():
    inp1 = entry_size1.get()
    inp2 = entry_size2.get()
    p = entry_path.get()
    if inp1 and inp2:
        if p:
            res = find.find_by_size(min_size=inp1, max_size=inp2, path=p)
        else:
            res = find.find_by_size(min_size=inp1, max_size=inp2)
        var = tk.StringVar(value=res[:-1])
        listbox = tk.Listbox(listvariable=var)
        listbox.grid(column=0, row=6, stick='we', columnspan=6, rowspan=5)
        lab = tk.Label(win, text=res[-1])
        lab.grid(column=0, row=12)
    else:
        pass


win = tk.Tk()
win.title('FileFind')
win.geometry('1100x400')
photo = tk.PhotoImage(file='logo.png')
win.iconphoto(False, photo)
label_privet = tk.Label(win, text='Найти файлы по')
label_name = tk.Label(win, text='названию:')
label_regex = tk.Label(win, text='регулярному выражению:')
label_date = tk.Label(win, text='дате:')
label_size = tk.Label(win, text='размеру:')
label_dod = tk.Label(win, text=' до ')
label_dos = tk.Label(win, text=' до ')
label_path = tk.Label(win, text='Введите путь:')
label_spr = tk.Label(win, text='Дату вводить в формате ГГГГ.ММ.ДД, размер: (число) (б, кб, мб и тд)')
entry_name = tk.Entry(win)
entry_regex = tk.Entry(win)
entry_date1 = tk.Entry(win)
entry_date2 = tk.Entry(win)
entry_size1 = tk.Entry(win)
entry_size2 = tk.Entry(win)
entry_path = tk.Entry(win)
button_name = tk.Button(win, text='Найти', command=name)
button_regex = tk.Button(win, text='Найти', command=regex)
button_date = tk.Button(win, text='Найти', command=date)
button_size = tk.Button(win, text='Найти', command=size)
label_privet.grid(column=0, row=0, stick='w')
label_name.grid(column=0, row=1, stick='w')
label_regex.grid(column=0, row=2, stick='w')
label_date.grid(column=0, row=3, stick='w')
label_size.grid(column=0, row=4, stick='w')
label_path.grid(column=0, row=5, stick='w')
label_spr.grid(column=0, row=6, stick='w')
entry_name.grid(column=1, row=1, stick='w')
entry_regex.grid(column=1, row=2, stick='w')
entry_date1.grid(column=1, row=3, stick='w')
label_dod.grid(column=2, row=3, stick='w')
entry_date2.grid(column=3, row=3, stick='w')
entry_size1.grid(column=1, row=4, stick='w')
label_dos.grid(column=2, row=4, stick='w')
entry_size2.grid(column=3, row=4, stick='w')
entry_path.grid(column=1, row=5, stick='w')
button_name.grid(column=4, row=1, stick='w')
button_regex.grid(column=4, row=2, stick='w')
button_date.grid(column=4, row=3, stick='w')
button_size.grid(column=4, row=4, stick='w')


if __name__ == '__main__':
    win.mainloop()
