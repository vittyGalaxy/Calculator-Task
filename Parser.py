import re


class Parser:
    def __init__(self):
        def eval_parentheses(expr):
            while '(' in expr:
                expr = re.sub(r'\(([^()]+)\)', lambda x: str(eval_simple(x.group(1))), expr)
            return eval_simple(expr)

        def eval_simple(expr):
            try:
                return eval(expr)
            except Exception as e:
                raise ValueError(f"Errore durante l'analisi dell'espressione: {e}")

        def parse_expression(expr):
            expr = expr.replace(" ", "")
            return eval_parentheses(expr)
