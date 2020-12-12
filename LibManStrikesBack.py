import mysql.connector as con

def display_from_fetchall(TupleOfLists):
    if len(TupleOfLists) == 0:
        print("\nNo records found.")
    else:
        print("id", "name", "\tauthor_name", "publication", "price", "quantity", "genre", sep='\t')
        for Row in TupleOfLists:
            for value in Row:
                print(value, end='\t')
            print()

def function_end():
    choice =  input("\nEnter y to continue, n to exit: ")
    if choice.lower() == 'y':
        main_menu()
    elif choice.lower() == 'n':
        print("Goodbye.")
        pass
    else:
        print("Invalid input. Try again.")
        function_end()

def main_menu():
    db.commit()
    print()
    print('-'*95)
    print('\t\t\t\tMAIN MENU')
    print('-'*95)
    print("\n1. Display All Records\n2. Search Existing Records \n3. Add New Book \n4. Modify Existing Records \n5. Issue Book \n6. Receive Issued Book \n7. Delete Records\n8. Exit\n")
    inp = int(input('Enter choice: '))
    if inp == 1:
        display()
    elif inp == 2:
        search()
    elif inp == 3:
        adddata()
    elif inp == 4:
        modify()
    elif inp == 5:
        issue()
    elif inp == 6:
        receive()
    elif inp == 7:
        delete()
    elif inp == 8:
        print('Goodbye')
        pass

def display():
    print()
    cur.execute("SELECT * FROM books")
    TupleOfLists = cur.fetchall()
    print("id", "name", "\tauthor_name", "publication", "price", "quantity", "genre", sep='\t')
    for Row in TupleOfLists:
        for value in Row:
            print(value, end='\t')
        print()
    function_end()

def search():
    print()
    s = int(input('''
        Search by:
        1. Book Name
        2. Author Name
        3. ID
    > '''))
    if s == 1:
        cur.execute("SELECT * FROM books WHERE name = '{}'".format(input("Enter the book's name: ")))
        L = cur.fetchall()
        display_from_fetchall(L)
    elif s == 2:
        cur.execute("SELECT * FROM books WHERE author_name = '{}'".format(input("Enter author name: ")))
        L = cur.fetchall()
        display_from_fetchall(L)
    elif s == 3:
        cur.execute("SELECT * FROM books WHERE id = '{}'".format(input("Enter id: ")))
        L = cur.fetchall()
        display_from_fetchall(L)
    else:
        print("Invalid input.")
    print()
    function_end()

def adddata():
    print()
    id_no = int(input("Enter the book id: "))
    name = input("Enter the book name: ")
    author_name = input("Enter the author's name: ")
    publication = input("Enter the publication's name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    genre = input("Enter the type of the book: ")

    cur.execute("INSERT INTO books VALUES ({}, '{}', '{}', '{}', {}, {}, '{}')".format(id_no, name, author_name, publication, price, quantity, genre))
    print("Record successfully added.\n")
    function_end()

def modify():
    print()
    b_name = input("Enter the name of the book to modify: ")
    print("id", "name", "author_name", "publication", "price", "quantity", "genre", sep='\t')
    field = input("Enter the name of the field (listed above) to modify: ")
    val = input("Enter the new value: ")
    if field in ["id","price","quantity"]:
        cur.execute("UPDATE books SET {} = {} WHERE name = '{}'".format(field, int(val), b_name))
    else:
        cur.execute("UPDATE books SET {} = '{}' WHERE name = '{}'".format(field, val, b_name))
    print('Modified successfully')
    print()
    function_end()

def issue():
    print()
    b_name = input("Enter name of the book to be issued: ")
    cur.execute("SELECT quantity FROM books WHERE name = '{}'".format(b_name))
    L = cur.fetchone()
    if L[0] == 0:
        print("Not available.")
    else:
        cur.execute("UPDATE books SET quantity = {} WHERE name = '{}'".format(L[0]-1, b_name))
        print("Book issued successfully.")
    print()
    function_end()

def receive():
    print()
    b_name = input("Enter name of the book to be returned: ")
    cur.execute("SELECT quantity FROM books WHERE name = '{}'".format(b_name))
    L = cur.fetchone()
    cur.execute("UPDATE books SET quantity = {} WHERE name = '{}'".format(L[0]+1, b_name))
    print("Book Received Successfully")
    print()
    function_end()

def delete():
    print()
    b_name = input("Enter name of the book to delete: ")
    cur.execute("DELETE FROM books WHERE name = '{}'".format(b_name))
    print("Record deleted successfully.")
    print()
    function_end()

#----------------------------------------------------------------------------------------


passwordFound = False

while True:
    p = input("Enter password: ")
    try:
        db = con.connect(user='root',passwd=p,host='localhost',database='library')
        db.close()
        passwordFound = True
        break
    except:
        print('Wrong password. Try again.')


if passwordFound:
    db = con.connect(user='root',passwd=p,host='localhost',database='library')
    cur = db.cursor()
    print('-'*95)
    print('\t\t\tLIBRARY MANAGEMENT SYSTEM')
    print('-'*95)
    main_menu()
    db.commit()
