"""
题目：实践非对称加密 RSA

1. 生成 RSA 公私钥对
2. 用昵称 + nonce 不断计算 SHA256
3. 找到满足 4 个 0 开头的 Hash
4. 用私钥对 “昵称+nonce” 签名
5. 用公钥验证签名
"""

import hashlib
import time

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


# -----------------------------
# 1 生成 RSA 公私钥
# -----------------------------
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

print("RSA 密钥对生成完成")
print("-----------------------------")


# -----------------------------
# 2 PoW 寻找 4 个 0
# -----------------------------
nickname = "ye"
nonce = 0
target = "0000"

start_time = time.time()

while True:

    message = nickname + str(nonce)

    hash_result = hashlib.sha256(message.encode()).hexdigest()

    if hash_result.startswith(target):
        break

    nonce += 1

end_time = time.time()

print("PoW 找到结果")
print("Hash内容:", message)
print("Hash值:", hash_result)
print("nonce:", nonce)
print("耗时:", round(end_time - start_time, 4), "秒")
print("-----------------------------")


# -----------------------------
# 3 私钥签名
# -----------------------------
signature = private_key.sign(
    message.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("签名生成成功")
print("Signature:", signature.hex()[:60], "...")
print("-----------------------------")


# -----------------------------
# 4 公钥验证
# -----------------------------
try:

    public_key.verify(
        signature,
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("验证成功：签名有效")

except:

    print("验证失败：签名无效")
