from sympy import sympify

def evaluate_expression(expression, precision=5):
    """
    Evaluate mathematical expression
    """
    try:
        result = sympify(expression).evalf(precision)
        return result
    except Exception as e:
        return f"Errore nell'espressione: {e}"


def main():
    expression1 = "((5+2)+(3-9))"  # Corretto
    expression2 = "((5+2)+(3-9)"   # Parentesi mancanti
    expression3 = "(5+2)+3-9)"     # Parentesi non bilanciate

    print(f"Espressione: {expression1} -> Risultato: {evaluate_expression(expression1)}")
    print(f"Espressione: {expression2} -> Risultato: {evaluate_expression(expression2)}")
    print(f"Espressione: {expression3} -> Risultato: {evaluate_expression(expression3)}")


if __name__ == '__main__':
 	main()