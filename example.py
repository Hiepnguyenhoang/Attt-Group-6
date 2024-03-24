from mickey import *
import array

def main():
    key = array.array('B', [0x01, 0x02, 0x03, 0x04, 0x05])
    iv = array.array('B', [0x06, 0x07, 0x08, 0x09, 0x0A])
    data = b'{"message":"Hello IoT"}'  # Thay đổi tin nhắn thành "Hello IoT"

    print("Plaintext:", data.decode('utf-8', errors='replace'))
    print("Original:", data.hex())

    mickey = Mickey(key, len(key), iv, len(iv))
    ciphertext = mickey.encrypt(data)

    mickey2 = Mickey(key, len(key), iv, len(iv))
    plaintext_result = mickey2.decrypt(ciphertext)
    print("Decrypt Hex:", plaintext_result.hex())
    print("Decrypt Result:", plaintext_result.decode('utf-8', errors='replace'))

main()
