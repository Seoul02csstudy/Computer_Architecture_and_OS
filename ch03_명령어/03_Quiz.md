- Python, C 의 차이점
  
  - 소스코드 전체가 저급언어로 변환되어 실행 -> C
  
  - 한 줄씩 저급언어로 변환하여 실행 -> Python
  
  - 단 두언어는 상대적일 뿐, C는 무조건 컴파일, Python은 무조건 인터프리터 언어가 아님

- 컴파일러와 인터프리터의 차이
  
  - 둘 다 고급언어를 저급언어로 변환하는 역할 
  
  - 단, 컴파일러의 경우 전체 코드를 보고 명령어를 수집 및 재구성
  
  - 인터프리터의 경우 각 행을 연속적으로 분석하며 실행
  
  - 이로인해 실행시간 컴파일러 > 인터프리터이다.
  
  - Java는 .java파일을 .class 파일로 자바 컴파일러가 컴파일하고 .class 파일을 기계어로 인터프리터가 변환함 ( java는 두 가지 특성을 가짐 (특이) )

- 유효주소 정의
  
  - 연산에 사용할 데이터가 저장된 위치
  
  - CPU는 유효주소를 통해서 메모리에 접근

- 주소지정방식
  
  - 직접주소 지정 방식
    
    - 유효주소가 주소란에 바로 들어가 있어 바로 접근 가능한 방식
    
        단점> 표현할 수 있는 유효주소에 제한이 있다.
  
  - 간접주소 지정 방식
    
    - 주소로 바로 접근하는게 아닌 주소를 따로 저장한 뒤에 저장된 주소를 통해서 유효주소 접근  

                   단점 > 직접주소지정방식보다 느림

* 큐, 스택의 정의 ****

**실제 N사, K사 cs관련 면접에서 나왔다 함**

----

1. 저급언어의 종류에는 (a)와 (b)가 있다.
   
   a: 기계어 b: 어셈블리어

2. 선입선출(가장 먼저 저장된 데이터를 빼내는 데이터 관리 방식)의 대표적인 명령어는 (a) 후입선출(나중에 저장한 데이터를 가장 먼저 빼내는 데이터관리방식)의 대표적 명령어는 (b)이다.
   
   a: 큐, b:스택
   
   