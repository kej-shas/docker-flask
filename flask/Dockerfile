# 使用官方 Python 镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 复制应用代码和依赖文件到容器中
COPY . /app

# 安装依赖
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 暴露 Flask 端口
EXPOSE 5000

# 启动应用
CMD ["python", "main.py"]
