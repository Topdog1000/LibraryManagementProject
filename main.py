from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class menu:
    def __init__(self):
        self.root = Tk()
        self.root.title('Library Management System by Emmanuel Udeze & Pranob Kanti')
        self.root.geometry("800x500")
        self.root.configure(bg="#FFBA7A")
        conn = sqlite3.connect('test.db')
        conn.execute(
            'CREATE TABLE if not exists book_info (title text not null, author text not null, year integer, isbn text)')
        conn.commit()
        conn.execute(
            'CREATE TABLE if not exists book_issued (isbn text, student_id text, ISSUE_DATE DATE NOT NULL, RETURN_DATE DATE NOT NULL, PRIMARY KEY (isbn,student_id))')
        conn.commit()
        conn.close()
        self.a_1 = Canvas(self.root, bg="#FFFFE4").place(x=200, y=25, width=400, height=450)
        label_0 = Label(self.a_1, bg="#FFFFE4", text='Library Management System', fg="#815B3A",
                        font=("Georgia 13 bold", 25, "bold")).place(x=230, y=65)
        l1 = Button(self.a_1, text='Books Database', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.book).place(x=300, y=250, width=200, height=40)
        l2 = Button(self.a_1, text='Issue & Return Books', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.student).place(x=300, y=300, width=200, height=40)
        self.root.mainloop()

    def book(self):
        self.a_2 = Canvas(self.root, bg="#FFBA7A").place(x=0, y=0, width=800, height=500)
        l1 = Button(self.a_2, text='Add Books', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.addbook).place(x=30, y=50, width=200, height=40)
        l2 = Button(self.a_2, text='Search Books', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.search).place(x=30, y=170, width=200, height=40)

        l4 = Button(self.a_2, text='All Books', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.all).place(x=30, y=290, width=200, height=40)
        l4 = Button(self.a_2, text='<< Main Menu', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.mainmenu).place(x=30, y=410, width=200, height=40)

    def addbook(self):
        self.ayear = IntVar()
        self.aauthor = StringVar()
        self.atitle = StringVar()
        self.aISBN = StringVar()
        self.f1 = Frame(self.a_2, height=400, width=500, bg='#FFFFE4')
        self.f1.place(x=250, y=50)
        l1 = Label(self.f1, text='Title : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=50, width=100)
        e1 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.atitle).place(x=150, y=50, height=30)
        l2 = Label(self.f1, text='Author : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=100, width=100)
        e2 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.aauthor).place(x=150, y=100,
                                                                                                 height=30)
        l3 = Label(self.f1, text='Year : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=150, width=100)
        e3 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.ayear).place(x=150, y=150, height=30)
        l4 = Label(self.f1, text='ISBN # : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=200, width=100)
        e4 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.aISBN).place(x=150, y=200, height=30)
        self.f1.grid_propagate(0)
        b1 = Button(self.f1, text='Add', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.adddata).place(x=66, y=300, width=150, height=40)
        b2 = Button(self.f1, text='Back', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.rm).place(x=284, y=300, width=150, height=40)

    def rm(self):
        self.f1.destroy()

    def mainmenu(self):
        self.root.destroy()
        a = menu()

    def adddata(self):
        a = self.atitle.get()
        b = self.aauthor.get()
        try:
            c = self.ayear.get()
        except:
            messagebox.showinfo("Error", "Please Enter correct value in of Year.")
        d = self.aISBN.get()
        conn = sqlite3.connect('test.db')
        try:
            if (a and b and c and d) == "":
                messagebox.showinfo("Error", "Fields cannot be empty.")
            else:
                print(a, b, c, d)
                conn.execute("insert into book_info \
                values (?,?,?,?)", (a, b, c, d));
                conn.commit()
                messagebox.showinfo("Success", "Book added successfully")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error", "Book is already present.")
        conn.close()

    def search(self):
        self.sid = StringVar()
        self.f1 = Frame(self.a_2, height=400, width=500, bg='#FFFFE4')
        self.f1.place(x=250, y=50)
        l1 = Label(self.f1, text='Title/Author/ISBN #: ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=20, y=50)
        e1 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.sid).place(x=200, y=50, height=30)
        b1 = Button(self.f1, text='Search', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.serch1).place(x=66, y=300, width=150, height=40)
        b1 = Button(self.f1, text='Back', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.rm).place(x=284, y=300, width=150, height=40)

    def create_tree(self, plc, lists, height):
        self.tree = ttk.Treeview(plc, height=height, column=(lists), show='headings')
        n = 0
        while n is not len(lists):
            self.tree.heading("#" + str(n + 1), text=lists[n])
            self.tree.column("" + lists[n], width=110)
            n = n + 1
        return self.tree

    def serch1(self):
        k = self.sid.get()
        if k != "":
            self.list4 = ("title", "author", "year", "ISBN")
            self.trees = self.create_tree(self.f1, self.list4, 9)
            self.trees.place(x=25, y=135)
            conn = sqlite3.connect('test.db')

            c = conn.execute("select * from book_info where title=? OR author=? OR ISBN=?", (k, k, k))
            a = c.fetchall()
            if len(a) != 0:
                for row in a:
                    self.trees.insert("", END, values=row)
                conn.commit()
                conn.close()
                self.trees.bind('<<TreeviewSelect>>')
                b1 = Button(self.f1, text='Delete', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                            command=self.deleteitem).place(x=70, y=350, width=150, height=40)
                b2 = Button(self.f1, text='Update', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                            command=self.updateitem).place(x=275, y=350, width=150, height=40)
            else:
                messagebox.showinfo("Error", "Data not found")

        else:
            messagebox.showinfo("Error", "Search field cannot be empty.")

    def updateitem(self):
        self.uyear = IntVar()
        self.uauthor = StringVar()
        self.utitle = StringVar()
        self.uISBN = StringVar()
        self.f1 = Frame(self.a_2, height=400, width=500, bg='#FFFFE4')
        self.f1.place(x=250, y=50)
        l1 = Label(self.f1, text='Title : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=50, width=100)
        e1 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.utitle).place(x=150, y=50, height=30)
        l2 = Label(self.f1, text='Author : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=100, width=100)
        e2 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.uauthor).place(x=150, y=100,
                                                                                                 height=30)
        l3 = Label(self.f1, text='Year : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=150, width=100)
        e3 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.uyear).place(x=150, y=150, height=30)
        l4 = Label(self.f1, text='ISBN # : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=200, width=100)
        e4 = Entry(self.f1, width=45, bg='#FFBA7A', fg='black', textvariable=self.uISBN).place(x=150, y=200, height=30)
        self.f1.grid_propagate(0)
        b1 = Button(self.f1, text='Update', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.update).place(x=175, y=300, width=150, height=40)

    def update(self):
        self.curItem = self.trees.focus()
        self.c1 = self.trees.item(self.curItem, "values")[3]
        a = self.utitle.get()
        b = self.uauthor.get()
        try:
            c = self.uyear.get()
        except:
            messagebox.showinfo("Error", "Please Enter correct value in of Year.")
        d = self.uISBN.get()
        conn = sqlite3.connect('test.db')
        try:
            if (a and b and c and d) == "":
                messagebox.showinfo("Error", "Fields cannot be empty.")
            else:
                self.c1 = self.trees.item(self.curItem, "values")[3]
                print(self.c1)
                conn.execute("UPDATE book_info SET title=?,author=?,year=?,isbn=? WHERE isbn=?", (a, b, c, d, self.c1))
                conn.commit()
                messagebox.showinfo("Success", "Book Updated successfully")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error", "Book is already present.")
        conn.close()

    def deleteitem(self):
        try:
            self.curItem = self.trees.focus()
            self.c1 = self.trees.item(self.curItem, "values")[3]
            print(self.c1)
            conn = sqlite3.connect('test.db')
            cd = conn.execute("select * from book_info where isbn=?", (self.c1,))
            ab = cd.fetchall()
            if ab != 0:
                print(self.c1)
                conn.execute("DELETE FROM book_info where isbn=?", (self.c1,));
                conn.commit()
                messagebox.showinfo("Successful", "Book Deleted sucessfully.")
                self.trees.delete(self.curItem)
            else:
                messagebox.showinfo("Error", "Book is Issued.\nBook cannot be deleted.")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Empty", "Please select something.")

    def all(self):
        self.f1 = Frame(self.a_2, height=400, width=500, bg='#FFFFE4')
        self.f1.place(x=250, y=50)
        b1 = Button(self.f1, text='Back', bg='orange', fg='black', width=10, bd=3, command=self.rm).place(x=250, y=400)
        conn = sqlite3.connect('test.db')
        self.list3 = ("title", "author", "year", "ISBN")
        self.treess = self.create_tree(self.f1, self.list3, 15)
        self.treess.place(x=25, y=50)
        c = conn.execute("select * from book_info")
        g = c.fetchall()
        if len(g) != 0:
            for row in g:
                self.treess.insert('', END, values=row)
        conn.commit()
        conn.close()

    def student(self):
        self.a_3 = Canvas(self.root, bg="#FFBA7A").place(x=0, y=0, width=800, height=500)
        l1 = Button(self.a_3, text='Issue book', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.issue).place(x=30, y=50, width=200, height=40)
        l2 = Button(self.a_3, text='Return Book', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.returnn).place(x=30, y=170, width=200, height=40)
        l3 = Button(self.a_3, text='Student Activity', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.activity).place(x=30, y=290, width=200, height=40)
        l4 = Button(self.a_3, text='<< Main Menu', relief="groove", bg="#FFFFE4", font=("Georgia 13 bold", 14),
                    command=self.mainmenu).place(x=30, y=410, width=200, height=40)

    def issue(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()
        self.f1 = Frame(self.a_3, height=400, width=500, bg='#FFFFE4')
        self.f1.place(x=250, y=50)
        l1 = Label(self.f1, text='ISBN # : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=50, width=100)
        e1 = Entry(self.f1, width=45, bg='#FFBA7A', textvariable=self.aidd).place(x=150, y=50, height=30)
        l2 = Label(self.f1, text='Student Id : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=100,
                                                                                                    width=100)
        e2 = Entry(self.f1, width=45, bg='#FFBA7A', textvariable=self.astudentt).place(x=150, y=100, height=30)
        b1 = Button(self.f1, text='Back', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.rm).place(x=66, y=300, width=150, height=40)
        b1 = Button(self.f1, text='Issue', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.issuedbook).place(x=284, y=300, width=150, height=40)

    def issuedbook(self):
        bookid = self.aidd.get()
        studentid = self.astudentt.get()
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("select isbn from book_info where isbn=?", (bookid,))
        an = cursor.fetchall()
        print(an)
        if (bookid and studentid != ""):
            if an != []:
                for i in an:
                    if int(i[0].replace("-", "")) > 0:
                        try:
                            conn.execute("INSERT INTO book_issued VALUES (?,?,date('now'),date('now','+7 day'))",
                                         (bookid, studentid,));
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Updated", "Book Issued sucessfully.")
                        except:
                            messagebox.showinfo("Error", "Book is already issued by student.")

                    else:
                        messagebox.showinfo("Unavailable", "Book unavailable.\nThere are 0 copies of the book.")
            else:
                messagebox.showinfo("Error", "No such Book in Database.")
        else:
            messagebox.showinfo("Error", "Fields cannot be blank.")

    def returnn(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()

        self.f1 = Frame(self.a_3, height=400, width=500, bg='#FFFFE4')
        self.f1.place(x=250, y=50)
        l1 = Label(self.f1, text='ISBN # : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=50, width=100)
        e1 = Entry(self.f1, width=45, bg='#FFBA7A', textvariable=self.aidd).place(x=150, y=50, height=30)
        l2 = Label(self.f1, text='Student Id : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=100,
                                                                                                    width=100)
        e2 = Entry(self.f1, width=45, bg='#FFBA7A', textvariable=self.astudentt).place(x=150, y=100, height=30)
        b1 = Button(self.f1, text='Back', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.rm).place(x=66, y=300, width=150, height=40)
        b1 = Button(self.f1, text='Return', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.returnbook).place(x=284, y=300, width=150, height=40)
        self.f1.grid_propagate(0)

    def returnbook(self):
        a = self.aidd.get()
        b = self.astudentt.get()

        conn = sqlite3.connect('test.db')

        fg = conn.execute("select isbn from book_info where isbn=?", (a,))
        fh = fg.fetchall()
        conn.commit()
        if fh != None:
            c = conn.execute("select * from book_issued where isbn=? and student_id=?", (a, b,))
            d = c.fetchall()
            conn.commit()
            if len(d) != 0:
                c.execute("DELETE FROM book_issued where isbn=? and student_id=?", (a, b,));
                conn.commit()
                messagebox.showinfo("Success", "Book Returned sucessfully.")
            else:
                messagebox.showinfo("Error", "Data not found.")
        else:
            messagebox.showinfo("Error", "No such book.\nPlease add the book in database.")
        conn.commit()
        conn.close()

    def activity(self):
        self.aidd = StringVar()
        self.astudentt = StringVar()
        self.f1 = Frame(self.a_3, height=400, width=500, bg='#FFFFE4')
        self.f1.place(x=250, y=50)
        self.list2 = ("ISBN", "Student_ID", "ISSUE DATE", "RETURN DATE")
        self.trees = self.create_tree(self.f1, self.list2, 9)
        self.trees.place(x=50, y=100)

        l1 = Label(self.f1, text='ISBN #/Student ID : ', font=("Georgia 13 bold", 14), bg="#FFFFE4").place(x=50, y=50)
        e1 = Entry(self.f1, width=40, bg='#FFBA7A', textvariable=self.aidd).place(x=220, y=50, height=30)
        b1 = Button(self.f1, text='Back', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.rm).place(x=30, y=350, width=120, height=40)
        b1 = Button(self.f1, text='Search', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.searchact).place(x=180, y=350, width=120, height=40)
        b1 = Button(self.f1, text='All', relief="groove", bg="#FFBA7A", font=("Georgia 13 bold", 14),
                    command=self.searchall).place(x=330, y=350, width=120, height=40)
        self.f1.grid_propagate(0)

    def searchact(self):
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = self.create_tree(self.f1, self.list2, 9)
        self.trees.place(x=50, y=100)
        conn = sqlite3.connect('test.db')
        bid = self.aidd.get()
        try:
            c = conn.execute("select * from book_issued where isbn=? or student_id=?", (bid, bid,))
            d = c.fetchall()
            if len(d) != 0:
                for row in d:
                    self.trees.insert("", END, values=row)
            else:
                messagebox.showinfo("Error", "Data not found.")
            conn.commit()

        except Exception as e:
            messagebox.showinfo(e)
        conn.close()

    def searchall(self):
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = self.create_tree(self.f1, self.list2, 9)
        self.trees.place(x=50, y=100)
        conn = sqlite3.connect('test.db')
        try:
            c = conn.execute("select * from book_issued")
            d = c.fetchall()
            for row in d:
                self.trees.insert("", END, values=row)
            conn.commit()
        except Exception as e:
            messagebox.showinfo(e)
        conn.close()


a = menu()
