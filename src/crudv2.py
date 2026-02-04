#______________________________________________________#

'''

                     CRUDZÃO 2.0


'''
#______________________________________________________#



#------------------------------------------------------------------------------------#




#______________________________________________________#


#                     BIBLIOTECAS

#______________________________________________________#


import mysql.connector
import customtkinter as ctk
from customtkinter import *
from tkinter import *
import tkcalendar
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import ttk





#______________________________________________________#





#------------------------------------------------------------------------------------#









#______________________________________________________#


#                     BACKEND

#______________________________________________________#



class Functions:





    def database(self):
        
        self.conexao = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'bdcrud'
        )
        self.cursor = self.conexao.cursor()
        
        
        
        
        
    def coletar_dados(self):
        
        self.id = self.entrada_id.get()
        self.nome = self.entrada_nome.get()
        self.email = self.entrada_email.get()
        self.telefone = self.entrada_telefone.get()
        self.data = self.entrada_data.get()
        self.estado = self.entrada_estado.get()
        self.sobre = self.entrada_sobre.get()
    
        
        
    def limpar_campos(self):
        
        self.entrada_id.delete(0, END)
        self.entrada_nome.delete(0, END)
        self.entrada_email.delete(0, END)
        self.entrada_telefone.delete(0, END)
        self.entrada_data.delete(0, END)
        self.entrada_estado.delete(0, END)
        self.entrada_sobre.delete(0, END)
        
    def enviaraobanco(self):
        
        self.database()
        self.coletar_dados()

        self.queryinsert = """
        INSERT INTO dados
        (nome, email, telefone, data, estado, sobre)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.valores = (self.nome, self.email, self.telefone, self.data, self.estado, self.sobre)

        self.cursor.execute(self.queryinsert, self.valores)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
        self.limpar_campos()
        self.carregar_dados()
        
        
        
        
        
    def carregar_dados(self):
        
        self.database()
        self.cursor.execute("SELECT * FROM dados")
        resultados = self.cursor.fetchall()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in resultados:
            self.tree.insert("", END, values=row)
        self.cursor.close()
        self.conexao.close()
        
        
        
    def acaoinserir(self):
        
        self.database()
        self.coletar_dados()
        self.enviaraobanco()
        self.carregar_dados()
        
        
    def duploclique(self, event):
        self.limpar_campos()

        item = self.tree.selection()
        if not item:
            return
    
        values = self.tree.item(item, "values")
    
        self.selected_id = values[0]
    
        id_, nome, email, telefone, data, estado, sobre = values
    
        self.entrada_id.configure(state="normal")
        self.entrada_id.insert(0, id_)
        self.entrada_id.configure(state="disabled")
    
        self.entrada_nome.insert(0, nome)
        self.entrada_email.insert(0, email)
        self.entrada_telefone.insert(0, telefone)
    
        self.entrada_data.insert(0, data)
        self.entrada_estado.insert(0, estado)
        self.entrada_sobre.insert(0, sobre)

    
            
    def update(self):
        
        self.coletar_dados()

        if not hasattr(self, 'selected_id') or not self.selected_id:
            print("Selecione um registro para atualizar.")
            return

        self.database()
        self.cursor.execute(
            """
            UPDATE dados
            SET nome = %s, email = %s, telefone = %s, data = %s, estado = %s, sobre = %s
            WHERE id = %s
            """,
            (self.nome, self.email, self.telefone, self.data, self.estado, self.sobre, self.selected_id)
        )
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
        self.limpar_campos()
        self.carregar_dados()
        
        
        
    def deletar(self):
        
        self.coletar_dados()
        if not self.selected_id:
            return
        self.database()
        try:
            self.cursor.execute("DELETE FROM dados WHERE id = %s", (int(self.selected_id),))
            self.conexao.commit()
        finally:
            self.cursor.close()
            self.conexao.close()
        self.limpar_campos()
        self.carregar_dados()
        
        
        
        
        
        
        

        
    
        
        
        
    
        
        
        
        
        
    

















#______________________________________________________#









#------------------------------------------------------------------------------------#












#______________________________________________________#


#                     FRONTEND

#______________________________________________________#




class App(Functions):
    
    def __init__(self):

        self.app = ctk.CTk()


        # CONFIGURAÇÃO DA JANELA
        
        
        self.app.geometry("1500x700")
        self.app.resizable(False, False)


        # CONSTRUTOR
        
        self.database()
        self.frames()
        self.labels()
        self.entries()
        self.botoes()
        self.treeview()
        self.carregar_dados()
        




    #---------------------------#
    #          FRAMES
    #---------------------------#
    
    
    
    def frames(self):
        
        
        self.frameleft = CTkFrame(
            self.app,
            fg_color="white",
            bg_color="transparent",
            corner_radius=20
        )
        self.frameleft.place(relx=0.01, rely=0.01, relwidth=0.3, relheight=0.98)
        
        self.frameright = CTkFrame(
            self.app,
            fg_color="white",
            bg_color="transparent",
            corner_radius=20
        )
        self.frameright.place(relx=0.32, rely=0.01, relwidth=0.673, relheight=0.98)
        
        
    def labels(self):
        
        self.nometopo = CTkLabel(
            self.frameleft,
            text="FORMULÁRIO DE CONSULTA",
            font=("segoe IU", 20, "bold"),
            text_color="black"

        )
        self.nometopo.place(relx=0.18, rely = 0.08)
        
        
        
        self.labelnome = CTkLabel(
            self.frameleft,
            text="NOME *",
            font=("segoe IU", 15, "bold"),
            text_color="black"

        )
        self.labelnome.place(relx=0.1, rely = 0.20)
        
        
        
        
        self.labelemail = CTkLabel(
            self.frameleft,
            text="EMAIL *",
            font=("segoe IU", 15, "bold"),
            text_color="black"

        )
        self.labelemail.place(relx=0.1, rely = 0.35)
        
        
        self.labeltelefone = CTkLabel(
            self.frameleft,
            text="TELEFONE *",
            font=("segoe IU", 15, "bold"),
            text_color="black"

        )
        self.labeltelefone.place(relx=0.1, rely = 0.50)
        
        
        
        self.labelconsulta = CTkLabel(
            self.frameleft,
            text="DATA DA CONSULTA *",
            font=("segoe IU", 15, "bold"),
            text_color="black"

        )
        self.labelconsulta.place(relx=0.1, rely = 0.65)
        
        
        self.labelestado = CTkLabel(
            self.frameleft,
            text="ESTADO DA CONSULTA *",
            font=("segoe IU", 15, "bold"),
            text_color="black"

        )
        self.labelestado.place(relx=0.52, rely = 0.65)
        
        
        
        
        self.labelsobre = CTkLabel(
            self.frameleft,
            text="CONSULTA SOBRE *",
            font=("segoe IU", 15, "bold"),
            text_color="black"

        )
        self.labelsobre.place(relx=0.1, rely = 0.75)
        
        
        
        
        
    def entries(self):
        
        self.entrada_nome = CTkEntry(
            self.frameleft,
            corner_radius= 15,
            placeholder_text="Insira o nome",
            placeholder_text_color="#7A7A7A",
            bg_color="white",
            border_color="#999999",
            border_width=2,
            text_color="black",
            fg_color="#ebebeb"
        )
        self.entrada_nome.place(relx=0.08, rely = 0.25, relwidth=0.7, relheight=0.06)
        
        
        self.entrada_email = CTkEntry(
            self.frameleft,
            corner_radius= 15,
            placeholder_text="Insira o email",
            placeholder_text_color="#7A7A7A",
            bg_color="white",
            border_color="#999999",
            border_width=2,
            text_color="black",
            fg_color="#ebebeb"
        )
        self.entrada_email.place(relx=0.08, rely = 0.40, relwidth=0.7, relheight=0.06)
        
        
        
        self.entrada_telefone = CTkEntry(
            self.frameleft,
            corner_radius= 15,
            placeholder_text="Insira o telefone",
            placeholder_text_color="#7A7A7A",
            bg_color="white",
            border_color="#999999",
            border_width=2,
            text_color="black",
            fg_color="#ebebeb"
        )
        self.entrada_telefone.place(relx=0.08, rely = 0.55, relwidth=0.7, relheight=0.06)
        
        
        self.entrada_sobre = CTkEntry(
            self.frameleft,
            corner_radius= 15,
            placeholder_text="Insira o telefone",
            placeholder_text_color="#7A7A7A",
            bg_color="white",
            border_color="#999999",
            border_width=2,
            text_color="black",
            fg_color="#ebebeb"
        )
        self.entrada_sobre.place(relx=0.08, rely = 0.8, relwidth=0.7, relheight=0.06)
        
        
        
        
        
        self.entrada_estado = CTkEntry(
            self.frameleft,
            corner_radius= 15,
            placeholder_text="",
            placeholder_text_color="#7A7A7A",
            bg_color="white",
            border_color="#999999",
            border_width=2,
            text_color="black",
            fg_color="#ebebeb"
        )
        self.entrada_estado.place(relx=0.5, rely = 0.7, relwidth=0.45, relheight=0.06)
        
        
        
        
        
        
        self.entrada_data = DateEntry(
            self.frameleft,
            date_pattern="yyyy-mm-dd",
        )
        self.entrada_data.place(relx=0.12, rely = 0.7, relwidth=0.22, relheight=0.04)
        
        
        
        
        self.entrada_id = CTkEntry(
            self.frameleft,
            corner_radius= 15,
            placeholder_text="ID",
            placeholder_text_color="#7A7A7A",
            bg_color="white",
            border_color="#999999",
            border_width=2,
            text_color="black",
            fg_color="#ebebeb"
        )
        self.entrada_id.place(relx=0.8, rely = 0.19, relwidth=0.15, relheight=0.05)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def botoes(self):
        
        self.botao_inserir = CTkButton(
            self.frameleft,
            text="INSERIR",
            font=("segoe IU", 20, "bold"),
            text_color="white",
            corner_radius=15,
            bg_color="white",
            fg_color="#2ed5ff",
            hover_color="#2696b3",
            command=self.acaoinserir
        )
        self.botao_inserir.place(relx=0.03, rely = 0.9, relwidth=0.3, relheight=0.06)
        
        
        self.botao_atualizar = CTkButton(
            self.frameleft,
            text="ATUALIZAR",
            font=("segoe IU", 20, "bold"),
            text_color="white",
            corner_radius=15,
            bg_color="white",
            fg_color="#2eff51",
            hover_color="#1d9631",
            command=self.update
        )
        self.botao_atualizar.place(relx=0.35, rely = 0.9, relwidth=0.3, relheight=0.06)
        
        
        self.botao_deletar = CTkButton(
            self.frameleft,
            text="DELETAR",
            font=("segoe IU", 20, "bold"),
            text_color="white",
            corner_radius=15,
            bg_color="white",
            fg_color="#ff0000",
            hover_color="#880000",
            command=self.deletar
        )
        self.botao_deletar.place(relx=0.67, rely = 0.9, relwidth=0.3, relheight=0.06)



    def treeview(self):

        lista_header = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Sobre']

        self.tree = ttk.Treeview(
        self.frameright,
        selectmode="extended",
        columns=lista_header,
        show="headings"
        )

   
        vsb = ttk.Scrollbar(
        self.frameright,
        orient="vertical",
        command=self.tree.yview
        )
        hsb = ttk.Scrollbar(
        self.frameright,
        orient="horizontal",
        command=self.tree.xview
        )

        self.tree.configure(
        yscrollcommand=vsb.set,
        xscrollcommand=hsb.set
    )

    # Cabeçalhos e colunas
        for col in lista_header:
         self.tree.heading(col, text=col)
         self.tree.column(col, anchor="center", width=120)

    # Layout
        self.tree.place(relx=0.04, rely=0.05, relwidth=0.9, relheight=0.9)
        vsb.place(relx=0.94, rely=0.05, relheight=0.88)
        hsb.place(relx=0.05, rely=0.95, relwidth=0.88)

        
        self.tree.bind("<Double-1>", self.duploclique)

        















    def run(self):
        self.app.mainloop()


























if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.run()


#______________________________________________________#









#------------------------------------------------------------------------------------#





# PRINCIPIOS DO CRUD

'''
comando = ''
cursor.execute(comando) 
conexao.commit() # edita o banco de dados
resultado = cursor.fetchall() # ler o banco de dados






'''

'''
conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'bdcrud'
)

cursor = conexao.cursor()






# CREATE


nome = "Pedro"
cpf = "12345678910"
comando_um = "INSERT INTO dados (nome, cpf) VALUES (%s, %s)"
valores = ("Pedro", "12345678910")
cursor.execute(comando_um, valores)
conexao.commit()




# READ


comando_dois = 'SELECT * FROM dados'
cursor.execute(comando_dois)
resultado = cursor.fetchall()
print(resultado)



# UPDATE



valores_2 = ("Pedro", 1)
comando_3 = 'UPDATE dados SET nome = %s WHERE ID = %s'
cursor.execute(comando_3, valores_2)
conexao.commit()











cursor.close()
conexao.close()




'''