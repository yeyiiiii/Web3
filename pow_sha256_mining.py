"""
题目：实践 PoW（Proof of Work）

编写程序，用自己的昵称 + nonce，不断修改 nonce 进行 SHA256 Hash 运算：

1. 直到满足 4 个 0 开头的哈希值，打印：
   - 花费的时间
   - Hash 的内容
   - Hash 值

2. 再次运算直到满足 5 个 0 开头的哈希值，打印：
   - 花费的时间
   - Hash 的内容
   - Hash 值
"""

import hashlib
import time

nickname = "ye"  # 这里替换成你的昵称


def mine(prefix_zeros):
    target = "0" * prefix_zeros
    nonce = 0

    start_time = time.time()

    while True:
        message = nickname + str(nonce)

        hash_result = hashlib.sha256(message.encode()).hexdigest()

        if hash_result.startswith(target):
            end_time = time.time()

            print("满足条件:", prefix_zeros, "个0")
            print("Hash内容:", message)
            print("Hash值:", hash_result)
            print("nonce:", nonce)
            print("耗时:", round(end_time - start_time, 4), "秒")
            print("-------------------------")

            return

        nonce += 1


# 计算 4 个 0
mine(4)

# 计算 5 个 0
mine(5)
