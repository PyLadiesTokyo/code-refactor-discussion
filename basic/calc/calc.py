""" 2つの値の足し算と引き算の結果を表示する. """


def calc(num1, num2):
    result_add = num1 + num2
    result_sub = num1 - num2

    return result_add, result_sub

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    # add, sub = calc(10, 5)
    num1 = 10
    num2 = 5
    #add_result, sub_result = add(num1, num2), sub(num1, num2)

    add_result = add(num1, num2)
    sub_result = sub(num1, num2)

    #add, sub = add(num1, num2), sub(num1, num2)
    #add(num1, num2)

    #print(f"{add=}")
    #print(f"{sub=}")
    print("add=%d" % add_result)
    print("sub=%d" % sub_result)

"""
1.
2値の足し算の結果を返す関数と引き算の結果を返す関数に分割しましょう

2.
分割した関数に合わせてテストを修正しましょう
"""
