#导入unittest、三角形、csv读取参数类
import unittest
from Day01.Code.sjx import SJX
from Day01.ReadData.read_csv import ReadCsv

# 实例化三角形
sjxClass = SJX()
# 实例化读取CSV工具
readCsvClass = ReadCsv()


class TestCsv(unittest.TestCase):
    # 测试三角形函数程序
    def test001(self):
        for i in range(len(readCsvClass.read_csv())):
            result = sjxClass.judge_sjx(int(readCsvClass.read_csv()[i][0]),
                                        int(readCsvClass.read_csv()[i][1]),
                                        int(readCsvClass.read_csv()[i][2]))
    #       断言，三角形运行结果与预期结构进行对比
            self.assertEqual(result, readCsvClass.read_csv()[i][3])
            print(readCsvClass.read_csv()[i][0],
                  readCsvClass.read_csv()[i][1],
                  readCsvClass.read_csv()[i][2],
                  readCsvClass.read_csv()[i][3],
                  "验证通过")


if __name__ == '__main__':
    unittest.main()
