from collections import Counter

MAX_LOOP_COUNT = 1000

repeating_pattern = []

def to_base(n,b):
    s = ""
    while n:
        s = str(n % b) + s
        n //= b
    return s


def base_subtraction(x,y,base):
  x_int = int(x, base)
  y_int = int(y, base)
  
  z = to_base((x_int - y_int), base)
  print("z", z, type(z))
  return z

def answer(minionId, base):
  
  n = minionId
  len_n = len(list(n))
  print(len_n)
  count = 0 
  
  while count < MAX_LOOP_COUNT:
    
    n = list(n)
    
    if n == 0:
      return 1 
    
    x = int(''.join(sorted(n, reverse=True)))
    y = int(''.join(sorted(n)))
    
    print("x", x, type(x))
    print("y", y, type(y))
    
    if base == 10:
      z = x - y
      
    else:
      z = base_subtraction(str(x), str(y), base)
      
    z = str(z).zfill(len_n)
    print(z)
    n = str(z)
    print("n", n)
    count = count + 1
    print("count", count)
    print(n, type(n))
    
    repeating_pattern.append(n)
  
answer('210022', 3)  

result = []

count_occurence = Counter(repeating_pattern)
for k,v in count_occurence.items():
  if v > 1:
    result.append(v)

print(count_occurence)
print(len(result))
    
  
  


    
  