class Calculator:
    def __init__(self):
        self.operator = ["+"]
        self.num = []

    def calculate(self, s):
        for e in s:
            if e.isdigit():
                if self.operator[-1] == "*":
                    n = self.num.pop() * int(e)
                    self.num.append(n)
                    self.operator.pop()
                elif self.operator[-1] == "/":
                    n = self.num.pop() / int(e)
                    self.num.append(n)
                    self.operator.pop()
                else:
                    self.num.append(int(e))
            elif e == " ":
                continue
            else:
                self.operator.append(e)

        res = 0

        while len(self.num) > 0:
            operator = self.operator.pop()

            if operator == "+":
                res += self.num.pop()
            else:
                res -= self.num.pop()
        return res


if __name__ == "__main__":
    s = "3 - 4 * 2 + 6"

    c = Calculator()
    print(c.calculate(s))

