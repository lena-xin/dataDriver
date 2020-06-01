
class SJX():
    def judge_sjx(slef, a, b, c):
        # 判断是否为三角形
        if a+b > c and a+c > b and b+c > a:
            if a == b and b == c:
                res = "等边三角形"
            elif a == b or b == c or a == c:
                res = "等腰三角形"
            else:
                res = "普通三角形"
        else:
            res = "不是三角形"
        return res


if __name__ == '__main__':

    a = input("请输入第一条边:")
    b = input("请输入第二条边:")
    c = input("请输入第三条边:")

    SJX().judge_sjx(int(a), int(b), int(c))
