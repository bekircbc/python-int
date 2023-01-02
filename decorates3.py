def outer():
  def deco(func):
    def inner():
      func()
    
    return inner
  return deco

# f = outer()

@outer()
def do_something():
  print("do_something() wurde ausgeführt")
  
do_something()