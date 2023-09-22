
def solve(equation : str):
    components = []
    list_equation = equation.split("")
    for i in range(0,len(equation)):
        try:
            if int(list_equation[i]) >= 0:
                num = []
                increase = 0
                while True:
                    try:
                        if int(list_equation[i+increase]) >= 0:
                            num.append(int(list_equation[i+increase]))
                        else:
                            break
                    except:
                        break
                
        except:
            pass