a = 20
b = 30

def myfunc():
  global a
  a = 10
  b = 3
  print(a, b)

if __name__ == "__main__":
  myfunc()
  print(a, b)