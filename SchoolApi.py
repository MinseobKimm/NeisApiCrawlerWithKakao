import requests
import json

class SchoolApi:

    params = {
        "KEY": "발급받은 key 값",
        "Type": "json",
    }

    schoolinfo = {}

    base_url = "https://open.neis.go.kr/hub/"

    def __init__(self, sub_url, params):
        self.sub_url = sub_url
        self.params = params

    def get_data(self):
        URL = SchoolApi.base_url + self.sub_url
        self.params.update(SchoolApi.params)
        self.params.update(SchoolApi.schoolinfo)
        response = requests.get(URL, params=self.params)

        try:
            j_response = json.loads(response.text)[self.sub_url]
            if j_response[0]["head"][0]["list_total_count"] == 1:
                return j_response[1]["row"][0]
            else:
                return j_response[1]["row"]
        except:
            print("찾는 데이터가 없습니다.")
            return response.text

    def get_school_info(self):
        data = self.get_data()

        SchoolApi.schoolinfo = {
            "ATPT_OFCDC_SC_CODE": data["ATPT_OFCDC_SC_CODE"],
            "SD_SCHUL_CODE": data["SD_SCHUL_CODE"]
        }


    def meal(self):
        data = self.get_data()
        try:
            string = "<조식>\n"+data[0]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
            string+= "<중식>\n"+data[1]["DDISH_NM"].replace("<br/>", "\n")+"\n\n"
            string += "<석식>\n" + data[2]["DDISH_NM"].replace("<br/>", "\n")
            characters = "1234567890./-*"
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            return string
        except:
            return "오늘은 급식이 없습니다."

    def time(self):
        data = self.get_data()
        string = ""
        try:
            for i in data:
                string += i["ITRT_CNTNT"] + "\n"
            return string
        except:
            return "오늘은 시간표가 없습니다."

    def schedule(self):
        data = self.get_data()
        try:
            return "오늘은 "+data["EVENT_NM"]+"이(가) 있습니다."
        except:
            return "x"