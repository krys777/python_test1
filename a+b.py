
class test:

  
  p=5

  def readNK(self):

    from sys import stdin, stdout

    n, k = stdin.readline().split()
    print(n + ' ' + k)

    n = int(n)
    k = int(k)

    print(self.p)

    return([n,k])

def BlahFunc():
  #hi hi 

def main():

  testObj = test()
  a=testObj.readNK()
  print(a)

'''
  cnt = 0
  lines = stdin.readlines(n+2)
  print(lines)

  for line in lines:
    if int(line) % k == 0:
      cnt += 1
 
  stdout.write(str(cnt))
'''
if __name__ == "__main__":
    main()
