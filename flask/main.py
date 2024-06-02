from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL 配置
app.config['MYSQL_DATABASE_HOST'] = 'mysql-db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ys1490.1225'
app.config['MYSQL_DATABASE_DB'] = 'tt1'

mysql = MySQL(app)

@app.route('/')
def index():
    # 在这里执行与数据库交互的代码
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")


import time
time.sleep(30)