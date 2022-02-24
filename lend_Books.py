# Importing Book_Split and Book_Split
import Book_Split
#Date_Time and Book_Split hass been imported
import Date_Time
import Book_Split
#def is used to define the BorrowBooks
def BorrowBooks():
    This=False

    FullName =input("Enter your Full Name: ")


    m="Borrow-"+ FullName+".txt"
# with open is used to read the files
    with open(m,"w+")as d:
        d.write("Library Management System \n")
        d.write("Borrowed by:"+FullName+"\n")
        d.write("Date:"+Date_Time.getdate()+" Time:"+Date_Time.gettime()+"\n\n")
        d.write("No.  BookName  WriterName   \n")
# while loop is used 
    while This==False:
        print("Choose The Option Given Below:")
        for i in range(len(Book_Split.BookName)):
            print("Input", i, "Borrowing Book", Book_Split.BookName[i])
        
        e=int(input())
# integer data type is used.      
        if(int(Book_Split.Quantity[e])>0):
            print(f"You have been issued {Book_Split.BookName[e]} . Please keep it safe and return it within 10 days")
            with open(m,"a")as d:
                d.write("1."+Book_Split.BookName[e]+"\t"+Book_Split.WriterName[e]+"\n")
            Book_Split.Quantity[e]=int(Book_Split.Quantity[e])-1
            with open("file.txt","w+")as d:
                for i in range(3):
                    d.write(Book_Split.BookName[i]+","+Book_Split.WriterName[i]+","+str(Book_Split.Quantity[i])+ ",$"+str(Book_Split.Price[i])+"\n")
            
                    
                   
        Next=True
        a=1
        
        while True:
            
            option=str(input("Wanna a add more Books? If sure then enter s or if not then enter q" ))
            if(option.upper()=="S"):
                a=a+1
                print("Have a look to the following option:")
                for i in range(len(Book_Split.BookName)):
                    print("Enter",i ,"To Borrow Book",Book_Split.BookName[i])
                e=int(input())
                if(int(Book_Split.Quantity[e])>0):
                    print("Books are Available")
                    with open(m,"a")as d:
                        d.write(str(a)+"   "+Book_Split.BookName[e]+"    "+Book_Split.WriterName[e]+"\n")

                    Book_Split.Quantity[e]=int(Book_Split.Quantity[e])-1
                    with open("file.txt","w")as d:
                        for i in range(3):
                            d.write(Book_Split.BookName[i]+","+Book_Split.WriterName[i]+","+str(Book_Split.Quantity[i])+",$"+Book_Split.Price[i]+"\n")
                            This=False

                else:
                    break

            elif(option.upper()=="Q"):
                print("Thanks for lending book, please keep it safe")
                print("")
                
                This=True
                break

            else:
                print("Please follow the given instruction")

     
               
               
                      
            
               
      
       
    

        
                    

                

                    
                            













                                
                                    
                                    
                                            
                                            
                                                                        
                                        
                                            
                                    

                                           
                                             
                                                
                                        
                                           



                                                                                    

                                

                                    
                                        
                                    
                                        
                                    
                                                    
                                     
                                     
                                         
                                           
                                                
                                                
                                                
                                            
                                   
                                        
                                             
                            

                   
                    

                        
                    
                    
        

   

   
        
        
        
        
import Book_Split
import Date_Time
def BorrowBooks():
    This=False

    FullName =input("Enter your Full Name: ")


    m="Borrow-"+ FullName+".txt"
    with open(m,"w+")as d:
        d.write("Library Management System \n")
        d.write("Borrowed by:"+FullName+"\n")
        d.write("Date:"+Date_Time.getdate()+" Time:"+Date_Time.gettime()+"\n\n")
        d.write("No.  BookName  WriterName   \n")

    while This==False:
        print("Choose The Option Given Below:")
        for i in range(len(Book_Split.BookName)):
            print("Input", i, "Borrowing Book", Book_Split.BookName[i])
        
        e=int(input())
        
        if(int(Book_Split.Quantity[e])>0):
            print(f"You have been issued{Book_Split.BookName[e]} . Please keep it safe and return it within 10 days")
            with open(m,"a")as d:
                d.write("1."+Book_Split.BookName[e]+"\t"+Book_Split.WriterName[e]+"\n")
            Book_Split.Quantity[e]=int(Book_Split.Quantity[e])-1
            with open("file.txt","w+")as d:
                for i in range(3):
                    d.write(Book_Split.BookName[i]+","+Book_Split.WriterName[i]+","+str(Book_Split.Quantity[i])+ ",$"+str(Book_Split.Price[i])+"\n")
            
                    
                   
        Next=True
        a=1
        
        while True:
            #print("hello")
            option=str(input("Wanna a add more Books? If sure then enter s or if not then enter q" ))
            if(option.upper()=="S"):
                a=a+1
                print("Have a look to the following option:")
                for i in range(len(Book_Split.BookName)):
                    print("Enter",i ,"To Borrow Book",Book_Split.BookName[i])
                e=int(input())
                if(int(Book_Split.Quantity[e])>0):
                    print("Books are Available")
                    with open(m,"a")as d:
                        d.write(str(a)+"   "+Book_Split.BookName[e]+"    "+Book_Split.WriterName[e]+"\n")

                    Book_Split.Quantity[e]=int(Book_Split.Quantity[e])-1
                    with open("file.txt","w")as d:
                        for i in range(3):
                            d.write(Book_Split.BookName[i]+","+Book_Split.WriterName[i]+","+str(Book_Split.Quantity[i])+",$"+Book_Split.Price[i]+"\n")
                            This=False

                else:
                    break

            elif(option.upper()=="Q"):
                print("Thanks for lending book, please keep it safe")
                print("")
                
                This=True
                break

            else:
                print("Please follow the given instruction")

     
               
               
                      
            
               
      
       
    

        
                    

                

                    
                            













                                
                                    
                                    
                                            
                                            
                                                                        
                                        
                                            
                                    

                                           
                                             
                                                
                                        
                                           



                                                                                    

                                

                                    
                                        
                                    
                                        
                                    
                                                    
                                     
                                     
                                         
                                           
                                                
                                                
                                                
                                            
                                   
                                        
                                             
                            

                   
                    

                        
                    
                    
        

   

   
        
        
        
      
     
               
               
                      
            
               
      
       
    

        
                    

                

                    
                            













                                
                                    
                                    
                                            
                                            
                                                                        
                                        
                                            
                                    

                                           
                                             
                                                
                                        
                                           



                                                                                    

                                

                                    
                                        
                                    
                                        
                                    
                                                    
                                     
                                     
                                         
                                           
                                                
                                                
                                                
                                            
                                   
                                        
                                             
                            

                   
                    

                        
                    
                    
        

   

   
        
        
        
        
