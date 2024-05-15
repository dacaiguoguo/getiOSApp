
import re

def extract_image(data, output_filename):
    # 正则表达式查找图片数据
    pattern = re.compile(rb'Content-Type: image/jpeg\r\n\r\n(.+?)\r\n--', re.DOTALL)
    match = pattern.search(data)
    if match:
        # 将二进制图片数据写入文件
        with open(output_filename, 'wb') as file:
            file.write(match.group(1))
    else:
        print("No image found")

req_path = "/Users/yanguosun/Developer/aistudy/recommend-prompt.txt"
# req_path = "/Users/yanguosun/Developer/aistudy/saved_request.txt"
# 用于把Charles抓到的post请求上传的图片 提取出来
# 读取保存的请求数据
with open(req_path, 'rb') as file:
    data = file.read()

# 调用函数，指定输出文件名
# extract_image(data, 'output_image.png')
extract_image(data, 'output_image2.jpg')