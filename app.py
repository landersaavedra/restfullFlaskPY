from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('postgres+psycopg2://hmuquvcwtvhooz:fab1a7f746e2272549f88cba4489bca5a658a98aa2e5a18115bad9e41d235996@ec2-75-101-147-226.compute-1.amazonaws.com:5432/daq6954nni6dr') #La ruta depende de donde tengas almacenada la base de datos
conn = db_connect.connect()
print(db_connect)
app = Flask(__name__)
api = Api(app)

class tb_city(Resource):
    def get(self):
        conn = db_connect.connect() 
        query = conn.execute("SELECT * from ooz.tb_city")
        return {'City': [  i[3] for i in query.cursor.fetchall()]} 

class find_tb_city(Resource):
    def get(self, nidcity):
        conn = db_connect.connect() 
        query = conn.execute('SELECT * from ooz.tb_city where "NIDCITY" =%d ' % int(nidcity))
        result = {'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class tb_state(Resource):
    def get(self):
        conn = db_connect.connect() 
        query = conn.execute("SELECT * from ooz.tb_state")
        return {'State': [  i[1] for i in query.cursor.fetchall()]} 

api.add_resource(tb_city, '/city')
api.add_resource(find_tb_city, '/find_city/<nidcity>')
api.add_resource(tb_state, '/state')

if __name__ == '__main__':
     app.run(port='5000')