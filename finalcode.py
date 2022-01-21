#at_home~ing~complete~realcomplete
import pandas as pd
import csv
import numpy as np

df = pd.DataFrame( columns=['번호','국어','영어','수학','총점','평균','환산'])

f = open('./num.txt', 'r')
      
while True:
    line = f.readline()
    
    if not line: 
          break    
    
    df= pd.read_csv('C:\kim\\{}.csv'.format(line.rstrip("\n")),encoding= ' UTF-8')

f.close()
df.index = df['번호']  
df = df.sort_index()
while True:
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
    #영어 입력
    while True:
  

      try:
        st_num_eng = str(input('{}의 영어 점수: '.format(st_num)))
        st_num_eng = int(st_num_eng)
      
      except ValueError as e:
        print('정수 0~100를 입력하시오')
        
      else:
        if st_num_eng <= 0:
          print('정수 0~100를 입력하시오')
          
        elif st_num_eng > 100 :
          print('정수 0~100를 입력하시오')

        else:
          break
    #수학 입력
    while True:
  

      try:
        st_num_math = str(input('{}의 수학 점수: '.format(st_num)))
        st_num_math = int(st_num_math)
      
      except ValueError as e:
        print('정수 0~100를 입력하시오')
        
      else:
        if st_num_math <= 0:
          print('정수 0~100를 입력하시오')
          
        elif st_num_math > 100 :
          print('정수 0~100를 입력하시오')

        else:
          break
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
    y_or_n = input('위 정보가 맞습니까?(y/n):')
    if y_or_n == 'n':
      continue
    elif y_or_n == 'y':
      print('(1)수정  (2)삭제') 
      del_or_rep = input('>>>') 
      if del_or_rep =='2':
        df = df.drop(del_in)#특정 열 삭제
        print('{}의 성적 기록이 삭제 되었습니다.'.format(del_num))
        df.index = df['번호']
        df = df.sort_index()
        continue
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

            else:
              break
        while True:
        
          try:
            st_num_eng = input('영어 (기존점수:{}) >'.format(df.at[del_in,'영어']))
            st_num_eng = int(st_num_eng)
          
          except ValueError as e:
            st_num_eng = df2.iat[0,2]
            break
          else:
            if st_num_eng <= 0:
              print('정수 0~100를 입력하시오')
              
            elif st_num_eng > 100 :
              print('정수 0~100를 입력하시오')

            else:
              break      
        while True:
        
          try:
            st_num_math = input('수학 (기존점수:{}) >'.format(df.at[del_in,'수학']))
            st_num_math = int(st_num_math)
          
          except ValueError as e:
            st_num_math = df2.iat[0,3]
            break
          else:
            if st_num_math <= 0:
              print('정수 0~100를 입력하시오')
              
            elif st_num_math > 100 :
              print('정수 0~100를 입력하시오')

            else:
              break
        print('---------------------------------')
        print("{}번 학생의 수정 점수는".format(del_num))
        print('국어 : {}점'.format(st_num_kor))
        print('영어 : {}점'.format(st_num_eng))
        print('수학 : {}점'.format(st_num_math))
        print('---------------------------------')
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
  elif num_menu == '4':
    
    a=input('파일이름을 입력하시오:')
    df.to_csv('C:\kim\\{}.csv'.format(a), mode='w',index=False)
    
    with open ('num.txt', 'w',encoding= ' UTF-8') as f:
      f.write(a+"\n")


    break
