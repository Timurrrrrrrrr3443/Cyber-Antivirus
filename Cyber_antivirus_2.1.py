import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

threats = ["Trojan.Salo.exe", "Worm.Borshch.dll", "Adware.Skvarka.vbs", "Exploit.Zhytnyak.sys"]
found_threat = None

def start_scan():
    global found_threat
    status_label.config(text="🔍 Сканування розпочато...")
    progress['value'] = 0
    log_output.delete("1.0", tk.END)
    root.update()

    for i in range(10):
        time.sleep(0.3)
        progress['value'] += 10
        root.update()
        if i == 5:
            found_threat = random.choice(threats)
            messagebox.showwarning("⚠️ Загроза знайдена!", f"Виявлено: {found_threat}")
            log_output.insert(tk.END, f"⚠️ Загроза: {found_threat}\n")

    status_label.config(text="✅ Сканування завершено.")
    log_output.insert(tk.END, "✅ Готово. Система у безпеці.\n")

def delete_threat():
    global found_threat
    if found_threat:
        messagebox.showinfo("🧹 Видалено", f"{found_threat} успішно ізольовано.")
        log_output.insert(tk.END, f"🧹 Видалено: {found_threat}\n")
        status_label.config(text="🛡️ Система очищена.")
        found_threat = None
    else:
        messagebox.showinfo("✅ Чисто", "Загроз не знайдено.")

def exit_program():
    root.destroy()

# GUI
root = tk.Tk()
root.title("Кібержеребець 3000 Lite™")
root.geometry("550x450")
root.configure(bg="#101010")

status_label = tk.Label(root, text="Стан: Очікування", font=("Courier New", 13), bg="#101010", fg="#00FF00")
status_label.pack(pady=10)

progress = ttk.Progressbar(root, length=500, mode="determinate")
progress.pack(pady=10)

scan_button = tk.Button(root, text="🔍 Сканувати", command=start_scan, font=("Courier New", 12), bg="#222", fg="#00FF00")
scan_button.pack(pady=5)

delete_button = tk.Button(root, text="🧹 Видалити загрозу", command=delete_threat, font=("Courier New", 12), bg="#222", fg="#00FF00")
delete_button.pack(pady=5)

exit_button = tk.Button(root, text="❌ Вийти", command=exit_program, font=("Courier New", 12), bg="#222", fg="#FF4444")
exit_button.pack(pady=10)

log_output = tk.Text(root, height=12, width=65, bg="#000000", fg="#00FF00", font=("Courier New", 11))
log_output.pack(pady=10)

root.mainloop()

