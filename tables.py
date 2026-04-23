import sqlite3

def create_tables():
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    query=""" Create table if not exists accounts(
    acn integer primary key autoincrement,
    name text,
    pass text,
    bal float,
    mob text,
    adhar text unique,
    email text unique,
    opendate datetime)
    
    """
    curobj.execute(query)
    conobj.commit()
    conobj.close()
    
    print("Table created or exists")
    