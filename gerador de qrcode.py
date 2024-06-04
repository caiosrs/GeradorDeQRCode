import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr_code(data, file_path, size=10, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    messagebox.showinfo("Sucesso", f"QR Code salvo em: {file_path}")

def browse_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    return file_path

def generate_and_save_qr():
    data = data_entry.get()
    if not data:
        messagebox.showwarning("Entrada inválida", "Por favor, insira o texto ou URL para o QR Code.")
        return

    file_path = browse_file()
    if file_path:
        generate_qr_code(data, file_path)
        data_entry.delete(0, tk.END)  # Limpa o campo de entrada

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de QR Code")

tk.Label(root, text="Texto ou URL para o QR Code:").grid(row=0, column=0, padx=10, pady=10)
data_entry = tk.Entry(root, width=50)
data_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Gerar QR Code", command=generate_and_save_qr).grid(row=1, columnspan=2, pady=10)

root.mainloop()
