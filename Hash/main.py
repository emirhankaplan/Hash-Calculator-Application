import tkinter as tk
import hashlib

def hash_text(event=None):
    text = entry.get()
    selected_algorithm = algorithm_var.get()

    if text and selected_algorithm:
        hash_function = getattr(hashlib, selected_algorithm)
        hash_result = hash_function(text.encode()).hexdigest()
        result_text.set(f"{selected_algorithm.upper()}: {hash_result}")
    else:
        result_text.set("Lütfen metin ve algoritma seçin.")

# Arayüzü oluştur
root = tk.Tk()
root.title("Hash Hesaplayıcı")

# Metin girişi
entry_label = tk.Label(root, text="Metni Girin:", font=("Helvetica", 12))
entry_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=10, pady=5)
entry.bind("<Return>", hash_text)  # Enter tuşuna basıldığında hash_text fonksiyonunu çağır

# Algoritma seçimi
algorithm_label = tk.Label(root, text="Hash Algoritması Seçin:", font=("Helvetica", 12))
algorithm_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

algorithms = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
algorithm_var = tk.StringVar(value=algorithms[0])  # Varsayılan olarak ilk algoritmayı seçiyoruz

algorithm_frame = tk.Frame(root)
algorithm_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")

for i, algorithm in enumerate(algorithms):
    algorithm_radio = tk.Radiobutton(algorithm_frame, text=algorithm.upper(), variable=algorithm_var, value=algorithm,
                                     font=("Helvetica", 12))
    algorithm_radio.pack(side="left", padx=5, pady=5)

# Hashleme düğmesi
hash_button = tk.Button(root, text="Hashle", command=hash_text, font=("Helvetica", 12))
hash_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Sonuç çerçevesi
result_frame = tk.LabelFrame(root, text="Sonuç", font=("Helvetica", 12), bd=2, relief="groove")
result_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

result_text = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=result_text, font=("Helvetica", 12), wraplength=400)
result_label.pack(padx=10, pady=5)

root.mainloop()
