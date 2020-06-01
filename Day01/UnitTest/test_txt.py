# 导入测试包
import unittest
from Day01.ReadData.read_txt import ReadTxt
from Day01.Code.sjx import SJX

sjxClass = SJX()
readTxtClass = ReadTxt()


class TestTxt(unittest.TestCase):
    def test_txt(self):
        for i in range(len(readTxtClass.read_txt())):
            print(readTxtClass.read_txt())
            result = sjxClass.judge_sjx(int(readTxtClass.read_txt()[i][0]),
                                        int(readTxtClass.read_txt()[i][1]),
                                        int(readTxtClass.read_txt()[i][2]))

            # 断言，判断是否预期结果
            self.assertEqual(result, readTxtClass.read_txt()[i][3])
            print(readTxtClass.read_txt()[i][0],
                  readTxtClass.read_txt()[i][1],
                  readTxtClass.read_txt()[i][2],
                  readTxtClass.read_txt()[i][3], "通过验证")


if __name__ == '__main__':
    unittest.main()
