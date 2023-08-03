#match statement 

a=int(input("ENTER ANY NUMBER X:"))
match a:
    case 0 :
        print( "ZERO")
    case 1:
        print ("ONE")
    case _:
        print(a)
    