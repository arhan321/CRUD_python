import mysql.connector


def connect_db():
    conn = mysql.connector.connect(
        host="localhost", 
        port=31234,
        user="root",      
        password="Djony", 
        database="python_CRUD"
    )
    return conn

def create_user(name, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    conn.close()

def get_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def get_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user(user_id, name, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (name, email, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    conn.close()

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah User")
        print("2. Tampilkan Semua User")
        print("3. Tampilkan User Berdasarkan ID")
        print("4. Update User")
        print("5. Hapus User")
        print("6. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            name = input("Masukkan nama: ")
            email = input("Masukkan email: ")
            create_user(name, email)
            print("User berhasil ditambahkan.")
        
        elif choice == '2':
            print("All users:")
            users = get_users()
            for user in users:
                print(user)
        
        elif choice == '3':
            user_id = int(input("Masukkan ID user: "))
            user = get_user(user_id)
            if user:
                print(user)
            else:
                print("User tidak ditemukan.")
        
        elif choice == '4':
            user_id = int(input("Masukkan ID user yang akan diupdate: "))
            name = input("Masukkan nama baru: ")
            email = input("Masukkan email baru: ")
            update_user(user_id, name, email)
            print("User berhasil diupdate.")
        
        elif choice == '5':
            user_id = int(input("Masukkan ID user yang akan dihapus: "))
            delete_user(user_id)
            print("User berhasil dihapus.")
        
        elif choice == '6':
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
