class Book :
  id = 0
  def __init__(self,Title,Author,Level):
      Book.id+=1
      self.uniqueID=Book.id
      self.Title=Title
      self.Author=Author
      self.Level=Level.upper()
      self.Availabilitystatus=True

  def Is_Status(self):
      if self.Availabilitystatus == True:
          return "Available"
      if self.Availabilitystatus == False:
          return "Not Available"
  def show_book(self):
      print(f'{self.uniqueID}\t|\t{self.Title}\t|\t{self.Author}\t\t\t|\t{self.Level}\t|\t{self.Is_Status()}')
class Member:
    id=0
    def __init__(self,Name,Email,Level):
      Member.id+=1
      self.uniqueID=Member.id
      self.Name =Name
      self.Email=Email
      self.Level=Level.upper()
      self.Listofborrowedbooks = []

    def show_member (self):
        print(f'{self.uniqueID}\t|\t{self.Name}\t|\t{self.Email}\t\t\t|\t{self.Level}')

    def borrowing(self,book):
        self.Listofborrowedbooks.append(book)

    def returninig(self,book):
        self.Listofborrowedbooks.remove(book)

class Library :
    listofmembers=[]
    listofbooks=[]
    def add_members (self,Name,Email,Level):
         member=Member(Name,Email,Level)
         self.listofmembers.append(member)
    def  show_members (self):
        for i in self.listofmembers:
          i.show_member()
    def  show_books (self):
        for i in self.listofbooks:
          i.show_book()
    def edit_members(self, e):
        for i in self.listofmembers :
            if e==i.uniqueID:
                self.listofmembers.pop(i.uniqueID-1)
                Name= input('Enter name : ')
                Email= input('Enter Email : ')
                Level= input('Enter Level : ')
                member = Member(Name, Email, Level)
                member.uniqueID=e
                self.listofmembers.insert(e-1,member)
            else :
                print('Invalid Input')
    def delete_member(self,e):
        for i in self.listofmembers :
            if e==i.uniqueID:
                self.listofmembers.pop(i.uniqueID-1)
    def add_books (self,Title,Author,Level):
         book =Book(Title,Author,Level)
         self.listofbooks.append(book)


    def find_member(self,id_member):

        for i in self.listofmembers:
            if i.uniqueID== id_member:
             return i

    def find_book(self, id_book):
        for x in self.listofbooks:
            if x.uniqueID==id_book:
             return x
    def borow_book (self,member_id,book_id):
        i=0
        while i<(len(self.listofmembers)-1):
            if self.listofmembers[i].uniqueID==member_id:
                break
            i+=1
        u = 0
        while u < (len(self.listofbooks)-1):
            if self.listofbooks[u].uniqueID == book_id:
                break
            u += 1
        if self.listofbooks[u].Availabilitystatus and self.listofbooks[u].Level==self.listofmembers[i].Level:
            self.listofmembers[i].borrowing(self.listofbooks[u])
            self.listofbooks[u].Availabilitystatus=False
            print(f"{self.listofmembers[i].Name} has borrowed the book : {self.listofbooks[u].Title}")
        else:
            print("The book has already borrowed")

    def return_book(self, member_id, book_id):
        i=0
        while i<(len(self.listofmembers)-1):
            if self.listofmembers[i].uniqueID==member_id:
                break
            i+=1
        u = 0
        while u < (len(self.listofbooks)-1):
            if self.listofbooks[u].uniqueID == book_id:
                break
            u += 1
        if (self.listofbooks[u].Availabilitystatus)==False and self.listofbooks[u].Level==self.listofmembers[i].Level:
            self.listofmembers[i].returninig(self.listofbooks[u])
            self.listofbooks[u].Availabilitystatus=True
            print(f"{self.listofmembers[i].Name} has returend the book : {self.listofbooks[u].Title}")
        else:
            print("The book has already returend ")



library=Library()
while True:
    print('''1-Add Member
2-Edit Member
3-Show Members
4-Delete Member
5-Add Book
6-Show Books
7-Borrow Book
8-Return Book
9-Exit    ''')
    choice = int(input("Enter Number of Your Choice : "))
    if choice==1:
        e=input("Enter Member Name : ")
        i=input("enter Member Email : ")
        O=input("Enter Member Level(a,b,c) : ")
        library.add_members(e,i,O)
    elif choice==2:
        t=int(input("Enter Member Id to edit : "))
        library.edit_members(t)
    elif choice==3:
        print('ID\t|\tName\t|\tEmail\t\t\t|\tLevel')
        library.show_members()
    elif choice==4:
        u = int(input('Enter Member Id to dalete : '))
        library.delete_member(u)

    elif choice==5:
        r=input('Enetr title : ')
        w=input('Enetr author : ')
        p=input('Enetr level (a,b,c) : ')
        library.add_books(r,w,p)
    elif choice==6:
        print(f'uniqueID\t|\tTitle\t|\tAuthor\t\t\t|\tLevel\t|\tAvailability')
        library.show_books()
    elif choice==7:
        i=int(input('Enter Member ID : '))
        s=int(input('Enter book ID : '))
        library.borow_book(i,s)

    elif choice==8:
        i = int(input('Enter Member ID : '))
        s = int(input('Enter book ID : '))
        library.return_book(i, s)
    elif choice==9:
        break
    else:
        print(" Invalid Input")