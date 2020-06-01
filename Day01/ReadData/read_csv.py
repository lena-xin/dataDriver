# 导包
import csv
# 打开CSV


class ReadCsv():
    def read_csv(self):
        with open("../../DataPool/sjx.csv", "r", encoding="utf-8") as f:
            datas = csv.reader(f)
            # 新建空列表，把单行返回的列表添加成为一个列表
            lines = []
            for data in datas:
                lines.append(data)
            return lines
                # print(data)


if __name__ == '__main__':
    print(ReadCsv().read_csv())
