# 파이썬으로 학생 기록 관리 프로그램 만들기

## 목록

1. 주요기능 설명  
2. 기능별 코드 설명


### 1. 주요 기능 설명
1. 학생 성적 입력 받기 

* 학생의 성적 기록을 학번 -> 국어 성적 -> 영어 성적 -> 수학 성적 순으로 받아준다.
* 이떄 중복되는 학번의 학생 성적은 입력 받지 못하도록 하며 , 0 이하의 숫자도 학번으로 지정되지 못하게 한다.
* 각 과목의 성적을 받을 때에는 0~100 사이에 정수만 입력 가능 하게하며 다른 값이 들어오면 해당과목의 점수를 다시 입력받는다.  
* 성적 입력이 완료되면 저장여부를 확인한다.
* 저장시에 입력된 학생의 총점과 평균을 확인시켜준 후 메인 화면으로 나간다.

2. 입력된 성적 현황 출력

* 입력된 학생의 정보를 학번순(오름차순)으로 출력한다.

3. 성적 수정

* 저장되어 있는 학생정보를 학번으로 불러와서 수정/삭제 한다.
* 해당 정보를 가지는 학생이 맞는지 확인한다.
* 저장되어 있지 않은 학생(학번) 입력시 메인 화면으로 돌아간다.
* 수정시 enter 입력 하면 기존 점수로 수정한다.
* 수정 점수가 0~100 사이의 정수가 아니면 다시 입력받는다
* 수정된 점수를 저장 여부를 확인한다.

4. 프로그램 종료 및 저장

* 해당 데이터를 csv로 저장하며 저장할 파일의 이름을 입력받는다.
* 다음에 프로그램을 실행시 저장된 파일을 자동으로 불러온다.

### 2. 기능별 설명

* 전에 사용했던 데이터 불러오기
프로그램 시작시 자동으로 전에 입력한 데이터를 불러온다
<pre>
<code>
  f = open('./num.txt', 'r') #csv 파일 이름이 저장되어 있는 num.txt 파일을 읽어 온다/
      
  while True:     #csv 파일을 한줄씩 읽어 df 에 넣는다
      line = f.readline()

      if not line: 
            break    

      df= pd.read_csv('C:\kim\\{}.csv'.format(line.rstrip("\n")),encoding= ' UTF-8')

  f.close()
  
  #df 의 인덱스를 번호랑 같게 설정 후 내림차순으로 정렬해준다. 
  
  f.index = df['번호']  
  df = df.sort_index()
</code>
</pre>


* 메인 화면
 
![cap1](https://user-images.githubusercontent.com/91679614/150639662-4f7f902b-2418-47cf-9ce3-5c86052982c8.PNG)

* 학번 입력 예외 처리

메인화면에서 1 을 선택하면 아래 화면처럼 학번을 입력할 수 있는 창이 뜬다

![cap2](https://user-images.githubusercontent.com/91679614/150639775-066db5de-d76d-4357-8c84-c23a768f909c.PNG)

학번에 문자열을 치면 입력할 수 없다는 메세지와 함께 매인화면으로 돌아간다

![cap3](https://user-images.githubusercontent.com/91679614/150639779-7aaca5f5-f049-459d-86df-3f3141b9f728.PNG)

학번에 0 이하의 수를 입력해도 입력할수 없다는 메세지와 함께 메인 화면으로 돌아간다

![cap4](https://user-images.githubusercontent.com/91679614/150639781-ea0c5f9e-9c69-4a67-b9a5-6d4c481f6ac8.PNG)

이미 있는 학번을 입력하면 존재하는 학번은 입력할 수 없다는 메세지와 함께 메인 화면으로 돌아간다

![cap8](https://user-images.githubusercontent.com/91679614/150640121-04a5550e-1197-46b3-8e3c-d23a8538e9aa.PNG)

*과목별 성적 입력 코드

![cap5](https://user-images.githubusercontent.com/91679614/150639782-39fcf126-34fc-4cec-a362-920413f8d1f1.PNG)

과목별 성적에 0~100 까지 정수가 아닌 다른것을 입력하면 해당과목의 점수를 다시 입력받는다.

![cap9](https://user-images.githubusercontent.com/91679614/150640227-eafb8ddd-b7cf-4930-8208-6ade53dceaf1.PNG)

* 저장여부 확인 후 저장

저장을 하지않을시 메세지 출력과 함꼐 메인화면으로 돌아간다

![cap10](https://user-images.githubusercontent.com/91679614/150640278-bea9ba8e-a39b-4c3f-b858-23573ad67e0f.PNG)

저장시 총합 과 평균 값 출력후 메인화면으로 돌아간다

![cap6](https://user-images.githubusercontent.com/91679614/150639830-a96ed74b-5a98-4246-8fca-76632aa06e8e.PNG)

*성적 현황 출력

메인 화면에서 2를 입력하면 아래 이미지 와 같이 성적 현황이 출력된다.

![cap7](https://user-images.githubusercontent.com/91679614/150639904-62ca86bb-9fa7-4579-b677-90eaf69052c9.PNG)

* 성적 수정/ 삭제 학생 입력 후 정보확인
메인화면에서 3을 입력하면 수정할 학생의 학번을 입력하는 창이 나온다

저장되지 않은 학번 입력시 존재하지 않는다는 메세지와 함께 메인 화면으로 돌아간다

![cap11](https://user-images.githubusercontent.com/91679614/150640400-c757b8a5-c6bb-4fb7-b32d-b44e94309246.PNG)

수정할 학번 입력란에 문자열을 입력해도 존재하지 않는다는 메세지와 함께 메인 화면으로 돌아간다

![cap12](https://user-images.githubusercontent.com/91679614/150640401-feddcb71-0484-40ae-b826-a48407987b98.PNG)

존재 하는 학번을 입력시에 학생의 정보를 출력하며  찾는 학생이 맞는지의 여부를 입력창이 나온다

![cap13](https://user-images.githubusercontent.com/91679614/150640403-3db974f2-81d3-49fd-9e8c-f757e7768505.PNG)
      
* 학생 일치 여부 및 수정/ 삭제 여부 

일치 여부 에서 n 을 입력하면 메인화면으로 돌아간다

![cap14](https://user-images.githubusercontent.com/91679614/150640570-e7cc4046-fe62-4427-a23f-a3089546ccd2.PNG)

일치 여부에서 y 를 입력하면 수정 삭제 여부를 물어본다
![cap15](https://user-images.githubusercontent.com/91679614/150640571-9421e6e7-f87c-4634-ac36-72ac435f4318.PNG)

* 성적 삭제

삭제를 선택하면 삭제 되었다는 메세지와 함께 메인 화면으로 돌아간다.
![cap16](https://user-images.githubusercontent.com/91679614/150640637-9c1129a8-41e4-4f50-b1c3-7a3595fa28ad.PNG)


*성적 수정시 수정 성적 입력

수정을 선택 하면 수정 할 점수를 입력 받을 수 있으며 enter를 쳐 넘어가면 해당점수는 기존의 점수로 입력받는다.
그후 저장 유무를 입력 받는다

![cap17](https://user-images.githubusercontent.com/91679614/150640691-b424b8d0-6bc4-4dd1-9d93-98ed99b18fe9.PNG)


* 프로그램 종료, 파일저장

메인 화면에서 4를 입력 받으면 해당 데이터를 csv로 저장하는데 csv 파일 이름을 입력받고 프로그램을 종료한다

![capfi](https://user-images.githubusercontent.com/91679614/150640774-a88771db-4eac-4e0f-ad42-1d7f0f155bb8.PNG)

