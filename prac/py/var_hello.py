from collections import namedtuple


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