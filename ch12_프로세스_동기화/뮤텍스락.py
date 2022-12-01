from threading import Thread, Lock
import threading
'''
탈의실 예시
탈의실은 자물쇠가 걸려있으면 사용자가 있는 것을 인식하고 대기한다.
이러한 자물쇠 기능을 코드로 구현한 것이 뮤텍스 락
'''
# mutex를 사용할 때
def worker(mutex, data, thread_safe):
    if thread_safe:
        mutex.acquire() # 임계 구역 잠그는 역할
        # 만약 임계 구역이 잠겨있다면
        # 임계 구역이 잠겨있는지 반복적으로 확인
        # 임계 구역이 잠겨있지 않다면 임계 구역 잠금
    try:
        print('손님 {} : {}번째입장\n'.format(threading.get_ident(), data))
    finally:
        if thread_safe:
            mutex.release() # 임계 구역 잠금 해제
            # 임계 구역 작업이 끝나면 잠금 해제

if __name__ == '__main__':
    threads = []
    thread_safe = True
    mutex = Lock()
    for i in range(20):
        t = Thread(target=worker, args=(mutex, i, thread_safe))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

