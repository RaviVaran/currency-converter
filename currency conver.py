import tkinter as tk
import requests


def convert_currency():
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = float(amount_entry.get())

    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    if response.status_code == 200: # The request was successful  and the server has returned the requested data.
        result = response.json()['rates'][to_currency] * amount
        result_label.config(text=f"{amount} {from_currency} is {result:.2f} {to_currency}")
    else:
        result_label.config(text="Unable to convert currencies.")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x400")

# Create and arrange the input widgets
from_currency_label = tk.Label(window, text="Convert from:",fg="red")
from_currency_label.pack()

from_currency_entry = tk.Entry(window)
from_currency_entry.pack()

to_currency_label = tk.Label(window, text="Convert to:",fg="red")
to_currency_label.pack()

to_currency_entry = tk.Entry(window)
to_currency_entry.pack()

amount_label = tk.Label(window, text="Amount:",fg="red")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()

convert_button = tk.Button(window, text="Convert",fg="red", command=convert_currency)
convert_button.pack()

result_label = tk.Label(window, text="",fg="green")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
