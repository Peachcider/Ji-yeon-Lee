import string #문자열모듈 사용
alp_str=string.ascii_uppercase+string.ascii_lowercase #알파벳 대문자+소문자 리스트 생성


import random #랜덤모듈 사용


def caeser_cipher(a,b): #카이사르 암호를 만드는 함수 a=문자열 이동 횟수, b=변환하고자 하는 문자
    push_str=alp_str[a:]+alp_str[:a] #원하는 만큼 알파벳 문자열을 이동
    idx=alp_str.index(b) #원래의 알파벳 문자열에서 바꾸고자 하는 알파벳의 위치를 찾음
    return push_str[idx] #이동시킨 문자열에서 원래 문자열의 위치에 있는 알파벳 반환


def caeser_solve(a,b):#카이사르 암호를 해석하는 함수. a=문자열 이동 횟수, b=변환하고자 하는 문자
    push_str=alp_str[a:]+alp_str[:a] #제시된 만큼 알파벳 문자열을 이동
    idx=push_str.index(b) #이동한 문자열에서 바뀐 알파벳의 위치를 찾음
    return alp_str[idx] #원래 문자열에서 바뀐 문자열의 위치에 있는 알파벳 반환

#"Keep Your Secret" UI

chiper = '''

      ____________________________
     ㅣ                          ㅣ  
     ㅣ       쉿! 비밀이야       ㅣ
     ㅣ                          ㅣ
     ㅣ------------★------------ㅣ
     ㅣ                          ㅣ
     ㅣ     Keep Your Secret     ㅣ
     ㅣ                          ㅣ
    _________________________________

'''

menu1 = '''
    어떤 작업을 실행하시겠습니까?
    1. 암호 생성
    2. 암호 해독
'''

menu2 ='''
    어떤 암호를 생성하시겠습니까?
    1. 카이사르 암호 (영어 -> 영어 암호)
    2. 카이사르 십진수 암호 (영어, 한글, 숫자 -> 십진수 암호)
'''
menu3 ='''
    어떤 암호를 해독하시겠습니까?
    1. 카이사르 암호 (영어 암호 -> 영어)
    2. 카이사르 십진수 암호 (십진수 암호 -> 영어, 힌글, 숫자)
'''
print(chiper)
r=0
while r==0:
    order1 = input(menu1)
    if order1 == '1':
        order2 = input(menu2)
        if order2 == '1':
            print("카이사르 암호(영어 -> 영어 암호)를 시작하겠습니다.")

            #카이사르 암호화
            num_push=random.randrange(1, 52) #알파벳 문자열 이동시킬 값 랜덤 선정.
            str_in=input("암호화할 문장을 입력하시오:") #암호화할 문장 입력. str_in=암호화할 문장
            print("암호화된 문장:",end="") 
            print(alp_str[num_push],end="") #출력할 암호 제일 앞자리에 이동시킨 횟수를 알파벳의 형태로 출력
            for spl in str_in: #암호화하고자 하는 문장(이하 평문)을 한글자씩 변환. spl=spell,평문의 한 글자
                if spl in alp_str: #평문의 해당 글자가 알파벳일 경우(알파벳 리스트에 포함된 경우)
                    print(caeser_cipher(num_push,spl), end="")#카이사르 암호화 함수 호출
                else: #평문의 해당 글자가 알파벳이 아닐 경우.
                    print(spl,end="") #그대로 출력.
            print(end="\n")
            r=1
        elif order2 == '2':
            print("카이사르 암호(영어, 한글, 숫자 -> 십진수 암호)를 시작하겠습니다")

            #카이사르-진수 암호화
            num_push=random.randrange(1, 52)
            str_in=input("암호화할 문장을 입력하시오:")
            print("암호화된 문장:",end="")
            print(num_push,end=" ") #가장 앞자리에 알파벳 리스트를 이동시킨 횟수를 출력.
            for spl in str_in:
                if spl in alp_str:
                    print(ord(caeser_cipher(num_push,spl)), end=" ") #ord()=10진수 변환 함수, 해석을 위해 split()을 사용하므로 각 글자마다 반드시 띄어쓰기(end=" ")포함.
                else:
                    print(ord(spl),end=" ")
            print(end="\n")
            r=1
        else:
            print("\n", "1과 2 둘 중 하나를 선택해주세요.", end="")

    elif order1 == '2':
        order3 = input(menu3)
        if order3 == '1':
            print("카이사르 암호 해독(영어 암호 -> 영어)을 시작하겠습니다.")
            #카이사르 해석
            str_in=input("해석할 문장을 입력하시오:") #암호문 입력. str_in=해석할 암호문
            print("해석된 문장:",end="") 
            num_push=alp_str.index(str_in[0])#암호문의 제일 앞 알파벳이 나타내는 수 만큼 알파벳 리스트 이동. num_push=이동한 알파벳 리스트
            for spl in str_in[1:]: #암호문의 두번째 글자부터 한글자씩 해석.
                if spl in alp_str: #암호문의 해당 글자가 알파벳일 경우
                    print(caeser_solve(num_push,spl), end="") #카이사르 암호 해석 함수 호출.
                else: #암호문의 해당 글자가 알파벳이 아닐 경우.
                    print(spl,end="") #그대로 출력.
            print(end="\n")
            r=1
        elif order3 == '2':
            print("카이사르 십진수 암호 (십진수 암호 -> 영어, 힌글, 숫자)를 시작하겠습니다.")
            #카이사르-진수 해석
            str_in=input("해석할 문장을 입력하시오:")
            print("해석된 문장:",end="")
            str_list=str_in.split() #띄어쓰기를 기준으로 각 어절을 문자열형태로 리스트화.
            num_push=int(str_list[0]) #암호문의 가장 앞자리만큼 알파벳 리스트를 이동.
            for spl in str_list[1:]: 
                spl_solve=chr(int(spl)) #암호문의 각 항목(10진수)을 문자화.
                if spl_solve in alp_str: #문자화 된 글자가 알파벳이면.
                    print(caeser_solve(num_push,spl_solve), end="") #카이사르 암호 해석 함수 호출. 
                else:
                    print(spl_solve,end="")
            print(end="\n")
            r=1
        else:
            print("\n", "1과 2 둘 중 하나를 선택해주세요.", end="")
    else:
        print("\n", "1과 2 둘 중 하나를 선택해주세요.", end="")
        
