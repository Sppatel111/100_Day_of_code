# num1=20
# num2=input("enter any number:")
# def add(n1,n2):
#     return n1+n2
#
# try:
#     x=add(num1,num2)
# except TypeError as e:
#     print(e)
# else:
#     print("add went well!")
#     print(x)
# finally:
#     print("executed finally!")


# try:
#     f=open("new.txt","r")
#     f.write("write the file.")
#
# except FileNotFoundError as e:
#     print(e)
# except:
#     print("all type error.")
# finally:
#     print("executed finally.")


# def ask_for_int():
#     while True:
#         try:
#             result=int(input("enter the number:"))
#         except:
#             print("Whoops!! that is not number")
#             continue
#         else:
#             print("yeah thank you")
#             break
#         finally:
#             print("executed finally")
#
# ask_for_int()

# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError as e:
#     print(e)
# except:
#     print("general error!!")


# try:
#     x=5
#     y=0
#     z=x/y
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("error")
#
# finally:
#     print("all done")

def ask():
    while True:
        try:
            n=int(input("enter the number:"))
        except:
            print("please try again!!")
            continue
        else:
            break
        finally:
            print("last finally executed.")

    print("your number square is:")
    print(n**2)


ask()