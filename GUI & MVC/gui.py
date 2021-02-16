# coding: utf-8
"""
    author: Louai KASSA BAGHDOUCHE

"""
from tkinter import Entry, Label, StringVar, Tk, Button, messagebox
from models import Person

ids = ["name", "last_name", "phone", "adresse", "city"]
bouton = ["chercher", "inserer", "effacer"]

def click(event):

    """ this function is used to implement placeholders in tkinter,
        since tkinter is pretty ugly and there is no a placeholder parameter
        in the Entry class.

    Args:
        event (click): when we click we can enter informations
    """
    for widget in widgets_entry.values():
        widget.config(stat='normal')
        widget.delete(0, 'end')


def initialize():

    """this functions is used to clear all entries
    """
    for idd in ids:
        widgets_entry[idd].delete(0, 'end')

def insert():
    """ Controller: this is an insertion method to control
        the insertion of new persons into our tsv file.
    """
    if (widgets_entry['name'].get() and
            widgets_entry['last_name'].get() and
            widgets_entry['city'].get()):

        individu = Person(
                        widgets_entry["name"].get(),
                        widgets_entry["last_name"].get(),
                        widgets_entry["phone"].get(),
                        widgets_entry["adresse"].get(),
                        widgets_entry["city"].get())

        if individu.already_exists():
            messagebox.askretrycancel('Already exists', 'The person already exists!')

        else:
            individu.insert_to_file()
            print('New person inserted succefully!')

    else:
        messagebox.showerror('Error', 'Name, Last name and city are required!')

def search():
    """ this method is used to search by name all the informations
        of a person stored in the tsv file.
    """

    if widgets_entry['name'].get():
        results = Person.search_person(widgets_entry['name'].get())

        if results[0]:
            messagebox.showinfo('Results', '%s results found:\n%s'%(str(results[1]), results[0]))

        else:
            messagebox.showwarning('No results', 'No results found!')

    else:
        messagebox.showerror('Error', 'Name are required!')
        initialize()

root = Tk()
root.title('Annuaire')
root['bg'] = '#fa6c61'

widgets_labs = {}
widgets_entry = {}
widgets_button = {}

i, j = 0, 0

for idi in ids:
    lab = Label(
        root,
        text=idi.title().replace('_', ' '),
        bg='#fa6c61',
        fg='white',
        font='Tahoma 11 bold')

    widgets_labs[idi] = lab
    lab.grid(row=i, column=0, padx=5, pady=5)

    var = StringVar()
    entry = Entry(root, text=var, bg='white', font='Tahoma 11 italic')

    # trying to implement a placeholde in the Entry field to be more aesthetic
    entry.insert(0, 'Enter your %s'%idi.title().replace('_', ' '))
    entry.config(state='disabled')
    # when we click we can enable the entry state in order to enter the informations
    entry.bind('<Button-1>', click)

    widgets_entry[idi] = entry
    entry.grid(row=i, column=1, padx=5, pady=5)

    i += 1

for idi in bouton:
    button = Button(root, text=idi, bg='#d65a4f', fg='white', font='Tahoma 10 bold', relief='flat')
    widgets_button[idi] = button
    button.grid(row=i+1, column=j, padx=5, pady=5)

    j += 1

widgets_button["inserer"].config(command=insert)
widgets_button["effacer"].config(command=initialize)
widgets_button["chercher"].config(command=search)

root.mainloop()
