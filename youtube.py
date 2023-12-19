from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import sv_ttk
from pathlib import Path

# Create a window object
window = tk.Tk()
sv_ttk.use_dark_theme()

icon_path = "icon.png"
icon_image = tk.PhotoImage(file=icon_path)
window.iconphoto(True, icon_image)

window.update()

window.minsize(window.winfo_width(), window.winfo_height())
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"+{x_coordinate-100}+{y_coordinate-100}")
canvas = tk.Canvas(window, width=500, height=400)
canvas.pack()

is_on = True
def switch():
    global is_on
    
    if is_on:
        sv_ttk.use_light_theme()
        is_on = False
    else:
        sv_ttk.use_dark_theme()
        is_on = True

# Set the window title
window.title("YouTube Video Downloader")

# Set the window size
window.geometry("500x200")

# Prevent the window from being resized
window.resizable(False, False)

def download_video():
    # Get the YouTube video URL from the entry field
    video_url = entry.get()

    if video_url == "":
        tk.messagebox.showerror(title="Error", message="Please enter a YouTube video URL.")
        return
    elif "youtube.com" not in video_url:
        tk.messagebox.showerror(title="Error", message="Please enter a valid YouTube video URL.")
        return
    elif "watch?v=" not in video_url:
        tk.messagebox.showerror(title="Error", message="Please enter a valid YouTube video URL.")
        return

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution video stream
    stream = yt.streams.get_highest_resolution()

    # Get the user's Downloads folder path
    downloads_folder = str(Path.home() / "Downloads")

    # Set the download location to the user's Downloads folder
    save_path = downloads_folder

    # Download the video to the selected location
    try: 
        stream.download(output_path=save_path)
        # Display a message box to indicate that the download is complete
        tk.messagebox.showinfo(title="Download Complete", message="The download is complete. The video can be found in your Downloads folder.")
    except:
        # Display a message box to indicate that an error occurred
        tk.messagebox.showerror(title="Error", message="An error occurred while downloading the video.")

    # Clear the entry field
    entry.delete(0, tk.END)


# Create a label for the instructions
label = tk.Label(window, text="Enter the YouTube video URL below:")
label.configure(font=("Arial", 12))
canvas.create_window(250, 20, window=label)

# Create an entry field for the YouTube video URL
entry = tk.Entry(window, width=50)
entry.configure(font=("Arial", 12), relief="flat", borderwidth=2, highlightthickness=2, highlightcolor="#00aaff", highlightbackground="#00aaff")
canvas.create_window(250, 50, window=entry)

# Create a button to download the video
button = ttk.Button(window, text="Download", style='Accent.TButton', command=download_video)
canvas.create_window(250, 100, height= 35 ,width=90 , window=button)

switch = ttk.Checkbutton(window, text="Change Theme", style="Switch.TCheckbutton", command=switch)
canvas.create_window(90, 175, height= 35 ,width=160 , window=switch)

# Run the main window loop
window.mainloop()