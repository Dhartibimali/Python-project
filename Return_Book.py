import Date_Time
import Book_Split

def Return():
    FullName=input("Enter the full name of the person who borrow the book:  " )
    e="Borrow-"+FullName+".txt"
    try:
        with open(e,"r")as d:
            lines=d.readlines()
            lines=[e.strip("$")for e in lines]
        with open(e,"r")as d:
            Data=d.read()
            print(Data)
    except:
        print("The name you have enter is incorrect")
        return()

    f="Return-"+FullName+".txt"
    with open(f,"w+")as d:
        d.write("Library Management System\n")
        d.write("       Book Returned By: "+FullName+"\n")
        d.write("Date: "+Date_Time.getdate()+"   Time:"+Date_Time.gettime()+"\n\n")
        d.write("NO.    BookName     Price \n")

    Total=0.0
    for i in range(3):
        if Book_Split.BookName[i] in Data:
            with open(f,"a")as d:
                d.write(str(i+1)+"\t\t"+Book_Split.BookName[i]+"\t\t$"+Book_Split.Price[i]+"\n")
                Book_Split.Quantity[i]=int(Book_Split.Quantity[i])+1
            Total+=float(Book_Split.Price[i])
            break
    print("$"+str(Total))
    print("Enter s for Sure and q for Quit, only if the date of book return has been expired")
    Do=input()
    if(Do.upper()=="S"):
        print("How many days you were late to returned the book which you hove lend form us?")
        Day=int(input())
        Fine=5*Day
        with open(f,"a") as d:
            d.write("Fine: $"+str(Fine)+"\n")
        Total=Total+Fine

        print("final total:"+"$"+str(Total))
        with open(f,"a")as d:
            for i in range(3):
                d.write(Book_Split.BookName[i]+","+Book_Split.WriterName[i]+","+str(Book_Split.Quantity[i])+","+"$"+Book_Split.Price[i]+"\n")
                

            
        
    
            
        

    
        
