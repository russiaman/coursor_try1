import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

def get_size_format(size):
    # Convert size to human readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

class DirectoryScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Scanner")
        self.root.geometry("800x600")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Path input
        ttk.Label(main_frame, text="Enter directory path:").grid(row=0, column=0, sticky=tk.W)
        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(main_frame, textvariable=self.path_var, width=50)
        self.path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        # Scan button
        self.scan_button = ttk.Button(main_frame, text="Scan Directory", command=self.scan_directory)
        self.scan_button.grid(row=0, column=2, padx=5)
        
        # Results area
        ttk.Label(main_frame, text="Directory Contents:").grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=(10,0))
        self.results_text = scrolledtext.ScrolledText(main_frame, width=80, height=30)
        self.results_text.grid(row=2, column=0, columnspan=3, pady=5)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def scan_directory(self):
        path = self.path_var.get().strip()
        
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        
        # Validate path
        if not path:
            messagebox.showerror("Error", "Please enter a directory path")
            return
            
        if not os.path.exists(path):
            messagebox.showerror("Error", f"The path '{path}' does not exist.")
            return
            
        if not os.path.isdir(path):
            messagebox.showerror("Error", f"'{path}' is not a directory.")
            return
        
        # Scan directory
        try:
            self.results_text.insert(tk.END, f"Contents of {path}:\n")
            self.results_text.insert(tk.END, "-" * 80 + "\n")
            self.results_text.insert(tk.END, f"{'Type':<8} {'Name':<40} {'Size':<15}\n")
            self.results_text.insert(tk.END, "-" * 80 + "\n")
            
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    self.results_text.insert(tk.END, f"[DIR]   {item:<40} {'-':<15}\n")
                else:
                    size = os.path.getsize(full_path)
                    size_str = get_size_format(size)
                    self.results_text.insert(tk.END, f"[FILE]  {item:<40} {size_str:<15}\n")
                    
        except PermissionError:
            messagebox.showerror("Error", "Permission denied to access this directory.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DirectoryScannerGUI(root)
    root.mainloop() 