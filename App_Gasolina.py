import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT

root = tk.Tk()


root.title("Cálculo da Gasolina")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

window_width = 250
window_height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_X = int(screen_width / 2 - window_width / 2)
center_Y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_X}+{center_Y}')



label_Dist = tk.Label(root, text = "Distância em\numa viagem")
label_Dist.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
Dist = tk.Entry()
Dist.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)



n_viagens_label = tk.Label(root, text = "Nº de Viagens")
n_viagens_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
n_viagens = tk.Entry()
n_viagens.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)



label_km_L = tk.Label(root, text = "Km/L")
label_km_L.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
km_L = tk.Entry()
km_L.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)



label_preco_gas = tk.Label(root, text = "Preço\ncombustível/L")
label_preco_gas.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
preco_gas = tk.Entry()
preco_gas.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


botao = tk.Button(root, text = "Calcule")
botao.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)


print("oi")

root.mainloop()
