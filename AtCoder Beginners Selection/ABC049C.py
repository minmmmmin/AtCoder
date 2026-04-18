s = input()
s = s.replace("eraser","")#文字なしに置き換える
s = s.replace("erase","")
s = s.replace("dreamer","")
s = s.replace("dream","")

if s == "":
  print("YES")
else:
  print("NO")