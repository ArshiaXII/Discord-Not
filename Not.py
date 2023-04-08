import tkinter as tk
from tkinter import filedialog, Text, messagebox, ttk
import os

root = tk.Tk()
root.title("Python Not Defteri Uygulaması")
root.geometry("800x600")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#ccc")
style.map("TButton", background=[("active", "#c0c0c0")])

def not_olustur():
    text_widget.delete(1.0, "end")

def not_goruntule():
    not_adi = filedialog.askopenfilename(defaultextension=".txt", title="Notları Görüntüle")
    if not not_adi:
        return
    with open(not_adi, "r") as file:
        not_metni = file.read()
    text_widget.delete(1.0, "end")
    text_widget.insert(1.0, not_metni)

def not_duzenle():
    not_adi = filedialog.askopenfilename(defaultextension=".txt", title="Not Düzenle")
    if not not_adi:
        return
    with open(not_adi, "r") as file:
        not_metni = file.read()
    text_widget.delete(1.0, "end")
    text_widget.insert(1.0, not_metni)

def not_sil():
    not_adi = filedialog.askopenfilename(defaultextension=".txt", title="Not Sil")
    if not not_adi:
        return
    os.remove(not_adi)
    messagebox.showinfo(title="Not Silindi", message=f"{not_adi} başarıyla silindi.")

frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)

text_widget = Text(frame, wrap="word", padx=10, pady=10, font=("Arial", 12))
text_widget.pack(expand=True, fill="both")

buton_frame = tk.Frame(frame, bg="white")
buton_frame.pack(side="bottom", fill="x")

buton_olustur = ttk.Button(buton_frame, text="Not Oluştur", command=not_olustur)
buton_olustur.pack(side="left", padx=10)

buton_goruntule = ttk.Button(buton_frame, text="Notları Görüntüle", command=not_goruntule)
buton_goruntule.pack(side="left", padx=10)

buton_duzenle = ttk.Button(buton_frame, text="Not Düzenle", command=not_duzenle)
buton_duzenle.pack(side="left", padx=10)

buton_sil = ttk.Button(buton_frame, text="Not Sil", command=not_sil)
buton_sil.pack(side="left", padx=10)

root.mainloop()