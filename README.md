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

### 2. 기능별 코드 설명

* 전에 사용했던 데이터 불러오기
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

* 메인 화면 출력

<pre>
<code>
  print('===================================')
  print('==피식 고등학교 성적처리 프로그램==')
  print('===================================')
  print('<<메뉴>>')
  print('1. 성적입력')
  print('2. 성적현황')
  print('3. 성적수정')
  print('4. 종료')
  print('===================================')
  num_menu = input(">>>")
  print('===================================')
</code>
</pre>


* 학번 입력 예외 처리

<pre>
<code>
if num_menu == '1':
    print('학생 성적 입력')
    print('===================================')
    
    #학번입력 예외처리 부분 
    try:
   
      st_num = str(input('학번:')) # 학번 입력받기
      st_num = int(st_num )       
   
    except ValueError   as e:  # 학번이 정수인지 확인 
      print('{}는 입력할 수 없습니다.'.format(st_num))
      continue
      
    else:
   
      i = []
      for a in range(len(df.index)): # 학번이 중복인지 확인 
        p = df.index[a] 
        i.append(p)

      if st_num <= 0: # 학번이 양수인지 확인 
        print('{}는 입력할 수 없습니다.'.format(st_num))
        continue
   
      elif st_num in i : # 학번이 정수인지 확인 
        print('{}은(는)성적이 존재하는 학생입니다.'.format(st_num))
        continue
</code>
</pre>

*과목별 성적 입력 코드

<pre>
<code>

  #국어 입력
    while True:
  

      try:
        st_num_kor = str(input('{}의 국어 점수: '.format(st_num)))
        st_num_kor = int(st_num_kor)
      
      except ValueError as e:
        print('정수 0~100를 입력하시오')
        
      else:
        if st_num_kor <= 0:
          print('정수 0~100를 입력하시오')
          
        elif st_num_kor > 100 :
          print('정수 0~100를 입력하시오')

        else:
          break
</code>
</pre>

* 저장여부 확인 후 저장

<pre>
<code>
    #저장 여부
    y_or_n = input('{}의 점수를 저장하시겠습니까(y/n)?'.format(st_num))
    
    if y_or_n == 'n':
      print('학생({})의 점수가 저장되지않았습니다.'.format(st_num))
      
    elif y_or_n == 'y':
     
      df2 = pd.Series([st_num_kor, st_num_eng, st_num_math])
      b = int(df2.sum())
      c = float(df2.mean())
      c = round(c,2)
      
      if c >=90:
        df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'A']
      elif 90> c >=80:
        df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'B']
      elif 80 > c >=70:
        df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'C']
      elif 70 > c >=60:
        df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'D']
      elif 60 > c :
        df.loc[len(df.index)] = [st_num,st_num_kor, st_num_eng, st_num_math,b,c,'F']
      
      print('학생 ({})의 점수 합계는 {}점, 평균은 {:.2f} 입니다.'.format(st_num,b ,c ))  
      
      df.index = df['번호']
      df =df.sort_index()
</code>
</pre>

*성적 현황 출력

<pre>
<code>
  elif num_menu == '2':
    df.index = df['번호']
    df = df.sort_index()
    print('-------------------------------------------------------------------------')
    print('{:<22}{:<6}{:<7}{:<6}{:<7}{:<7}{:<8}'.format('번호', '국어', '영어', '수학','총합', '평균','환산'))
    print('-------------------------------------------------------------------------')
    for in_dex in range(len(df.index)):
      for col in range(len(df.columns)):
        
        if col == 5 :
          a = ('{:.2f}'.format(df.iat[in_dex,col]))
          print('{:<10}'.format(a), end='')

        elif col == 6 :
          a = df.iat[in_dex,col]
          print('{:<8}'.format(a)  )
        elif col == 0:
          print('{:<20}      '.format(df.iat[in_dex,col]),end='')
        else:
          print('{:<9}'.format(df.iat[in_dex,col]),end='')
</code>
</pre>
            
* 성적 수정/ 삭제 학생 입력 후 정보확인
<pre>
<code>
 elif num_menu == '3':
    
    try:
   
      del_num = input('수정할 학생 번호 :') # 학번 입력받기
      del_num = int(del_num )       
   
    except ValueError   as e:  # 학번이 정수인지 확인 
      print('{}는  없습니다.'.format(del_num))
      continue
      
    else:
      
      if del_num <= 0: # 학번이 양수인지 확인 
        print('{}는 입력할 수 없습니다.'.format(del_num))
        continue
      elif del_num > 0:
        i = []
        for a in range(len(df.index)): # 학번이 중복인지 확인 
         p = df.index[a] 
         i.append(p)
     
        if del_num not in i : # 학번이 중복인지 확인 
            print('{}은(는)성적이 존재하지않는 학생입니다.'.format(del_num))
            continue   
    print('-------------------------------------------------------------------------')
    print('{:<22}{:<6}{:<6}{:<5}{:<6}{:<7}{:<8}'.format('번호', '국어', '영어', '수학','총합', '평균','환산'))
    print('-------------------------------------------------------------------------')
    df2 = df.loc[[del_num]]
    del_in = df2.index
    del_in = del_in[0]
    for col in range(len(df2.columns)):
      del_i = 0
      if col == 5 :
        a = ('{:.2f}'.format(df2.iat[del_i,col]))
        print('{:<10}'.format(a), end='')

      elif col == 6 :
        a = df2.iat[del_i,col]
        print('{:<8}'.format(a)  )
      elif col == 0:
        print('{:<20}      '.format(df2.iat[del_i,col]),end='')
      else:
        print('{:<8}'.format(df2.iat[del_i,col]),end='')    
    print('-------------------------------------------------------------------------')
</code>
</pre>
      
* 학생 일치 여부 및 수정/ 삭제 여부 
<pre>
<code>
y_or_n = input('위 정보가 맞습니까?(y/n):')
    if y_or_n == 'n':
      continue
    elif y_or_n == 'y':
      print('(1)수정  (2)삭제') 
      del_or_rep = input('>>>') 
</pre>
</code>

* 성적 삭제
<pre>
<code>
      if del_or_rep =='2':
        df = df.drop(del_in)#특정 열 삭제
        print('{}의 성적 기록이 삭제 되었습니다.'.format(del_num))
        df.index = df['번호']
        df = df.sort_index()
        continue
</pre>
</code>

*성적 수정시 수정 성적 입력
<pre>
<code>
      elif del_or_rep == '1':
      
        while True:
        
          try:
            st_num_kor = input('국어 (기존점수:{}) >'.format(df.at[del_in,'국어']))
            st_num_kor = int(st_num_kor)
          
          except ValueError as e:
            st_num_kor = df2.iat[0,1]
            break
          else:
            if st_num_kor <= 0:
              print('정수 0~100를 입력하시오a')
              
            elif st_num_kor > 100 :
              print('정수 0~100를 입력하시오a')

</code>
</pre>

* 수정 성적 저장 여부 확인 후 저장
<pre>
<code>

        yes_or_no = input('위 내용대로 수정 하시겠습니까? (y/n): ')
        if yes_or_no == 'n':
          continue
        elif yes_or_no == 'y':
          df3 = pd.Series([st_num_kor, st_num_eng, st_num_math])
          b = int(df3.sum())
          c = float(df3.mean())
          c = round(c,2)
          
          if c >=90:
            df.loc[del_in] = [del_num,st_num_kor, st_num_eng, st_num_math,b,c,'A']
            
          elif 90> c >=80:
            df.loc[del_in] = [del_num,st_num_kor, st_num_eng, st_num_math,b,c,'B']
            
          elif 80 > c >=70:
            df.loc[del_in] = [del_num,st_num_kor, st_num_eng, st_num_math,b,c,'C']
            
          elif 70 > c >=60:
            df.loc[del_in] = [del_num,st_num_kor, st_num_eng, st_num_math,b,c,'D']
            
          elif 60 > c :
            df.loc[del_in] = [del_num,st_num_kor, st_num_eng, st_num_math,b,c,'F']
          
          
          df.index = df['번호']  
          df = df.sort_index()
          continue        
</code>
</pre>

* 프로그램 종료, 파일저장
<pre>
<code>
  elif num_menu == '4':
    
    a=input('파일이름을 입력하시오:')
    df.to_csv('C:\kim\\{}.csv'.format(a), mode='w',index=False)
    
    with open ('num.txt', 'w',encoding= ' UTF-8') as f:
      f.write(a+"\n")


    break
</code>
</pre>
