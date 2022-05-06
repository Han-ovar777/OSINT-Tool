import tkinter
from tkinter import filedialog
from tkinter.filedialog import  askopenfile
import os


 #use to hide tkinter window



def search_for_file_path ():
    root = tkinter.Tk()
    root.withdraw()
    currdir = os.getcwd()
    #tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    tempfile = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please select a file')
    if tempfile:
        print ("You chose: %s" % tempfile.name)
    return tempfile


def getimage():
    myfile= search_for_file_path()
    return myfile

