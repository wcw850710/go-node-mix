import socket
from typing import get_type_hints
from functools import wraps
from inspect import getfullargspec

# s = socket.socket()
# s.send()

def add(a, b):
  """
  :param a: int
  :param b: int
  :return: int
  """
  return a + b

# 函數類型寫法
def add2(a: int, b: int = 10) -> int:
  validate_input(add2, a = a, b = b)
  return a + b

def validate_input(obj, **kwargs):
  hints = get_type_hints(obj)
  print(hints)
  # print(add2.__annotations__)
  for param_name, param_type in hints.items():
    if param_name == "return":
      continue
    if not isinstance(kwargs[param_name], param_type):
      raise TypeError("參數：{} 類型錯誤，應該是：{}".format(param_name, param_type))

def type_check(decorator):
  @wraps(decorator)
  def wrapped_decorator(*args, **kwargs):
    func_args = getfullargspec(decorator)[0]
    kwargs.update(dict(zip(func_args, args)))
    validate_input(decorator, **kwargs)
    return decorator(**kwargs)
  return wrapped_decorator

@type_check
def add3(a: int, b: int = 10) -> int: # 裝飾氣版本德 add2
  return a + b

if __name__=="__main__":
  print(add2(1, 2))
  print(add2(1))
  print(add3("1"))
  # print(add2("1")) # 顯示同上
