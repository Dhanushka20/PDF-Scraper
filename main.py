import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog
from PyPDF2 import PdfReader

# Function to open a file dialog and select a PDF file
def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        page_number = ask_page_number()
        if page_number:
            extract_text_from_pdf(file_path, page_number)

# Function to ask the user for the page number
def ask_page_number():
    page_number = simpledialog.askinteger("Page Number", "Enter the page number to extract:")
    return page_number

# Function to extract text from the selected PDF file
def extract_text_from_pdf(file_path, page_number):
    try:
        reader = PdfReader(file_path)
        # Check if page number is valid
        if 0 < page_number <= len(reader.pages):
            page = reader.pages[page_number - 1]  # Adjust for 0-based indexing
            text = page.extract_text()
            display_extracted_text(text)
        else:
            messagebox.showerror("Error", f"Invalid page number: {page_number}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text: {str(e)}")

# Function to display the extracted text in the text widget
def display_extracted_text(text):
    text_display.delete(1.0, tk.END)
    text_display.insert(tk.END, text)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("PDF Scraper")
root.geometry("1200x800")
root.configure(bg="#4a4a4a")  # Set background color

# Title label
title_label = tk.Label(root, text="PDF Scraper", font=("Helvetica", 24, "bold"), bg="#4a4a4a", fg="white")
title_label.pack(pady=20)

# Frame for buttons
button_frame = tk.Frame(root, bg="#4a4a4a")
button_frame.pack(pady=20)

# Button to select PDF file
select_button = tk.Button(button_frame, text="Select PDF File", command=select_pdf_file, font=("Helvetica", 14), bg="#007acc", fg="white", activebackground="#005f99", activeforeground="white")
select_button.grid(row=0, column=0, padx=10)

# Scrollable text widget to display extracted text
text_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30, font=("Helvetica", 12))
text_display.pack(pady=20, padx=20)

# Run the Tkinter main loop
root.mainloop()
