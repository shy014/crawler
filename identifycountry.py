import csv
import phonenumbers
from phonenumbers import geocoder

def get_country_from_phone_number(phone_number):
    try:
        number = phonenumbers.parse(phone_number)
        country_code = phonenumbers.region_code_for_number(number)
        country_name = geocoder.description_for_number(number, "en")
        return country_code, country_name
    except phonenumbers.phonenumberutil.NumberParseException:
        return None, None

# 从输入文件读取电话号码，并识别归属地
input_file = "input.txt"  # 输入文件名，每行一个电话号码
output_file = "output.csv"  # 输出文件名，保存识别结果

with open(input_file, "r") as file:
    phone_numbers = file.readlines()

results = []
for phone_number in phone_numbers:
    phone_number = phone_number.strip()
    phone_number = "+" + phone_number
    country_code, country_name = get_country_from_phone_number(phone_number)
    if country_code and country_name:
        result = [phone_number, f"{country_name} ({country_code})"]
    else:
        result = [phone_number, "Failed to identify the country"]
    results.append(result)

# 将识别结果写入CSV文件
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Phone Number", "Country"])
    writer.writerows(results)

print("识别结果已保存到文件:", output_file)
