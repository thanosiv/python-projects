import os
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
open_file = filedialog.askdirectory() # Returns opened path as str

new_filename = input("Enter the prefix to rename each file to:- ") # input for user to set the prefix of each file in the director
os.chdir(open_file) # change the working directory to the folder selected in the dialog
 
for count, f in enumerate(os.listdir()): # for each item in the directory
    f_name, f_ext = os.path.splitext(f) # split the file into filename and extension
    f_name = new_filename + str(count) # update the current file with the string entered into input, and the current count
 
    new_name = f'{f_name}{f_ext}' # recombine the filename and the extension
    os.rename(f, new_name) # finalize the filename change

print(str(count) + ' Files updated') # print out the number of files that were updated
