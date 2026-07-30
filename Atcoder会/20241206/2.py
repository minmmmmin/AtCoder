H,W = map(int, input().split())
l = [input() for _ in range(H)]

for i in range(H):
  for j in range(W):
    if l[i][j] == "s":
      for k in range(-1, 2):
        for n in range(-1, 2):
          try:
            if l[i+k][j+n] == "n" and i+k >= 0 and j+n >= 0:
              if l[i+k*2][j+n*2] == "u" and i+k*2 >= 0 and j+n*2 >= 0:
                if l[i+k*3][j+n*3] == "k" and i+k*3 >= 0 and j+n*3 >= 0:
                  if l[i+k*4][j+n*4] == "e" and i+k*4 >= 0 and j+n*4 >= 0:
                    for m in range(5):
                      print(i+k*m+1, end=" ")
                      print(j+n*m+1)
                    
          except IndexError:
            continue