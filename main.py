import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter import ttk

def analyze_file():
    """Opens a file dialog, reads the selected file, and analyzes its content."""
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, content)

            word_count = len(content.split())
            char_count = len(content)
            line_count = content.count('\n') + 1

            word_count_label.config(text=f"Words: {word_count}")
            char_count_label.config(text=f"Characters: {char_count}")
            line_count_label.config(text=f"Lines: {line_count}")

    except Exception as e:
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, f"Error reading file: {e}")
        word_count_label.config(text="Words: N/A")
        char_count_label.config(text="Characters: N/A")
        line_count_label.config(text="Lines: N/A")

# -------------------- GUI Setup --------------------

root = tk.Tk()
root.title("Simple Text File Analyzer")
root.geometry("800x600")
root.configure(bg="#f0f0f0") # A light gray background

# Using a frame for better organization
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

# Title label
title_label = ttk.Label(main_frame, text="Text File Analyzer", font=("Helvetica", 20, "bold"))
title_label.pack(pady=(10, 20))

# Button to open file dialog
open_button = ttk.Button(main_frame, text="Open and Analyze File", command=analyze_file)
open_button.pack(pady=10)

# Scrolled Text Widget to display file content
text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=70, height=20, font=("Helvetica", 12))
text_area.pack(pady=10, padx=10, fill="both", expand=True)

# Frame for statistics
stats_frame = ttk.Frame(main_frame)
stats_frame.pack(pady=10)

word_count_label = ttk.Label(stats_frame, text="Words: N/A", font=("Helvetica", 12, "bold"))
word_count_label.grid(row=0, column=0, padx=20)

char_count_label = ttk.Label(stats_frame, text="Characters: N/A", font=("Helvetica", 12, "bold"))
char_count_label.grid(row=0, column=1, padx=20)

line_count_label = ttk.Label(stats_frame, text="Lines: N/A", font=("Helvetica", 12, "bold"))
line_count_label.grid(row=0, column=2, padx=20)

# Run the application
root.mainloop()