def decode_part(massage,start,end,key):
    part = massage[start:end]
    decoded_part = part[::key]
    return decoded_part

def decode_entire_msg(massage):
    decoded_massage = ""
    start = 1
    key = int(massage[0]) #因为每一次找到end之后，解码用的key 是start 时的数字，所以要现在外面define 第一轮的 start 和 key
    msg_len = 1 # 整个msg中元素的数量，用于让while loop停下，在总长度小于100的时候
    count = 0  # 字母的数量
    
    while count <= 100 and msg_len < len(massage):
        if massage[msg_len].isdigit():
            end = msg_len
            decode_msg = decode_part(massage,start,end,key)
            decoded_massage += decode_msg
            key = int(massage[msg_len])
            start = end + 1

        
        elif massage[msg_len].isalpha():
            count += 1
        msg_len += 1
    return decoded_massage 


def main():
    message = "3Gn.olwo pd/Q gh5l!d pulAk c_kosk an2 moPn! .y\oausr? 3mqei,sd+ktcbe.KrkcmOpsne!se odYpqo>kulq fag pozrtks dftpqh /ipaslk!dp4vm fkofwolp9 mjcnre"
    print(decode_entire_msg(message))
main()