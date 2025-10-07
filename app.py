"""
Author: Ryan Zhang
Date: 2025-08-08 21:37:59
LastEditors: Ryan Zhang
Email: ryanzhang@bytesycn.com
LastEditTime: 2025-10-07 08:18:50
FilePath: \app.py
Repositories: https://github.com/hz157/cable-label
Description: 


Copyright (c) 2025 by Ryan Zhang, All Rights Reserved.
"""

from flask import Flask, render_template, request, send_file
from datetime import datetime
import pandas as pd
import os
import sys

# 创建 Flask 应用
app = Flask(__name__)

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {"xlsx", "xls"}


# 检查文件扩展名是否允许
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# 风格模板
style = [
    "{placeholder0}\tFr: {placeholder1}\tTo: {placeholder2}",
    "{placeholder0}\tFrom: {placeholder1}\tTo: {placeholder2}",
    "{placeholder0}\t本端: {placeholder1}\t对端: {placeholder2}",
    "Act: {placeholder0}\tFr: {placeholder1}\tTo: {placeholder2}",
    "Act: {placeholder0}\tFrom: {placeholder1}\tTo: {placeholder2}",
    "用途: {placeholder0}\t本端: {placeholder1}\t对端: {placeholder2}",
    "Act: {placeholder0}\nFr: {placeholder1}\nTo: {placeholder2}",
    "Act: {placeholder0}\nFrom: {placeholder1}\nTo: {placeholder2}",
    "用途: {placeholder0}\n本端: {placeholder1}\n对端: {placeholder2}",
]


# 主页面路由，提供上传界面
@app.route("/")
def index():
    # 将 style_list 和它的索引一并传递到模板
    styles_with_index = [(i + 1, style) for i, style in enumerate(style)]
    return render_template("index.html", style_list=styles_with_index)


# 模板文件路径（假设已经有一个模板文件 template.xlsx）
TEMPLATE_PATH = os.path.join(os.getcwd(), "templates", "template.xlsx")


@app.route("/download-template")
def download_template():
    # 提供模板文件下载
    return send_file(TEMPLATE_PATH, as_attachment=True)


# 上传文件并处理
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"
    file = request.files["file"]
    selected_style_index = int(request.form["style_index"]) - 1

    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join("uploads", filename)
        file.save(filepath)

        # 读取 Excel 文件
        df = pd.read_excel(filepath)

        # 存储 label_content 的列表
        label_contents = []

        # 循环处理每一行数据
        for index, row in df.iterrows():
            name_value = row["Name"]
            from_value = row["From"]
            to_value = row["To"]
            if selected_style_index <= 5:
                label_content_1 = style[selected_style_index].format(
                    placeholder0="", placeholder1=from_value, placeholder2=to_value
                )
                label_content_2 = style[selected_style_index].format(
                    placeholder0="", placeholder1=to_value, placeholder2=from_value
                )
                label_contents.append(label_content_1)
                label_contents.append(label_content_2)
            else:
                label_content_1 = style[selected_style_index].format(
                    placeholder0=name_value,
                    placeholder1=from_value,
                    placeholder2=to_value,
                )
                label_content_2 = style[selected_style_index].format(
                    placeholder0=name_value,
                    placeholder1=to_value,
                    placeholder2=from_value,
                )
                label_contents.append(label_content_1)
                label_contents.append(label_content_2)

        # 保存输出文件
        new_df = pd.DataFrame({"label_content": label_contents})
        output_filename = f'{datetime.now().strftime("%Y-%m-%d-%H_%M_%S")}.xlsx'
        output_filepath = os.path.join("uploads", output_filename)
        new_df.to_excel(output_filepath, index=False)

        # 返回生成的文件
        return send_file(output_filepath, as_attachment=True)

    return "Invalid file or style index"


# 启动应用
if __name__ == "__main__":
    # 确保上传文件夹存在
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True, port=5000, host='0.0.0.0')
