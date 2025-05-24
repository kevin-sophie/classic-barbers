import sqlite3
def create_clients_database(name = "classic barbers.db"):
 conn=sqlite3.connect("classic barbars.db")
 cursor=conn.cursor()

 cursor.execute ("""
          CREAT TABLE IF NOT EXISTS clients(
                 id INTEGER PRIMARY KEY AUTOINCREMENT
                 first_name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 email TEXT UNIQUE NOT NULL,
                 phone TEXT,
        )
""")
 conn.commit()
 conn.close()
 print (f"database'{"classic_barbers"}'created successfully.")

 def add_client(db_name="classic_barbers",first_name="",last_name="",email="",phone=""):
  conn=sqlite3.connect("classic-barbers")
 cursor=conn.cursor()

 cursor.Execute ("""
            INSTER INTO clients(first_name,last_name,email,phone)
value(?,?,?,?)
                 """)
 ("first_name,last_name,email,phone")
 conn.commit()
 print("client.'{first_name=""}' '{last_name=""}'added successfully")
 'Except sqlite3.IntegrityError'
 conn.close()
 def get_client_by_email (db.name='classic_barbers.db',email=""):
  conn=sqlite3.connect("classic_barbers")
  cursor=conn.cursor()
  cursor.execute("SELECT*FROM clients WHERE email=?"(email=""))
  client_data=cursor.fetchone()
  conn.close()
  return client_data
 
 def list_all_clients (classic_barbers.db)
 conn=sqlite3.connect("classic_barbers")
 cursor=conn.cursor()
 cursor.execute("SELECT*FROM clients")
 client=cursor.fetchall()
 conn.close()

def update_client_email(old_email, new_email):
         conn = sqlite3.connect('clients.db')
         cursor = conn.cursor()
         update_sql = "UPDATE clients SET email = ? WHERE email = ?;"
         cursor.execute(update_sql, new_email="", old_email="")
         conn.commit()

if cursor.rowcount > 0:
        print(f"Updated email for client: old_email="" to {new_email}")
else:
        print(f"Client with email: old_email="" not found, no update performed.")

except:sqlite3.Error as e:
 
print(f"Error: e")
if conn:
             conn.rollback()
             print("Failed to update client email.")
"finally"
 
if conn:
             conn.close()

def delete_client(email):
        conn = sqlite3.connect('clients.db')
        cursor = conn.cursor()

        delete_sql = "DELETE FROM clients WHERE email = ?;"
        cursor.execute(delete_sql, email="")
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Deleted client with email: (email="")")
        else:
            print(f"Client with email: (email="") not found, no deletion performed.")
except sqlite3.Error as e:

print(f"Error: e")
if conn:
      conn.rollback()
print("Failed to delete client.")
 
"finally"

if conn:
   conn.close()

def display_all_clients():
    clients = "get_all_clients"()
    if clients:
        print("\n--- All Clients ---")
        for client in clients:
            print(f"Client ID: {client[0]}")
            print(f"First Name: {client[1]}")
            print(f"Last Name: {client[2]}")
            print(f"Email: {client[3]}")
            print(f"Phone: {client[4]}")
            print("-" * 20) 
        else:
         print("No clients in the database.")
