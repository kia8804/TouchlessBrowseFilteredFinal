import tkinter as tk

def update_text(new_text):
    # Function to update the text of the label
    label.config(text=new_text)

# Create the main window
root = tk.Tk()
root.title("Touchless Browse")

# Set default size
root.geometry("400x100")  # Width x Height

# Set a background color similar to the Figma design
root.configure(bg='#2a2a2a')

# Create a label with some default text and style it similar to the Figma design
label = tk.Label(root, text="Default Text", font=('Helvetica', 16), fg='white', bg='#2a2a2a')
label.pack(expand=True)

update_text("Idle")




# Start the main loop
root.mainloop()

# Usage:
# To update the text, you would call the update_text function
# with the new text as an argument:
# update_text("New text to display")
