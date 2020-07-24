import sqlite3


conn = sqlite3.connect("users.db")
c = conn.cursor()


def getUserById(id):
    result = c.execute("SELECT * FROM users  WHERE id=?", (str(id),))
    return result.fetchone()
    
def getUserNameById(id):
    result = c.execute("SELECT name FROM users WHERE id=?", (str(id),))
    return result.fetchone()

def getUserTagById(id):
    result = c.execute("SELECT tag FROM users WHERE id=?", (str(id),))
    return result.fetchone()

def getUserXpById(id):
    result = c.execute("SELECT xp FROM users WHERE id=?", (str(id),))
    return result.fetchone()

def CreateUser(name, tag, xp=0):
    c.execute("INSERT INTO users(name, tag, xp) VALUES (?, ?, ?)", (name, tag, xp,))
    conn.commit()
    

def DeleteUser(id):
    c.execute("DELETE FROM users where id=?", (id))
    conn.commit()
#  (name, tag, xp, id)