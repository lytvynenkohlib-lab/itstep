def checker(var_1):
    if type(var_1) is str:
        raise TypeError(f"sorry, we cant work{type(var_1)}")
    else:
        return var_1


f_var = 10
s_var = "dima"

checker(f_var)
checker(s_var)