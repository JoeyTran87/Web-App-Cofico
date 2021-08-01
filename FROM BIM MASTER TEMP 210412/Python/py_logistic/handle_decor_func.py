import functools, time
from program_var import *

# def decor(func,more='More:'):
#     #----------------------------------------# bảo tồn tên Function lồng bên trong
#     @functools.wraps(func) 
#     def wrapper(*args,**kwargs):
#         print(f"{more}Something is happening before the function is called.")        
#         value = func(*args,**kwargs)
#         print(f"{more}Something is happening after the function is called.")
#         return value
#     return wrapper
# def normal_step(tips='Tips:'):
#     def decor(func):
#         #----------------------------------------# bảo tồn tên Function lồng bên trong
#         @functools.wraps(func) 
#         def wrapper(*args,**kwargs):
#             print(f"[{tips}] Some tips before do sometnig")        
#             value = func(*args,**kwargs)
#             print(f"[{tips}] Some next actions after done sometnig")
#             return value
#         return wrapper
#     return decor

def loop_flow(count = 4):
    def decor(func):
        #----------------------------------------# bảo tồn tên Function lồng bên trong
        @functools.wraps(func) 
        def wrapper(*args,**kwargs):
            value=None
            for i in range(count):   
                print(BREAKER_SEC)             
                value = func(*args,**kwargs)
                if value.lower() == 'q_':
                    print(f"\tBạn chọn [Thoát]\n{BREAKER_SEC}\n\tTiến trình đang thoát")
                    break
                elif value.lower() == ' z_':
                    print(f"\tBạn chọn [Tái khởi]\n{BREAKER_SEC}\n\tĐang tái khởi động tiến trình")
                elif value.lower() == 'fail':
                    print(f"\t[!] Tiến trình lỗi, bạn còn [{count-i-1}] lần thực hiện lại")
                    if count-i-1 == 0:
                        print(f"\tBạn đã hết [số lần] cho phép thực hiện Tiến trình\t{BREAKER_SEC}\n\tTiến trình đang thoát")
                else:
                    break
            return value
        return wrapper
    return decor



@loop_flow()
def doSomeThing(name):
    try:
        ask = input('Viết câu lệnh của bạn:\n >>>> :')
        print(f"\t{name} đang thực hiện [{ask}]")
        if ask == '0': # test Exception
            raise Exception('Bạn gặp lỗi')
        else:
            return ask
    except Exception as ex:
        print(f"[Exception] : {ex}")
        return "fail"


#Normal output
def clock(func):
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        # name = func.__name__
        name = fatorial_1.__name__
        arg_str = ','.join(repr(agr) for agr in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        time.sleep(1)
        return result
    return clocked


 # Progress bar output
def processor(func):
    a = []
    def clocked(arg):
        a.append(arg)
        t0 = time.perf_counter()
        result = func(arg)
        elapsed = time.perf_counter() - t0

        b = arg*'*'
        c = (a[0] - arg)*'.'
        # end='' First, don't wrap
        # \r Move to the beginning of the line, overwrite the output
        print('\r{:^1.2f}[{}->{}]{}'.format(elapsed, b, c, result), end='')
        time.sleep(1)
        return result
    return clocked

@clock
def fatorial_1(n):
    return 1 if n < 2 else n*fatorial_1(n-1)


@processor
def fatorial(n):
    time.sleep(0.1)
    return 1 if n < 2 else n*fatorial(n-1)



if __name__ == '__main__':
    # doSomeThing('Duy')
    # fatorial_1(6)
    fatorial(20)