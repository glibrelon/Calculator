import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT
from tkinter import messagebox

def calculate():
    single_travel_distance = float(Dist.get())
    n_ride = float(n_viagens.get())
    total_distance_traveled = single_travel_distance * n_ride
    car_efficiency = float(km_L.get())
    gas_price = float(price_gas.get())
    calculo = (total_distance_traveled / car_efficiency ) * gas_price

    return messagebox.showinfo('message', f'R$ {calculo:.2f}')

root = tk.Tk()


# Title and window format
root.title( "Cálculo da Gasolina" )

root.columnconfigure( 0, weight=1 )
root.columnconfigure( 1, weight=3 )

window_width = 250
window_height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_X = int( screen_width / 2 - window_width / 2 )
center_Y = int( screen_height / 2 - window_height / 2 )

root.geometry( f'{window_width}x{window_height}+{center_X}+{center_Y}' )



# Data entries
    
    # Distance of a ride entry
label_Dist = tk.Label( root, text = "Distância em\numa viagem" )
label_Dist.grid( column=0, row=0, sticky=tk.W, padx=5, pady=5 )
Dist =  tk.Entry()
Dist.grid( column=1, row=0, sticky=tk.W, padx=5, pady=5 )


    # Total travels
n_viagens_label = tk.Label( root, text = "Nº de Viagens" )
n_viagens_label.grid( column=0, row=1, sticky=tk.W, padx=5, pady=5 )
n_viagens = tk.Entry()
n_viagens.grid( column=1, row=1, sticky=tk.W, padx=5, pady=5 )


    # Car Performance
label_km_L = tk.Label( root, text = "Km/L" )
label_km_L.grid( column=0, row=2, sticky=tk.W, padx=5, pady=5 )
km_L = tk.Entry()
km_L.grid( column=1, row=2, sticky=tk.W, padx=5, pady=5 )


    # Gas Price per liter
label_preco_gas = tk.Label( root, text = "Preço\ncombustível/L" )
label_preco_gas.grid( column=0, row=3, sticky=tk.W, padx=5, pady=5 )
price_gas = tk.Entry()
price_gas.grid ( column=1, row=3, sticky=tk.W, padx=5, pady=5 )


# Button
button = tk.Button( root, text = "Calcule", command = calculate )
button.grid( column=1, row=5, sticky=tk.W, padx=5, pady=5 )



root.mainloop()
