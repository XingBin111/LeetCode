class Calculator:
    def __init__(self):
        self.operator = []
        self.num = []

    def calculate(self, s):
        if s[0].isdigit():
            self.operator.append("+")
        res = 0
        for e in s:
            if e.isdigit():
                if self.operator[-1] == "(":
                    self.operator.append("+")
                    self.num.append(int(e))
                else:
                    self.num.append(int(e))
            elif e == " ":
                continue
            elif e == ")":
                tmp = 0
                while self.operator[-1] != "(":
                    tmp += self.do_operator()
                self.operator.pop()
                self.num.append(tmp)
            else:
                self.operator.append(e)

        while len(self.num) > 0:
            res += self.do_operator()

        return res

    def do_operator(self):
        res = 0
        operator = self.operator.pop()
        if operator == "+":
            res += self.num.pop()
        elif operator == "-":
            res -= self.num.pop()
        elif operator == "*":
            tmp = self.num.pop()
            self.num.append(self.num.pop() * tmp)
        elif operator == "/":
            tmp = self.num.pop()
            self.num.append(self.num.pop() / tmp)
        return res


if __name__ == "__main__":
    s = "3*(-2+(3-2)*(4-1))"

    c = Calculator()
    print(c.calculate(s))

