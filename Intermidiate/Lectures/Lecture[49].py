

# :: Youtube Playlist Content : 

# --> lecture-246 : EH - 10 ( thoda niche hai playlist mai ).
# --> lecture-247 : EH-11. 
# --> lecture-248 : EH-12. 
# --> lecture-249 : EH-13 (Exercise). 
# --> lecture-250 : EH-14. 


# _______________________________________________________________________________________________________________________ 



# NOTE: What will happen when exceptions occur in one thread? will it impact other threads?

# - Answer : No , it does not effect other thread execution because thread have their seperate execution flow. 


# :: Exceptions in Multi-threading : 


# - Ex :  ( without exception handelling , ,it gives error for the display() and then continue the show() function execution )



# from threading import * 
# from time import sleep 

# def display():
#     for i in range(4):
#         sleep(0.1)
#         print("hello" + 10)

# def show():
#     for i in range(4):
#         print("hello")
#         sleep(0.5)



# t1 = Thread(target = display)
# t2 = Thread(target=show)


# t1.start()
# t2.start()


# t1.join()
# t2.join()

# for i in range(4):
#     print("Bye")












# :--> What happens for exception in thread ? 

# - The interpreter calls threading.excepthook() with one argument i.e named tuple with 4 argument. 

# 1.) The exception class.
# 2.) Exception instance / value.
# 3.) A traceback object. 
# 4.) Thread name. 




# NOTE:  

# --> For main thread :  sys.excepthook runs.
# --> For created thread :  threading.excepthook runs. 









# ________________________________________________________________________________________________________________________________________







