from collections import namedtuple
from typing import List, Dict


def main():
    print("hello", end="")
    print(" python")

if __name__ == "__main__":
    main()
    my_list = ["frank", "handsome", "575"]
    # 匿名便亮 _
    for _, e in enumerate(my_list):
        print(e)

    # 元祖 不可改
    sex_tuple = ("male", "female")
    # namedtuple 元祖增強

# 3.5 後有類型申明功能，僅提示，不會影響運行
age: int = 12
name: str = "frank"
sex: bool = True
weight: float = 75
x: bytes = b"test"
courses: list =['django', 'scrapy', 'tornado']
courses2: List[str] = ['django', 'scrapy', 'tornado']

user_info:Dict[str, float] = {"frank": 18}