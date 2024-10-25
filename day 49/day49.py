# შექმენი პროგრამა რომელიც მიიღებს მოსწავლის ქულას, პირობითი განცხადების გამოუტანს შეფასებას შემდეგი სისტემით:
# score > 80: A
# score > 50: B
# score < 40: C

score = int(input('enter your score'))
if score > 80:
    print('A')
elif score > 50:
    print('B')
    