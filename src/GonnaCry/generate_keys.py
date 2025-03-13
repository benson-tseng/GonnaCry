import base64
from Crypto.Random import get_random_bytes

def generate_key(size, encode=False):  # `size` 更直覺
    content = get_random_bytes(size)  # 產生 `size` bytes 的隨機數
    
    if encode:
        return base64.b64encode(content)

    return content

if __name__ == "__main__":
    print(generate_key(32))  # 產生 32 Bytes（256-bit）的隨機金鑰
