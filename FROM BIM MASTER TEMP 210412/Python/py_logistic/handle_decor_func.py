import functools, time
# from handle_cmd import spin_three_dots
from program_var import *

def heading_wrap(func):
    def wrapper (*args,**kwargs):
        print(BREAKER)
        func(*args,**kwargs)
        print(BREAKER)
    return wrapper

def slow_down(func):
    def wrapper (*args,**kwargs):
        time.sleep(0.5)
        func(*args,**kwargs)
        time.sleep(0.5)
    return wrapper

def loop_flow(func):
    """Dành cho Function return Single ouput"""
    #----------------------------------------# bảo tồn tên Function lồng bên trong
    @functools.wraps(func) 
    def wrapper(*args,**kwargs):
        time.sleep(0.5)
        value=None
        try:
            print(BREAKER_SEC)             
            value = func(*args,**kwargs)
            if value.lower() == 'qq'or value.lower() == 'zz'or value.lower() == 'q_'or value.lower() == 'z_' or value.lower() == 'fail':
                raise Exception('Mã lệnh vòng lặp')
            elif value.split(':')[-1].lower() == 'y':
                    return True
            elif value.split(':')[-1].lower() == 'n':
                return False
            else:
                return value
        except Exception as ex:
            if ex.args[0] == 'Mã lệnh vòng lặp':
                value = f'Interrupter:{value}'
                return value
            else:
                return None
        
    return wrapper

def loop_flow_1(count = 4):
    """Dành cho Function return Multi Output"""
    def decor(func):
        #----------------------------------------# bảo tồn tên Function lồng bên trong
        @functools.wraps(func) 
        def wrapper(*args,**kwargs):
            value=None
            for i in range(count):   
                print(BREAKER_SEC)             
                value = func(*args,**kwargs)[1]
                if value.lower() == 'qq':
                    return '0##'
                elif value.lower() == 'zz':
                    return '0###'
                elif value.lower() == 'q_'or value.lower() == ' z_' or value.lower() == 'fail':
                    print(f"\t[!] Tiến trình đang [Reset] hoặc [Gặp lỗi]\n\tBạn còn [{count-i-1}] lần thực hiện lại")
                    return '0#'
                elif value.lower() == 'y':
                    return True                
                elif value.lower() == 'n':
                    return False
                else:
                    break
            return value
        return wrapper
    return decor



@loop_flow
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


def decor_ask_boolean(func):
    def wrapper(*args,**kwargs):
        value = None
        while True:
            value = func(*args,**kwargs).lower()
            if value == 'y':
                value = True
                break
            elif value == 'n': 
                value = False
                break
        return value

    return wrapper










if __name__ == '__main__':
    # doSomeThing('Duy')
    # fatorial_1(6)
    fatorial(20)