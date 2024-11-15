
class Page:
    def __init__(self,name,content):
        self.nom = name
        self.contenu = content

    def __repr__(self):
        return f"#{self.nom}"

    def __str__(self):
        chaine = f"p{self.nom}\n"
        for line in self.contenu:
            chaine = chaine + f" {line}\n"

        return chaine

class Book:
    def __init__(self,name,cover_font="S",content=None):
        self.cover = [name,cover_font]
        if content == None:
            self.__contenu = [Page(1,"")]
        else:
            self.__contenu = content


    def __repr__(self):
        return f"###{self.cover[0]}"

    def __str__(self):
        if self.cover[1] == "S":
            return f"|{self.cover[0]}|"
        
        if self.cover[1] == "P":
            return f"+{self.cover[0]}+"


    def get_contenu(self):
        return self.__contenu
    
    def set_contenu(self,l_pages):
        new_content = [Page(i,l_pages[i]) for i in range(len(l_pages))]
        self.__contenu = new_content

    def read_contenu(self):
        chaine = f"###{self.cover[0]}\n"
        for page in self.__contenu:
            chaine = chaine + str(page)
        
        return chaine

    
    @property
    def taille(self):
        return len(self.__contenu)


    def save(self,file_name):
        f = open(file_name+".txt","w")
        f.write(self.read_contenu())
        f.close()

    
    def __del__(self):
        for page in self.__contenu:
            del page


class Bibli:
    def __init__(self,name="Bibli0",content=None):
        self.nom = name
        if content == None:
            self.__contenu = {(0,1):Book("Book0")}
        else:
            self.__contenu = content

    
    def add_book(self,coords,book):
        self.__contenu[coords] = book

    def take_book(self,coords):
        return self.__contenu.pop(coords)

    def __str__(self):
        return str(self.__contenu)

    
    @property
    def taille(self):
        return len(self.__contenu.keys())


# ==============================================================

if __name__ == "__main__":
    book1 = Book("Code1","S")
    book1.set_contenu([["asf","455522"],["CJDF","8545"],["No_mker","5445415f"]])
    page1 = book1.get_contenu()[1]

    bibli0 = Bibli()
    bibli0.add_book((1,1),book1)

    bibli0 = None

    print(book1)
    print(page1)