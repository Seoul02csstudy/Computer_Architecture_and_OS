import threading
import time


class ThreadPool(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def acquire(self, name):
        with self.lock:
            self.active.append(name)
            print('탈의실 입장: {} | 현 탈의실 인원 {}'.format(name, self.active))

    def release(self, name):
        with self.lock:
            self.active.remove(name)
            print('탈의실 퇴장: {} | 현 탈의실 인원 {}'.format(name, self.active))


def worker(semaphore, pool):
    with semaphore:
        name = threading.currentThread().getName()
        pool.acquire(name) # wait 함수
        time.sleep(1)
        pool.release(name)  # signal 함수


if __name__ == '__main__':
    threads = []
    pool = ThreadPool()
    semaphore = threading.Semaphore(3) # 현재 탈의실 제한 3개 (전역변수 S)
    for i in range(10):
        t = threading.Thread(
            target=worker, name='손님 ' + str(i), args=(semaphore, pool))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()