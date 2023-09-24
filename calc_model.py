class SimpleCalcModel:
    __display = '2+2*2'

    def calculate(self):
        try:
            result = eval(self.__display)
            self.__display = str(result)
        except SyntaxError:
            print("Некоректное выражение")

    def command(self, key: str):
        if key != "=": 
            if key.isdigit():
                if self.__display == "0": 
                    self.__display = key
                else: 
                    self.__display += key   
            else: 
                if self.__display[-1] not in "+-*/": 
                    self.__display += key
            
            if key == "C": 
                if len(self.__display) > 1: 
                    self.__display = self.__display[:-1]

            if key == "AC":
                self.__display = "0"
        else: 
            print(self.__display) 
            self.calculate() 

    def get_display(self):
        return self.__display


class AccountCalcModel(SimpleCalcModel):
    def command(self, key:str):
        if key in "()":
            self._display += key
        elif key == "%":  # 3*7 - 1 => "3*7". "-1"
            last_value_index =  max(self._display.rfind("-"),
                                    self._display.rfind("+"),
                                    self._display.rfind("*"),
                                    self._display.rfind("/"))
            if last_value_index < 0:
                return
            last_value = self._display[last_value_index:]
            self._display = self._display[:last_value_index]
            self.calculate()
            res1 = eval(f"{self._display} * {last_value} / 100")
            self._display += str(res1)
        else:
            super().command(key)


if __name__ == "__main__":
    print("Testing model:")
    calc = AccountCalcModel()

    calc.command("3")
    calc.command("*")
    calc.command("3")
    calc.command("3")
    calc.command("3")
    calc.command("3")
    calc.command("3")
