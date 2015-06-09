import os
import sqlite3
import os

class Db(object):

    """Classe Db pour interraction avec BDD"""
    def __init__(self):
        self.db_path = './'
        self.db_name = 'crawler.sq3'
        self._createPath()
        self.conn = sqlite3.connect(self.db_path+self.db_name)
        self.cur = self.conn.cursor()
        self._createTable()

    def _createTable(self):
        """Creation de la table si non existante"""
        self.cur.execute("CREATE TABLE IF NOT EXISTS crawl(chemin TEXT, fichier TEXT, extension TEXT)")

    def _createPath(self):
        if os.path.isdir(self.db_path):
            pass
        else:
            os.makedirs(self.db_path, mode=0o777)

    def commit(self):
        self.conn.commit()

    def dataInsert(self, chemin, fichier, extension):
        """Insertion"""
        self.cur.execute("INSERT INTO crawl(chemin, fichier, extension) VALUES (:chemin, :fichier, :extension)", {"chemin": chemin, "fichier": fichier, "extension": extension})
        self.conn.commit()

    def readData(self):
        """Lecture de la table"""
        self.cur.execute("SELECT * FROM crawl")
        return(self.cur.fetchall())

    def find(self, data):
        """Trouve les éléments passer en arguments"""
        self.cur.execute("SELECT * FROM crawl WHERE fichier = ?", data)
        return(self.cur.fetchall())

    def count(self):
        """Compte le nbr de ligne dans la table"""
        self.cur.execute("SELECT COUNT(*) FROM crawl")
        return(self.cur.fetchone())

    def close(self):
        """Fermeture du curseur et de la connection"""
        self.cur.close()
        self.conn.close()

db = Db()
<
####
#for rep, sous, fich in os.walk("/"):
#    db.dataInsert(str(rep), str(fich), '*')
#    print("fichier : ", rep)
# db.commit()
####
data = input("Entrez votre recherche : ")
print(db.find(str(data)))
db.close()
