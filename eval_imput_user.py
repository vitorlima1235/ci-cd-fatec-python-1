def calcular_vulneravel(expressao):
    # ❌ VULNERÁVEL: eval pode executar código arbitrário
    return eval(expressao)  # CodeQL vai detectar aqui!
    # Atacante pode fazer: expressao = "__import__('os').system('rm -rf /')"
"""
# Como corrigir:
import ast

def calcular_seguro(expressao):
    # ✅ SEGURO: Usar ast.literal_eval para expressões seguras
    try:
        return ast.literal_eval(expressao)
    except (ValueError, SyntaxError):
        raise ValueError("Expressão inválida")
"""