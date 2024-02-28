from tkinter import *
from tkinter import messagebox
import speedtest
import threading

# Function to perform speed test
def perform_speed_test():
    try:
        sp = speedtest.Speedtest()
        sp.get_servers()
        down_speed = round(sp.download() / (10 ** 6), 2)  # Mbps
        up_speed = round(sp.upload() / (10 ** 6), 2)  # Mbps
        # Update labels with speed results
        lab_down.config(text=f"Download: {down_speed} Mbps")
        lab_up.config(text=f"Upload: {up_speed} Mbps")
        messagebox.showinfo("Speed Test", "Speed test completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Speed test failed: {str(e)}")

# Function to initiate speed test
def speedcheck():
    try:
        lab_down.config(text="Testing...")
        lab_up.config(text="Testing...")
        # Start speed test in a separate thread
        thread = threading.Thread(target=perform_speed_test)
        thread.start()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x300")
sp.config(bg="#333333")  # Dark gray background color

# Create and place widgets
lab_title = Label(sp, text="Internet Speed Test", font=("Arial", 24, "bold"), bg="#333333", fg="white")
lab_title.pack(pady=10)

lab_down = Label(sp, text="Download: ", font=("Arial", 18), bg="#333333", fg="white")
lab_down.pack(pady=5)

lab_up = Label(sp, text="Upload: ", font=("Arial", 18), bg="#333333", fg="white")
lab_up.pack(pady=5)

btn_check = Button(sp, text="Check Speed", font=("Arial", 16, "bold"), bg="#007bff", fg="white", relief=RAISED, command=speedcheck)
btn_check.pack(pady=20)

# Run the application
sp.mainloop()
