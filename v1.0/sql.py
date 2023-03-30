import pyodbc
import tkinter as tk

root=tk.Tk()
root.geometry("300x300")
root.title("Conexion a base de datos prueba")

label1=tk.Label(text="Server Name")
label1.pack()
Entry1=tk.Entry()   
Entry1.pack()
label2=tk.Label(text="DataBase")
label2.pack()
Entry2=tk.Entry()
Entry2.pack()
label3=tk.Label(text="Respuesta")
label3.place(x=200,y=200)

def conexionSql():
    try:
        connection=pyodbc.connect('Driver={SQL Server};SERVER='+Entry1.get()+';DATABASE='+Entry2.get()+';Trusted_Connection=yes;')
        label3.config(text="Conexion Exitosa")
    except:
        label3.config(text="Error al intentar conectarse")
       

button1=tk.Button(root,text="Ingresar",command=conexionSql)
button1.bind("<Button-1>",conexionSql)
button1.pack()
root.mainloop()
