def hello():
  print("Hello world")
  
def pack(argument_one,argument_two,argument_three):
  return [argument_one,argument_two,argument_three]

def eat_lunch(food):
  if len(food) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(food)):
      if i == 0:
        print(f"First I eat {food[0]}")
      else:
        print(f"Next I eat {food[i]}")

hello()
print(pack("argument_one","argument_two","argument_three"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])