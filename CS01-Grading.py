K=int(input("คะแนนเก็บ:"))
J=int(input("คะแนนสอบกลางภาค:"))
I=int(input("คะแนนสอบปลายภาค:"))

score=K+J+I
if 80 <= score <= 100:
        print ('Grade: A')
elif 75 <= score <=79:
        print ('Grade: B+')
elif 70 <= score <= 74:
        print ('Grade: B')
elif 65 <= score <= 69:
        print ('Grade: C+')
elif 60 <= score <= 64:
        print ('Grade: C')
elif 55 <= score <= 59:
        print ('Grade: D+')
elif 50 <= score <= 54:
        print ('Grade: D')
elif 0 <= score <= 49:
        print ('Grade: F')
else:
        print('number between 0 - 100')