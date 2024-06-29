Explanation of Code
Imports and Function Definitions

Imports:
tkinter for the GUI.
os for executing system commands.
ctypes for interacting with Windows API functions to log out or sign out.
Functions:
shutdown(): Executes a shutdown command using os.system.
sign_out(): Uses ctypes to call the Windows API function ExitWindowsEx with parameters to sign out the user.
log_out(): Similar to sign_out(); here it's a duplicate function for logging out (could be removed or renamed to avoid redundancy).
restart(): Executes a restart command using os.system.
about(): Creates a new top-level window with information about the application.
Main Window Setup

Create Main Window:
root = tk.Tk() initializes the main window.
root.title("System Control") sets the window title.
Menu Bar

Menu Bar Creation:
menubar = tk.Menu(root) creates the main menu bar.
root.config(menu=menubar) attaches the menu bar to the main window.
File Menu:
filemenu = tk.Menu(menubar, tearoff=0) creates a file menu.
filemenu.add_command(label="Exit", command=root.quit) adds an "Exit" option to the file menu, which closes the application.
menubar.add_cascade(label="File", menu=filemenu) adds the file menu to the menu bar.
Help Menu:
helpmenu = tk.Menu(menubar, tearoff=0) creates a help menu.
helpmenu.add_command(label="About", command=about) adds an "About" option to the help menu, which opens the about window.
menubar.add_cascade(label="Help", menu=helpmenu) adds the help menu to the menu bar.
Buttons

Button Creation:
Each button is created with tk.Button, specifying the parent window (root), text, command to execute on click, font, foreground color (fg), and background color (bg).
shutdown_button.pack(pady=10, ipadx=20, ipady=10) and similar lines pack the buttons into the window with padding for spacing.
Buttons for System Control:
Shutdown Button: Red background, triggers shutdown().
Sign Out Button: Orange background, triggers sign_out().
Log Out Button: Blue background, triggers log_out().
Restart Button: Green background, triggers restart().
Window Background Color

root.configure(background='red') sets the main window's background color to red.
Main Loop

root.mainloop() starts the Tkinter main loop, which waits for user interaction and keeps the window open.
