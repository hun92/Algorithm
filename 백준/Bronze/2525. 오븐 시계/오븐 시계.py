#a와b를 공백을 기준으로 한 줄에 입력 박디 위함
a, b = map(int, input().split())
#요리에 필요한 시간을 timer을 입력받기 위함
timer = int(input())
#요리시간 timer은 분단위로 주어지기때문에
#현재 시간의 분인b와timer의 합이 60분보다 크거나같으면
if b + timer >= 60:
#현재 시간의 시인a에 (c+timer)//60을 더해주며 b는(b+timer)%60으로 바꿔주는 조건문울 만들어 주면 다음가 같다
    a = a +(b + timer)//60
    b = (b + timer)%60
#a + (b+timer)//60의 값이 25나 24와 같이 크거나 같아지면 다음 날로 넘어가 1과 0철험 출력되는 조건문을 만들어 줘야 한다
    if a >= 24:
        a = a - 24
        print(a,b)
    else:
#else문은 a + (b,timer)//60 값이 24보다 작을때이다        
        print(a,b)
else:
#b와 timer의 합이 60보다 작을 경우에는 다음과 같이 작성해 주면된다.    
    print(a,b + timer)
    