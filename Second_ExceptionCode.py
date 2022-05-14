try:
    #a = 10
    #a/0
    list = [10,20,30,40]
    list[6]
except  ZeroDivisionError:
    print("Not Divisible By Zero")

except IndexError:
    print("ArrayIndex Problem")

except :
    print("SomeThing Wrong Happened In Code")

else:
    print("EveryTing is Ok")




# U can Give into List Also

#IndexError
#ZeroDivisionError