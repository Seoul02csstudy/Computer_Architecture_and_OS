'''
상호 배제를 위한 동기화 ex
계좌에는 10만원 저축
프로세스 A : 저축된 금액에 2만원 넣는 process
프로세스 B : 저축된 금액에 5만원 넣는 process
'''
# 동기화가 제대로 이루어지지 않은 경우
money = 10
processA = 2
processB = 5
# process A와 process B가 동시에 실행되었다고 하면
# 1. process A,B에서 잔액을 읽는다.
moneyA = money
moneyB = money
print(moneyA)       # 10
print(moneyB)       # 10
# 2. 읽어들인 값에서 2만원 더한다.
moneyA += processA
print(moneyA)       # 12
# 2. 읽어들인 값에서 5만원 더한다.
moneyB += processB
print(moneyB)       # 15

money = moneyA # money 는 moneyA가 된다.
print(money)        # 12
money = moneyB
print(money)        # 15

# 동기화가 이루어진 경우
money = 10
processA = 2
processB = 5
# process A와 process B가 동시에 실행되었다고 하면
# 1. process A에서 먼저 잔액을 읽는다.
moneyA = money
print(moneyA)       # 10
# 2. 읽어들인 값에서 2만원 더한다.
moneyA += processA
print(moneyA)       # 12
# 3. money에 더한 값을 저장한다.
money = moneyA      # 12
# 4. processB에서 잔액을 읽는다.
moneyB = money      # 12

# 5. 읽어들인 값에서 5만원 더한다.
moneyB += processB
print(moneyB)       # 15

# 6. money에 값을 업데이트한다.
money = moneyB
print(money)        # 17