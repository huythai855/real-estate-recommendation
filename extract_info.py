import os

import requests


# api_key = os.getenv("API_KEY")

api_key = "GOOGLE API KEY"

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

input = """
anh Thái đang muốn tìm căn nhà mặt đất cho gia đình ở Cổ Nhuế 1, Bắc Từ Liêm, Hà Nội gồm hai vợ chồng, diện tích tối thiểu 90m, gồm 1 phòng khách, phòng ngủ của 2 vợ chồng và 1 bếp
"""


data = {
    "contents": [
        {
            "parts": [
                {
                    "text": """
                        Bạn là một trợ lý của một chuyên viên kinh doanh bất động sản, từ thông tin trao đổi với người dùng, hãy trích xuất các thông tin đã có theo các trường thông tin dưới đây và trả lại kết quả dạng json, nếu trường thông tin nào không trích xuất được hãy để trống trong kết quả:
                            - Loại hình: Nhà mặt đất, chung cư, căn hộ dịch vụ
                            - Giá: …. (đơn vị VND)
                            - Diện tích: …… (đơn vị m2)
                            - Mặt tiền: …. (đơn vị m)
                            - Số phòng khách:
                            - Số phòng ngủ:
                            - Số phòng tắm:
                            - Khu vực:
                                - Phường:
                                - Quận:
                                - Thành Phố:
                        
                        Ví dụ: “Chị Liên đang muốn tìm căn chung cư cho gia đình gồm 4 người, diện tích tối thiểu 90m, gồm 1 phòng khách, phòng ngủ của 2 vợ chồng và phòng ngủ của 2 con, khu vực Khương Đình, Thanh Xuân, Hà Nội”
                        
                        Kết quả trả về:
                        {
                          "loại hình": "chung cư",
                          "giá": "4000000000",
                          "diện tích": "90",
                          "mặt tiền": "",
                          "số phòng khách": 1,
                          "số phòng ngủ": 2,
                          "số phòng tắm": "",
                          "khu vực": {
                            "phường": "Khương Đình",
                            "quận": "Thanh Xuân",
                            "thành phố": "Hà Nội"
                          }
                        }
                        
                        Giờ hãy thực hiện yêu cầu cho input:
                    """ + input
                }
            ]
        }
    ]
}


headers = {
    "Content-Type": "application/json"
}


response = requests.post(url, json=data, headers=headers)

text = response.json()['candidates'][0]['content']['parts'][0]['text']

print(text)

# if response.status_code == 200:
#     print("Success:", response.json())
# else:
#     print(f"Error {response.status_code}:", response.text)
