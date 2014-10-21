from flask import *
from random import randint

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/test')
def test():
	return render_template('spark.html')

@app.route('/obstacleAvoidance')
@app.route('/obstacleAvoidance/<course>/<teamCode>',methods=['GET', 'POST'])
def Obstacle_Avoidance_Page(course, teamCode):
    entrance=["1","2","3"]; exits=["X","Y","Z"]
    gateTuple = entrance[randint(0,2)] +"," +  exits[randint(0,2)]
    return Response(json.dumps(gateTuple), mimetype='application/json')

if __name__ == '__main__':
	app.run(debug=True)
