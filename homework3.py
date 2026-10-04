import ast
import operator

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def safe_eval(node):
  if isinstance(node, ast.Constant):
    if isinstance(node.value, (int, float)):
      return node.value
    raise TypeError(f"Недопустимий тип даних: {type(node.value)}")

  elif isinstance(node, ast.BinOp):
    if type(node.op) in operators:
      left = safe_eval(node.left)
      right = safe_eval(node.right)
      return operators[type(node.op)](left, right)
    raise TypeError(f"Недопустима операція: {type(node.op)}")

  elif isinstance(node, ast.UnaryOp):
    if type(node.op) in operators:
      operand = safe_eval(node.operand)
      return operators[type(node.op)](operand)
    raise TypeError(f"Недопустима унарна операція: {type(node.op)}")

  else:
    raise TypeError(f"Недопустимий синтаксис виразу: {type(node)}")


def calculate(expression):
  try:
    node = ast.parse(expression, mode="eval").body
    return safe_eval(node)
  except ZeroDivisionError:
    return "Помилка: Ділення на нуль!"
  except Exception as e:
    return f"Помилка обчислення: {e}"


if __name__ == "__main__":
  expr = "2 + 3 * (4 - 1) ** 2"
  print(f"Вираз: {expr}")
  print(f"Результат: {calculate(expr)}")