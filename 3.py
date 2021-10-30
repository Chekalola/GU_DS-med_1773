class MyExeption(TypeError):
    def __init__(self,txt):
        self.txt = txt
lit_list = []
command = ""
while command != 'stop':
    str_input = input("Input only nums:")
    try:
        num = ['1','2','3','4','5','6','7','8','9']
        for i in str_input:
            if i not in num:
                raise MyExeption("This is not a number!")
    except MyExeption as err:
        print(err)
    else:
        lit_list.append(str_input)
    command = input('Write "stop" for stop inputing:')
print(lit_list)