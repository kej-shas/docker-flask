# 使用官方 MySQL 镜像
FROM mysql

# 设置 MySQL root 用户密码
ENV MYSQL_ROOT_PASSWORD=ys1490.1225

# 将数据库文件复制到容器中
COPY my_database.sql /docker-entrypoint-initdb.d/


# 暴露 MySQL 端口
EXPOSE 3306
