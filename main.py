from dotenv import load_dotenv
import requests
import os
import re
import time

# 从环境变量中获取 API 密钥
load_dotenv()
api_key = os.getenv("API_KEY")


def request_capitalize_my_title(title_input):
    url = "https://capitalize-my-title.p.rapidapi.com/title/" + title_input
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "capitalize-my-title.p.rapidapi.com",
    }

    try:
        response = requests.get(url, headers=headers)
        title_output = response.json()["data"]["output"]
        return title_output
    except Exception as e:
        print("\033[1;31m" + "Error: " + str(e) + "\033[0m")
        return None


def add_braces(input_string):
    """splitting a string into words, checking if each word starts with a capital letter, and then wrapping those specific words with curly braces {}."""
    if not input_string:
        return None
    words = input_string.split()

    processed_words = []
    for word in words:
        if word[0].isupper():
            word = f"{{{word}}}"  # Wrap the word with curly braces
        processed_words.append(word)

    # Join the processed words back into a string
    output_string = " ".join(processed_words)
    return output_string


def process_bib_file(file_path):
    # 读取 bib 文件内容
    with open(file_path, "r") as file:
        bib_data = file.read()

    # 使用正则表达式提取标题部分
    pattern = r"\n\s*title\s*=\s*{(.*?)}[^}]*(?=\n\s*\S|\Z)"
    titles = re.findall(pattern, bib_data, re.DOTALL)

    # 处理并替换标题部分
    for title in titles:
        title = title.replace("{", "").replace("}", "")  # 去除原有的大括号
        print(f"Before: {title}")

        processed_title = add_braces(request_capitalize_my_title(title))
        if not processed_title:
            print("\n")
            continue

        print(f"After : {processed_title}\n")
        bib_data = bib_data.replace(title, processed_title)
        time.sleep(1)  # api 调用频率限制

    # 保存修改后的 bib 文件
    base_name, extension = os.path.splitext(file_path)
    new_file_name = base_name + "_new" + extension
    with open(new_file_name, "w") as file:
        file.write(bib_data)


if __name__ == "__main__":
    # title_input = "Analysis and observations from the first amazon picking challenge"
    # title_input = "A new technique for fully autonomous and efficient 3 d robotics hand/eye calibration"
    # request_capitalize_my_title(title_input)

    file_path = "refs.bib"
    process_bib_file(file_path)
