import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import Menu
from tkinter import messagebox

class BentfordApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Bem vindo ao app do squad Bentford")
        self.geometry('650x400')
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageAdicionarContato, PageRemoverContato, PageBuscarContato, PageBuscarContato, PageExportarContatos):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        
        menu = Menu(self)
        new_item = Menu(menu, tearoff=0)

        new_item.add_command(label='Adicionar contato', command=lambda: self.show_frame("PageAdicionarContato"))

        new_item.add_command(label='Remover contato', command=lambda: self.show_frame("PageRemoverContato"))

        new_item.add_separator()

        new_item.add_command(label='Buscar contato', command=lambda: self.show_frame("PageBuscarContato"))

        new_item.add_separator()

        new_item.add_command(label='Exportar contatos', command=lambda: self.show_frame("PageExportarContatos"))

        new_item.add_separator()

        new_item.add_command(label='Fechar', command=self.quit)

        menu.add_cascade(label='File', menu=new_item)

        self.config(menu=menu)
        

        

        self.show_frame("StartPage")
    
    def messagbox(self):
        tk.messagebox.showinfo(title="Ok", message="yo")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Aqui a historia começa...", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


class PageRemoverContato(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Remover contato", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Remover",
                           command=lambda: tk.messagebox.showinfo(title="Ok", message="yo"))
        button.pack()


class PageAdicionarContato(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Adicionar contato", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Adicionar",
                           command=lambda: tk.messagebox.showinfo(title="Ok", message="yo"))
        button.pack()

class PageBuscarContato(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Buscar contato", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Buscar",
                           command=lambda: tk.messagebox.showinfo(title="Ok", message="yo"))
        button.pack()

class PageExportarContatos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Exportar Contatos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Exportar",
                           command=lambda: tk.messagebox.showinfo(title="Ok", message="yo"))
        button.pack()

if __name__ == "__main__":
    app = BentfordApp()
    app.mainloop()