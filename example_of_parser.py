# importo le regedit
import re

# Funzione per valutare l'espressione tra parentesi
def eval_parentheses(expr):
    # Trova tutte le espressioni tra parentesi
    while '(' in expr:
        expr = re.sub(r'\(([^()]+)\)', lambda x: str(eval_simple(x.group(1))), expr)
    return eval_simple(expr)

# Funzione per valutare semplici espressioni aritmetiche (senza parentesi)
def eval_simple(expr):
    try:
        # Utilizza la funzione eval per valutare l'espressione
        return eval(expr)
    except Exception as e:
        raise ValueError(f"Errore durante l'analisi dell'espressione: {e}")

# Funzione principale per valutare l'espressione
def parse_expression(expr):
    expr = expr.replace(" ", "")  # Rimuove gli spazi
    return eval_parentheses(expr)

# Esempio di utilizzo
expr = "(5+2) + (3+1)"
result = parse_expression(expr)
print(f"Risultato: {result}")
