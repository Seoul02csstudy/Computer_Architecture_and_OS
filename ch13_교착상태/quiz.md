- 자원 할당 그래프란?
  
  - 교착 상태를 그래프로 표현한 것

- 교착 상태 발생 조건 4가지와 특징
  
  - 상호 배제, 점유와 대기, 비선점, 원형 대기
  - 특징 : 4가지가 필수조건이긴 하나, 4가지를 충족한다고 해서 무조건 교착 상태가 발생하는건 아님

- 교착 상태 해결 방법 3가지와 각각의 특징
  
  - 예방
    
    - 필수조건 4가지 중 하나를 제거
    
    - but 4가지 중 하나를 제거하는건 사실상 불가능하거나 매우 비효율
  
  - 회피
    
    - 교착 상태가 발생하지 않을 정도로만 조심히 자원을 할당하는 방식
    
    - 즉, 할당 후 안전순서열이 존재해야하는 경우에만 할당
  
  - 검출 후 회복
    
    - 교착 상태가 된 후에 회복
    
    - 선점을 통한 회복과 프로세스 강제 종료를 통한 회복 2가지 존재
    
    - 타조 알고리즘 : 그냥 발생빈도도 낮고, 심각성이 적어서 무시하는 경우


