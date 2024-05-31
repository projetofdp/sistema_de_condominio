from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from funcoesdb_encomendas import criar_banco_de_dados, adicionar_encomenda, buscar_encomenda, listar_encomendas


def adicionar_encomenda_interface():
    porteiro = porteiro_entry.get()
    destinatario = destinatario_entry.get()
    apartamento = apartamento_entry.get()
    adicionar_encomenda(porteiro, destinatario, apartamento)
    messagebox.showinfo("Sucesso", "Encomenda adicionada com sucesso!")
    atualizar_lista_encomendas()


def buscar_encomenda_interface():
    id_encomenda = id_encomenda_entry.get()
    nome_retirada = nome_retirada_entry.get()
    documento_retirada = documento_retirada_entry.get()
    buscar_encomenda(id_encomenda, nome_retirada, documento_retirada)
    messagebox.showinfo("Sucesso", "Encomenda buscada com sucesso!")
    atualizar_lista_encomendas()


def atualizar_lista_encomendas():
    for i in tree.get_children():
        tree.delete(i)

    encomendas = listar_encomendas()
    for encomenda in encomendas:
        tree.insert("", "end", values=encomenda)


def pesquisar_encomendas():
    query = search_entry.get()
    for i in tree.get_children():
        tree.delete(i)

    encomendas = listar_encomendas()
    for encomenda in encomendas:
        if query.lower() in str(encomenda).lower():
            tree.insert("", "end", values=encomenda)


# Cores
co1 = "#feffff"  # Branca
co6 = "#038cfc"  # azul

# Criação da janela principal
janela = Tk()
janela.title("Registro de Encomendas")
janela.geometry("1042x720")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=1280, height=50, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=1280, height=90, bg=co1)
frame_dados.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=4, columnspan=1, ipadx=720)

frame_pesquisa = Frame(janela, width=1280, height=50, bg=co1)
frame_pesquisa.grid(row=5, column=0, pady=0, padx=20, sticky=NSEW)

frame_tabela = Frame(janela, width=1280, height=400, bg=co1)
frame_tabela.grid(row=6, column=0, pady=0, padx=20, sticky=NSEW)

# Frame para dividir as entrys de cadastro e de retirada
frame_linha = Frame(frame_dados, width=55, height=5, bg=co1)
frame_linha.grid(row=6, column=4, pady=0, padx=10, sticky=NSEW)
# Frame para criar espaço no lado esquerdo das entrys
frame_linha = Frame(frame_dados, width=55, height=0, bg=co1)
frame_linha.grid(row=6, column=0, pady=0, padx=0, sticky=NSEW)

# Frame Logo
app_lg = Image.open('logo_encomendas.png')
app_lg = app_lg.resize((45, 45))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Registro de Encomendas", width=1280, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)

# Seção de Cadastro de Encomenda
Label(frame_dados, text="", bg=co1).grid(row=1, column=1, pady=0, padx=0, sticky=NSEW)

Label(frame_dados, text="Porteiro:", bg=co1, anchor=NW).grid(row=2, column=1, pady=0, padx=0, sticky=NSEW)
porteiro_entry = Entry(frame_dados, width=21)
porteiro_entry.grid(row=2, column=2)

Label(frame_dados, text="Destinatário:", bg=co1, anchor=NW).grid(row=3, column=1, pady=0, padx=0, sticky=NSEW)
destinatario_entry = Entry(frame_dados, width=21)
destinatario_entry.grid(row=3, column=2)

Label(frame_dados, text="Apartamento:", bg=co1, anchor=NW).grid(row=4, column=1, pady=0, padx=0, sticky=NSEW)
apartamento_entry = Entry(frame_dados, width=21)
apartamento_entry.grid(row=4, column=2)

Button(frame_dados, text="Adicionar Encomenda", width=18, overrelief=RIDGE, command=adicionar_encomenda_interface).grid(row=5, column=2, columnspan=2)

# Seção de Retirada de Encomenda
Label(frame_dados, text="ID da Encomenda:", bg=co1, anchor=NW).grid(row=2, column=5, pady=0, padx=0, sticky=NSEW)
id_encomenda_entry = Entry(frame_dados, width=21)
id_encomenda_entry.grid(row=2, column=6)

Label(frame_dados, text="Nome de Quem Retirou:", bg=co1, anchor=NW).grid(row=3, column=5, pady=0, padx=0, sticky=NSEW)
nome_retirada_entry = Entry(frame_dados, width=21)
nome_retirada_entry.grid(row=3, column=6)

Label(frame_dados, text="Documento de Identificação (CPF/RG):", bg=co1, anchor=NW).grid(row=4, column=5, pady=0, padx=0, sticky=NSEW)
documento_retirada_entry = Entry(frame_dados, width=21)
documento_retirada_entry.grid(row=4, column=6)

Button(frame_dados, text="Buscar Encomenda", width=18, overrelief=RIDGE, command=buscar_encomenda_interface).grid(row=5, column=6, columnspan=2)

# Seção de Pesquisa
Label(frame_pesquisa, text="", bg=co1).grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

Label(frame_pesquisa, text="Pesquisar:", bg=co1, anchor=NW).grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)
search_entry = Entry(frame_pesquisa, width=30)
search_entry.grid(row=1, column=1, pady=0, padx=10, sticky=NSEW)

Button(frame_pesquisa, text="Pesquisar", width=15, overrelief=RIDGE, command=pesquisar_encomendas).grid(row=1, column=2, pady=0, padx=10, sticky=NSEW)

Label(frame_pesquisa, text="", bg=co1).grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

# Seção de Lista de Encomendas
tree = ttk.Treeview(frame_tabela, columns=("ID", "Porteiro", "Destinatário", "Apartamento", "Data/Hora Entrega", "Nome Retirada", "Documento Retirada", "Data/Hora Retirada",), height=21, selectmode="extended", show='headings')

tree.heading("ID", text="ID")
tree.heading("Porteiro", text="Porteiro")
tree.heading("Destinatário", text="Destinatário")
tree.heading("Data/Hora Entrega", text="Data/Hora Entrega")
tree.heading("Apartamento", text="Apartamento")
tree.heading("Nome Retirada", text="Nome Retirada")
tree.heading("Documento Retirada", text="Documento Retirada")
tree.heading("Data/Hora Retirada", text="Data/Hora Retirada")
tree.grid(row=9, column=0, columnspan=2)

tree.column("ID", width=50)
tree.column("Porteiro", width=100)
tree.column("Destinatário", width=110)
tree.column("Apartamento", width=110)
tree.column("Data/Hora Entrega", width=150)
tree.column("Nome Retirada", width=150)
tree.column("Documento Retirada", width=170)
tree.column("Data/Hora Retirada", width=160)


# Inicializar o banco de dados e a lista de encomendas
criar_banco_de_dados()
atualizar_lista_encomendas()

janela.mainloop()

