__author__ = 'Perkins'


from script import BB_ZipFix
from tkinter import *
from tkinter import filedialog
import logging

class Application(Frame):
    def __init__(self,parent,str_filename=''):
        Frame.__init__(self, parent)
        self.parent = parent
        self.str_filename = str_filename
        self.create_widgets()

    def create_widgets(self):

        self.parent.title("Extract BB grade files (I HATE BLACKBOARD)")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        label1 = Label(self,text="This application extracts everything from a blackboard grade zip file \nIt then deletes the extra .txt,.zip,.rar files",justify=LEFT)
        label1.grid(row=0,column=0,columnspan=5,sticky=W,padx=5,pady=5)

        #create a file find button
        find_file_button=Button(self,text="Choose zip",command = self.find_file,padx=5,pady=5)
        find_file_button.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        #create a file textbox
        self.entry_file_name = Entry(self)
        self.entry_file_name.insert(0,self.str_filename)
        self.entry_file_name.grid(row=1,column=1,columnspan = 2,sticky=W+E,padx=5,pady=5)

        #create extract button
        self.result_button = Button(self,text="Extract Files",command = self.extractall,state=DISABLED,padx=5,pady=5)
        self.result_button.grid(row=1,column=4,sticky=E)

        #where output goes
        self.output = Text(self)
        self.output.grid(row=3, column=0, columnspan=5, rowspan=1, padx=5,pady=5, sticky=E+W+S+N)


    def find_file(self):
        #TODO filepicker
        self.str_filename = filedialog.askopenfilename(filetypes = (("Zip files", "*.zip")
                                                                    ,("All files", "*.*")))
        #set textbox value
        self.entry_file_name.delete(0,END)
        self.entry_file_name.insert(0,self.str_filename)

        #enable Extract button if .zip
        if (".zip" in self.str_filename):
            self.result_button.configure(state=NORMAL)
        else:
            self.result_button.configure(state=DISABLED)
        return self.str_filename

    def extractall(self):
        bb = BB_ZipFix(self.str_filename)
        bb.setupProjects()

        self.output.delete("1.0",END)
        with open('UI.log') as f:
            self.output.insert(END,f.read())

def main():
    # Configure only in your main program clause
    logging.basicConfig(level=logging.DEBUG,
                        filename='UI.log', filemode='w',
                        format='%(name)s %(levelname)s %(message)s')
    root = Tk()
    app=Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()

