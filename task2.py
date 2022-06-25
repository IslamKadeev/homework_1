def int32_to_ip(int32):
    bytes_list = []
    ip = ''

    for i in range (4):
        bytes_list.append(int32 & 255)
        int32 >>= 8

    bytes_list.reverse()
    for byte in bytes_list:
        ip += str(byte) + "."
        
    return ip[:-1]

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(32) == "0.0.0.32"
