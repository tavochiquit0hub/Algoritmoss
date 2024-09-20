import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import math


# Función para redimensionar la imagen
def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height), Image.ANTIALIAS)


# Función para ajustar las imágenes a 16:9 y 4:3
def adjust_image_aspect_ratios(image_path):
    image = Image.open(image_path)
    y_res = image.height

    # 16:9 aspect ratio
    new_x_16_9 = math.ceil((16 / 9) * y_res)
    resized_16_9 = resize_image(image, new_x_16_9, y_res)
    resized_16_9.save("resized_16_9.jpg")

    # 4:3 aspect ratio
    new_x_4_3 = math.ceil((4 / 3) * y_res)
    resized_4_3 = resize_image(image, new_x_4_3, y_res)
    resized_4_3.save("resized_4_3.jpg")

    return resized_16_9, resized_4_3


# Función para cargar la imagen y redimensionarla
def upload_and_process_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        resized_16_9, resized_4_3 = adjust_image_aspect_ratios(file_path)

        # Mostrar imágenes redimensionadas en la ventana
        img_16_9 = ImageTk.PhotoImage(resized_16_9)
        img_4_3 = ImageTk.PhotoImage(resized_4_3)

        label_16_9.config(image=img_16_9)
        label_16_9.image = img_16_9

        label_4_3.config(image=img_4_3)
        label_4_3.image = img_4_3

        # Información al usuario
        result_label.config(text="Imágenes guardadas como 'resized_16_9.jpg' y 'resized_4_3.jpg'")


# Crear ventana
root = tk.Tk()
root.title("Redimensionar Imagen a 16:9 y 4:3")

# Botón para cargar imagen
upload_button = tk.Button(root, text="Cargar Imagen", command=upload_and_process_image)
upload_button.pack(pady=10)

# Etiquetas para mostrar las imágenes redimensionadas
label_16_9 = tk.Label(root)
label_16_9.pack(pady=10)

label_4_3 = tk.Label(root)
label_4_3.pack(pady=10)

# Resultado
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
