from flask import Flask,render_template,request
from flaskext.mysql import MySQL
aplicacion=Flask(__name__)
mysql=MySQL()
aplicacion.config['MYSQL_DATABASE_HOST']= 'localhost'
aplicacion.config['MYSQL_DATABASE_PORT']=3306
aplicacion.config['MYSQL_DATABASE_USER']= 'root'
aplicacion.config['MYSQL_DATABASE_PASSWORD']= ''
aplicacion.config['MYSQL_DATABASE_DB']= 'prueba'

mysql.init_app(aplicacion)

conexion=mysql.connect()
cursor=conexion.cursor

@aplicacion.route('/')
def index():
    return render_template('/principal.html')
@aplicacion.route("/crg", methods=['POST'])
def crg():
 encontrar=request.form['busque']
 sql=f"call busqueda ('{encontrar}')"
 cursor.execute(sql)
 resultado=cursor.fetchall()
 conexion.commit()
 return render_template("principal.html", dato= resultado)






if __name__=='__main__':
    aplicacion.run(host="0.0.0.0",debug=True,port="8081" )