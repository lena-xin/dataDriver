# 打开文件
class ReadTxt():
    def read_txt(self):
        with open("../../DataPool/sjx.txt", "r", encoding="utf-8") as f:
            '''
            读取文本数据的方式：
            read()  按字节读，需要指定大小
            readline() 按行读取
            readlines() 读取所有行
            '''
            datas = f.readlines()  # 读取的数据含有'\n' ,需要去除换行符
            lines = []
            for data in datas:
                '''
                strip() 用于去除换行
                split() 用于按照指定分割字符分割字符串
                '''
                lines.append(data.strip().split(' '))

        return lines

# if __name__ == '__main__':
