total_seconds = 9875 
Hour = total_seconds//3600 # jeak yr lek kot
minutes = (total_seconds % 3600)// 60 # % jeak yr somnol
seconds = (total_seconds % 60)

print("Hour: ", Hour)
print("minutes: ", minutes)
print("seconds: ", seconds)
print("9875 seconds = ",Hour,'H', minutes,'m',seconds,'s')
print(f"{Hour} H - {minutes} m -{seconds} s")