def Book_Split():
    global BookName
    global WriterName
    global Quantity
    global Price

    BookName=[]
    WriterName=[]
    Quantity=[]
    Price=[]

    with open("file.txt","r")as d:
        lines=d.readlines()
        lines=[p.strip("\n") for p in lines]

        for i in range(len(lines)):
            b=0
            for e in lines[i].split(','):
                if(b==0):
                    BookName.append(e)
                elif(b==1):
                    WriterName.append(e)
                elif(b==2):
                    Quantity.append(e)
                elif(b==3):
                    Price.append(e.strip("$"))
                b+=1

                    
                    
                                  
                     
                    
                        
            
            
