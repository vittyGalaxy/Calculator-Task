import re


class Parser:
    def __init__(self):
        self.is_initialized = False
        self.expr = ""

    def set_expr(self, expr):
        self.expr = expr
        self.is_initialized = True

    def eval_parentheses(self):
        while '(' in self.expr:
            self.expr = re.sub(r'\(([^()]+)\)', lambda x: str(self.eval_simple(x.group(1))), self.expr)
        return self.eval_simple(self.expr)

    def eval_simple(self, expr):
        # TODO: levare eccezione, tornando magari un valore booleano
        # se é true, allora é andata bene altrimenti é un risultato da non mostrare
        print(eval(expr))
        # try:
        #     return eval(expr)
        # except Exception as e:
        #     raise ValueError(f"Errore durante l'analisi dell'espressione: {e}")

    def parse_expression(self):
        self.expr = self.expr.replace(" ", "")
        return self.eval_parentheses()


def main():
    parser = Parser()
    expr_correct = "3*(5-2) + (3+1)"
    wrong_expr_1 = "3(3+2)"
    wrong_expr_2 = "3*(3+2"
    wrong_expr_3 = "3*3+"
    wrong_expr_4 = ")3+3("
    parser.set_expr(wrong_expr_4)
    print(parser.parse_expression())


if __name__ == '__main__':
    main()
