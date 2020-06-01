# 导测试包 unittest
import unittest
from Day01.Code.sjx import SJX
from Day01.ReadData.read_json import ReadJson


sjxClass = SJX()
readJsonClass = ReadJson()


class TestJson(unittest.TestCase):
    def test_json(self):
        for i in range(len(readJsonClass.read_json())):
            result = sjxClass.judge_sjx(int(readJsonClass.read_json()[i]["b1"]),
                                        int(readJsonClass.read_json()[i]["b2"]),
                                        int(readJsonClass.read_json()[i]["b3"])
                                        )

            # 断言判断结果
            self.assertEqual(result, readJsonClass.read_json()[i]["expect"])
            print(readJsonClass.read_json()[i]["b1"],
                  readJsonClass.read_json()[i]["b2"],
                  readJsonClass.read_json()[i]["b3"],
                  readJsonClass.read_json()[i]["expect"], "----> 验证通过")


if __name__ == '__main__':
    unittest.main()
