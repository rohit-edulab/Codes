
def print_from_stream(n, stream=EvenStream()):
    
     num = 0
   # print(type(n))
     for i in range(n):
        if i == 0 :
          num = stream.get_next()
          if(num % 2 == 0):
            print(0)
          else:
            num = 0
            print(1)
        else:
          print(stream.get_next() - num)

