import tkinter as tk

# Função que será chamada quando o botão for clicado
def mostrar_mensagem():
    label.config(text="Olá, Tkinter!")

# Cria uma instância da janela principal
janela = tk.Tk()
janela.title("Minha Tela Tkinter")  # Define o título da janela

# Cria um rótulo (label)
label = tk.Label(janela, text="Bem-vindo ao Tkinter!")
label.pack()  # Coloca o rótulo na janela

# Cria um botão
botao = tk.Button(janela, text="Clique em mim", command=mostrar_mensagem)
botao.pack()  # Coloca o botão na janela

# Inicia o loop de eventos da aplicação
janela.mainloop()