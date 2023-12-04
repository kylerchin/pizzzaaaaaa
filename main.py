#Kyler Chin
#2023-03

import tkinter as tk
from tkinter import ttk, Button

def update_receipt():
    # Build receipt based on user's selections
    initprice = 0

    match size_var.get():
        case "Small":
            initprice = 10.99
        case "Medium":
            initprice = 12.99
        case "Large":
            initprice = 14.99

    toppings = []
    
    if cheese_var.get():
        toppings.append("Cheese $1.25")
    if pepperoni_var.get():
        toppings.append("Pepperoni $1.25")
    if sausage_var.get():
        toppings.append("Sausage $1.25")
    if mushrooms_var.get():
        toppings.append("Mushrooms $1.25")
    if onions_var.get():
        toppings.append("Onions $1.25")

    
    subprice = (len(toppings) * 1.25) + initprice

    receipt_text = "Receipt:\n"
    receipt_text += "Size: {}\n".format(size_var.get())
    receipt_text += "Base cost: {:.2f}\n".format(initprice)
    receipt_text += "Toppings: {}\n".format(", ".join(toppings))
    receipt_text += "Crust: {}\n".format(crust_var.get())
    receipt_text += "Subtotal: {:.2f}\n".format(subprice)
    receipt_text += "Tax: {:.2f}\n".format(subprice * 0.0875)
    receipt_text += "Total: {:.2f}\n".format(subprice * 1.0875)

    # Update receipt label
    receipt_label.config(text=receipt_text)

def update_size(size):
    global size_state
    size_state = size
    print(f"Size selected: {size}")

root = tk.Tk()
root.title("Pizza Size Selection")

size_options = {"Small": "small.png", "Medium": "medium.png", "Large": "large.png"}
size_images = {}
size_labels = {}

for size, image_filename in size_options.items():
     # Load the original image
    original_image = tk.PhotoImage(file=image_filename)

    # Resize the image by 0.25x
    resized_image = original_image.subsample(4, 4)
    size_images[size] = resized_image

    # Create a label for the text
    size_labels[size] = tk.Label(root, text=size)
size_state = "Small"  # Initial size state

# Size Type
size_var = tk.StringVar()
size_var.set("Medium")

# Create radio buttons for each size option
small_radio = ttk.Radiobutton(root, image=size_images["Small"], variable=size_var, value="Small")
medium_radio = ttk.Radiobutton(root,  image=size_images["Medium"], variable=size_var, value="Medium")
large_radio = ttk.Radiobutton(root, image=size_images["Large"],  variable=size_var, value="Large")

small_radio.pack()
medium_radio.pack()

large_radio.pack()

# Pizza Toppings
cheese_var = tk.IntVar(value=1)
pepperoni_var = tk.IntVar()
sausage_var = tk.IntVar()
mushrooms_var = tk.IntVar()
onions_var = tk.IntVar()

# Crust Type
crust_var = tk.StringVar()
crust_var.set("Hand-tossed")

# Toppings Subheading
toppings_label = tk.Label(root, text="Toppings")
toppings_label.pack()

# Create Checkboxes for Toppings

cheese_checkbox = tk.Checkbutton(root, text="Cheese", variable=cheese_var)
pepperoni_checkbox = tk.Checkbutton(root, text="Pepperoni", variable=pepperoni_var)
sausage_checkbox = tk.Checkbutton(root, text="Sausage", variable=sausage_var)
mushrooms_checkbox = tk.Checkbutton(root, text="Mushrooms", variable=mushrooms_var)
onions_checkbox = tk.Checkbutton(root, text="Onions", variable=onions_var)
cheese_checkbox.pack()
pepperoni_checkbox.pack()
sausage_checkbox.pack()
mushrooms_checkbox.pack()
onions_checkbox.pack()

toppings_label = tk.Label(root, text="Crust Type")
toppings_label.pack()

# Create Radio Buttons for Crust Type
hand_tossed_radio = tk.Radiobutton(root, text="Hand-tossed", variable=crust_var, value="Hand-tossed")
deep_dish_radio = tk.Radiobutton(root, text="Deep-dish", variable=crust_var, value="Deep-dish")
thin_crust_radio = tk.Radiobutton(root, text="Thin-crust", variable=crust_var, value="Thin-crust")

hand_tossed_radio.pack()
deep_dish_radio.pack()
thin_crust_radio.pack()


# Create Submit Button
submit_button = tk.Button(root, text="Update Receipt:", command=update_receipt)
submit_button.pack()


# Create Receipt Label
receipt_label = tk.Label(root, text="Receipt:\n")
receipt_label.pack()

root.mainloop()