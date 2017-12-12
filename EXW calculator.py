"""
http://exportarya.com/calcular-precio-exw.asp
EXW()
分母: MPN + MPE + MO + ENV + EMB + CER + GFB + OG
分子: 1- (IP + (U/ (1 -IG))
error handling = 只能數字, 分母不為0, 不能空白
若中間輸入錯誤需從頭輸入

此版本還差分母ZeroDivisionError後無法跳回IG值
 """


def EXW():
    t_list = ["MPN", "MPE", "MO", "ENV", "EMB", "CER", "GFB", "OG"]
    t_dict = {}.fromkeys(t_list)
    b_list = ["IP", "U", "IG"]
    b_dict = {}.fromkeys(b_list)
    top_amount = 0
    bottom_amount = 0
    restart1 = True
    restart2 = True

    #分子的計算
    while restart1:
        restart1 = False
        for key in t_dict:
            if t_dict[key] is None:
                try:
                    t_dict[key] = float(input("Please input " + key))
                except ValueError:
                    print("Please input an integer")
                    restart1 = True
                    break
            top_amount += t_dict[key]
    print("User input:", t_dict)
    print("The top value of EXW is", top_amount)

    # 分母的計算
    while restart2:
        restart2 = False
        for key in b_dict:
            if b_dict[key] is None:
                try:
                    b_dict[key] = float(input("Please input " + key))
                    if b_dict["IG"] == 1:
                        raise ZeroDivisionError
                except ValueError:
                    print("Please input an integer")
                    restart2 = True
                    break
                except ZeroDivisionError as e:
                    print(e, "IG value shouldn't be 1.")
                    restart2 = True
                    break
    #bottom_amount = (1 - (b_dict["IP"] + (b_dict["U"] / (1 - b_dict["IG"]))))

    print("The bottom value of EXW is",  bottom_amount)

    print("The EXW value is ", top_amount / bottom_amount)

EXW()