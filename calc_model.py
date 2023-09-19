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
