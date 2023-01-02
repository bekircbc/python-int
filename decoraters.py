
# def outer(func):
#   counter=0
#   def inner(x):
#     nonlocal counter
#     print("Wurde bisher ausgeführt: " + str(counter))
#     counter+=1
#     return func(x)
#   return inner

# @outer
# def calculate_something(x):
#   print("calculate_something(" + str(x) + ")")
#   return x * x

# do_something=outer(do_something) # the same as @outer

# print(calculate_something(5))
# print(calculate_something(5))


# anstatt do_something outer ausgeführt.. 

def outer(func):
  cached={}
  def inner(x):
    if x in cached:
      return cached[x]
    result = func(x)
    cached[x]=result
    return result
  return inner

@outer
def calculate_something(x):
  print("calculate_something(" + str(x) + ")")
  return x * x

# do_something=outer(do_something) # the same as @outer

print(calculate_something(5))
print(calculate_something(5))