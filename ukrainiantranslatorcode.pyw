import tkinter as tk
from tkinter import ttk, messagebox

def get_file_extension(language):
    extensions = {
        'python': 'py',
        'javascript': 'js',
        'js': 'js',
        'c++': 'cpp',
        'cpp': 'cpp',
        'c': 'c',
        'java': 'java',
        'c#': 'cs',
        'csharp': 'cs',
        'ruby': 'rb',
        'php': 'php',
        'swift': 'swift',
        'kotlin': 'kt',
        'html': 'html',
        'css': 'css',
        'sql': 'sql',
        'go': 'go',
        'rust': 'rs'
    }
    return extensions.get(language.lower().strip(), 'txt')

def generate_code():
    language = lang_combo.get().strip()
    commands_text = text_input.get("1.0", tk.END).strip()
    
    if not language:
        messagebox.showerror("Помилка", "Будь ласка, оберіть або введіть мову програмування!")
        return
        
    if not commands_text:
        messagebox.showerror("Помилка", "Будь ласка, введіть хоча б одну команду!")
        return

    lines = commands_text.split('\n')
    ext = get_file_extension(language)
    filename = f"generated_code.{ext}"
    
    code_content = []
    code_content.append(f"// Згенеровано за допомогою ukrainiantranslatorcode")
    code_content.append(f"// Цільова мова: {language}\n")
    
    for item in lines:
        if not item.strip():
            continue
        if ext == 'py':
            code_content.append(f"# {item}")
        elif ext in ['js', 'cpp', 'c', 'java', 'cs', 'php', 'swift', 'kt', 'go', 'rs']:
            code_content.append(f"// {item}")
        elif ext == 'sql':
            code_content.append(f"-- {item}")
        else:
            code_content.append(f"{item}")

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(code_content))
        messagebox. موفقیت("Успіх", f"Файл успішно створено та збережено як:\n{filename}")
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося зберегти файл: {e}")

# Створення графічного вікна
root = tk.Tk()
root.title("Український перекладач коду")
root.geometry("500x450")
root.minsize(400, 350)

# Елементи інтерфейсу
tk.Label(root, text="Оберіть або введіть мову програмування:", font=("Arial", 10)).pack(pady=5)

languages_list = ['python', 'javascript', 'c++', 'java', 'c#', 'html', 'css', 'sql', 'go', 'rust']
lang_combo = ttk.Combobox(root, values=languages_list, font=("Arial", 10))
lang_combo.pack(pady=5, fill=tk.X, padx=20)
lang_combo.set('python')

tk.Label(root, text="Введіть ваші команди (кожна з нового рядка):", font=("Arial", 10)).pack(pady=5)

text_input = tk.Text(root, font=("Arial", 10), height=12)
text_input.pack(pady=5, fill=tk.BOTH, expand=True, padx=20)

btn_generate = tk.Button(root, text="Згенерувати файл", command=generate_code, font=("Arial", 11, "bold"), bg="#4CAF50", fg="white")
btn_generate.pack(pady=10)

# Запуск вікна (не закриється, поки користувач сам не натисне хрестик)
root.mainloop()