# since this is the main program so all the py file of library management system has been imported
import Date_Time
import Book_Split
import Return_Book
import lend_Books

def Main():
# while loop is used 
    while(True):
# welcome meassage is displayed as soon as we open the LMS
        Welcome_Message= '''\n--------WELCOME TO THE LIBRARY MANAGEMENT SYSTEM--------
        Please choose an option below:
        1.To Display all the books
        2.To lend/ADD a books
        3.To Return a books
        4.To Quit the library
        '''
        print(Welcome_Message)
# Exception hendeling is done.
        try:
            e=int(input("Choose the Numbers: "))
            print()
            if(e==1):
                with open("file.txt","r")as d:
                    lines=d.read()
                    print(lines)
                    print()
            elif(e==2):
                Book_Split.Book_Split()
                lend_Books.BorrowBooks()
            elif(e==3):
                Book_Split.Book_Split()
                Return_Book.Return()
            elif(e==4):
                print("Thank you for choosing LIBRARY MANAGEMENT. Have a great day!")
                exit()
            else:
                print("Invalid Option")
        except ValueError:
            print("Kindly follow the instruction!")
Main()
            
               
                
        
        
    

    
