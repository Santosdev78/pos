import tkinter as tk
import math

class Calculadora:
    def __init__(self):
        self.app_calculadora = tk.Tk()
        self.app_calculadora.geometry("550x600")
        self.app_calculadora.title("CALCULADORA ITLA")
        self.app_calculadora.configure(bg="pink")

        self.pantalla = tk.Entry(self.app_calculadora, width=70, borderwidth=10)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        
        botones_num_y_op = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            "0", '.', '=', '+',
            '√', 'sin', 'cos', 'tan'
        ]
        
        fila = 1
        columna = 0
        for boton in botones_num_y_op:
            tk.Button(self.app_calculadora, text=boton, padx=30, pady=30,
                    command=lambda x=boton: self.botones_no_basicos(x)).grid(row=fila, column=columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

        tk.Button(self.app_calculadora, text="♡", padx=30, pady=30,
                  command=self.borrar_resultado_ant).grid(row=6, column=0)

        self.app_calculadora.mainloop()
        
    def borrar_resultado_ant(self):
        self.pantalla.delete(0, tk.END)
    
    def botones_no_basicos(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, resultado)
            except Exception as error:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Ocurrio un error")
        elif valor == "♡": 
            self.borrar_resultado_ant()
        elif valor in ['√', 'sin', 'cos', 'tan']:
            try:
                valor_actual = self.pantalla.get()
                if valor_actual:
                    if valor == '√':
                        resultado = math.sqrt(float(valor_actual))
                    elif valor == 'sin':
                        resultado = math.sin(math.radians(float(valor_actual)))
                    elif valor == 'cos':
                        resultado = math.cos(math.radians(float(valor_actual)))
                    elif valor == 'tan':
                        resultado = math.tan(math.radians(float(valor_actual)))
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, resultado)
                else:
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, "Debe ingresar un valor")
            except Exception as error:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error: " + str(error))
        else:
            self.pantalla.insert(tk.END, valor)

if __name__ == "__main__":
    calculadora = Calculadora()