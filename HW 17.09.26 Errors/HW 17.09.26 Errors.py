a=int(input(f"для выбора ошибки напишите число от 1 до 4 \n"))
if a==1:
    # 1. (SyntaxError)
    print("Привет, мир )"
elif a==2:
    # 2. (RuntimeError / Exception)
    print(10 / 0)
elif a==3:
    # 3. (SemanticError)
    print(unknown)
elif a==4:
    # 4. (LogicalError)
    print(4 + 8 / 2)
