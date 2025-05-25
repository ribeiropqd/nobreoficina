import tkinter as tk
from tkinter import messagebox

class NobreOficinaApp:
    def __init__(self):
        self.produtos = [] # Lista para armazenar os produtos.
        self.usuarios = [] # Lista para armazenar os usuários cadastrados.

        self.janela = tk.Tk()
        self.janela.title("Nobre Oficina - Sistema de Cadastro")
        self.janela.geometry("400x300")
        self.janela.config(bg="white")

        # Menu
        menubar = tk.Menu(self.janela)
        
        menu_arquivo = tk.Menu(menubar, tearoff=0)
        menu_arquivo.add_command(label="Nova Janela", command=self.nova_janela)
        menu_arquivo.add_command(label="Sair", command=self.janela.quit)
        menubar.add_cascade(label="Opções", menu=menu_arquivo)
        # Área de Registro
        menu_registro = tk.Menu(menubar, tearoff=0)
        menu_registro.add_command(label="Registrar Produto", command=self.tela_registro)
        menubar.add_cascade(label="Registrar", menu=menu_registro)
        # Área de Ajuda
        menu_ajuda = tk.Menu(menubar, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.sobre)
        menubar.add_cascade(label="Ajuda", menu=menu_ajuda) 
        # Produtos
        menu_produtos = tk.Menu(menubar, tearoff=0)
        menu_produtos.add_command(label="Produtos Cadastrados", command=self.mostrar_produtos)
        menubar.add_cascade(label="Produtos", menu=menu_produtos)
        # Usuários
        menu_usuario = tk.Menu(menubar, tearoff=0)
        menu_usuario.add_command(label="Cadastre-se", command=self.tela_registro_usuario)
        menubar.add_cascade(label="Usuário", menu=menu_usuario)

        self.janela.config(menu=menubar)
        self.janela.mainloop()

    def nova_janela(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Nova Janela")
        nova.geometry("200x100")
        tk.Label(nova, text="Nova janela aberta!").pack

    def tela_registro(self):
        janela_registro = tk.Toplevel(self.janela)
        janela_registro.title("Registrar Produto")
        janela_registro.geometry("300x250")

        tk.Label(janela_registro, text="Nome do Produto: ").pack(pady=5)
        nome_entry = tk.Entry(janela_registro)
        nome_entry.pack()

        tk.Label(janela_registro, text="Descrição: ").pack(pady=5)
        desc_entry = tk.Entry(janela_registro)
        desc_entry.pack()

        tk.Label(janela_registro, text="Preço (R$): ").pack(pady=5)
        preco_entry = tk.Entry(janela_registro)
        preco_entry.pack()

        tk.Label(janela_registro, text="Quantidade: ").pack(pady=5)
        qnt_entry = tk.Entry(janela_registro)
        qnt_entry.pack()

        def salvar_produto():
            nome = nome_entry.get()
            desc = desc_entry.get()
            qnt = qnt_entry.get()
            try:
                preco = float(preco_entry.get())
            except ValueError:
                messagebox.showerror("Erro", "Preço deve ser um número.")
                return
            
            if nome and desc:
                self.produtos.append({'Nome': nome, 'descricao': desc, 'preco': preco, 'quantidade': qnt})
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                janela_registro.destroy()
            else:
                messagebox.showwarning("Aviso", "Preencha todos os campos.")
        
        tk.Button(janela_registro, text="Salvar", command=salvar_produto).pack(pady=15)

    def tela_registro_usuario(self):
        janela_usuario = tk.Toplevel(self.janela)
        janela_usuario.title("Registrar Usuário")
        janela_usuario.geometry("350x400")

        # Campos do Formulário.
        labels = ["Nome completo", "Email", "Telefone", "Data de Nascimento", "Endereço"]
        entradas = {}
        
        for label in labels:
            tk.Label(janela_usuario, text=label + ":").pack(pady=3)
            entrada = tk.Entry(janela_usuario, width=40)
            entrada.pack()
            entradas[label] = entrada

            def salvar_usuario():
                nome = entradas["Nome Completo"].get()
                email = entradas["Email"].get()
                telefone = entradas["Telefone"].get()
                nascimento = entradas["Nascimento"].get()
                endereco = entradas["Endereço"].get()
        
                if all([nome, email, telefone, nascimento, endereco]):
                    self.usuarios.append({
                        "nome": nome,
                        "email": email,
                        "telefone": telefone,
                        "nascimento": nascimento,
                        "endereço": endereco
                    })
                    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                    janela_usuario.destroy()
                else:
                    messagebox.showwarning("Aviso", "Preencha todos os campos.")
            
            tk.Button(janela_usuario, text="Salvar", command=salvar_usuario).pack(pady=15)

    def mostrar_produtos(self):
        janela_lista = tk.Toplevel(self.janela)
        janela_lista.title("Produtos Cadastrados")
        janela_lista.geometry("400x300")

        if not self.produtos:
            tk.Label(janela_lista, text="Nenhum produto cadastrado.").pack(pady=5)
            return
            
        lista = tk.Listbox(janela_lista, width=50)
        lista.pack(pady=10)

        for i, produto in enumerate(self.produtos):
            texto = f"{i+1}. {produto['Nome']} - {produto['descricao']} - R$ {produto['preco']:.2f}"
            lista.insert(tk.END, texto)

        def excluir_produto():
            selecao = lista.curselection()
            if selecao:
                index = selecao[0]
                nome_produto = self.produtos[index]["Nome"]
                confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Deseja excluir '{nome_produto}'?")
                if confirmacao:
                    del self.produtos[index]
                    lista.delete(index)
                    messagebox.showinfo("Excluido", "Produto excluido com sucesso.")
                else:
                    messagebox.showwarning("Aviso", "Selecione um produto para excluir.")
            
        tk.Button(janela_lista, text="Excluir Produto Selecionado", command=excluir_produto).pack(pady=10)

    def sobre(self):
        messagebox.showinfo("Sobre", "Sistema de Cadastro - Nobre Oficina\nDesenvolvido em Python com Tkinter.")
    

if __name__ == "__main__":
    NobreOficinaApp()
