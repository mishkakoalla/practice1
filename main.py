def main ():
    try:
        print("решим уравнение")
        a = int(input("Введите значение a :"))
        b = int(input("Введите значение b :"))
        x = int(input("Введите значение x :"))
        if x>5:
            y=(5*a*b)/(x**2 + a**2)
        else :
            y=4*(a+b-x)**2
            print("Значение Y =%.1f"%y)
    except:
        print("неверные значения")
main()


