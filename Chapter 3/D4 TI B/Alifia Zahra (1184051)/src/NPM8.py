def X(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 ==0):
          if(n !=0):
              print(n, end = "")
X(input("Masukan NPM anda :"))