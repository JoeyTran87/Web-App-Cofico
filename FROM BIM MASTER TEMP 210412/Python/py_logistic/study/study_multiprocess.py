
import multiprocessing
import time



def dosomething():
    print('Sleeping 1s')
    time.sleep(1)
    print('Done Sleeping')

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target = dosomething)
    p2 = multiprocessing.Process(target = dosomething)
    p1.start() # BẮT ĐẦU CÁC TIỀN TRÌNH ĐA LUỒNG
    p2.start()
    p1.join() # CHỜ CHO ĐẾN KHI CÁC TIẾN TRÌNH CON TẮT HẾT
    p2.join()
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start,2)} second(s)")




"""
RuntimeError:
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.
"""