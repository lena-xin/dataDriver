# 导包 json
import json
from Day01.Code.sjx import SJX

class ReadJson():
    def read_json(self):
        # 打开文件流
        with open("../../DataPool/sjx.json", "r", encoding="utf-8") as f:
            datas = json.load(f)
            result = datas["bian"]
        # print(result)
        return result


if __name__ == '__main__':
    print(ReadJson().read_json())
