m = 4 #change to input later
n = 2 #change to input later

arr_ai = [8,9,3,2] #change to dict
arr_score = [5,4,1,3]

temp_ai = []
temp_score = []

for i in range(len(arr_ai)): 
    if n >= arr_ai[i]:
        n = n + arr_score[i]
        print(arr_ai[i], "success")
    else:
        print(arr_ai[i], "defeat")
        temp_ai.append(arr_ai[i])
        temp_score.append(arr_score[i])

temp_ai.append(0) #just as separator
temp_score.append(0) #just as separator

# TODO: loop until no other value

print(n, "current score")
for i in range

for i in range(len(temp_ai)):
  if n >= temp_ai[i]:
    n = n + temp_score[i]
    print(temp_ai[i], "success")
  else:
      print(temp_ai[i], "defeat")
      temp_ai.append(arr_ai[i])
      temp_score.append(arr_score[i])
