import datetime
def getdate():
    dt = datetime.datetime.now()
    return(dt.strftime("%x"))
def gettime():
    dt = datetime.datetime.now()
    return(dt.strftime("%X"))
    
    
