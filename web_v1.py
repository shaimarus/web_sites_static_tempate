from flask import Flask, Response, render_template, stream_with_context,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy

#from flask_track_usage import TrackUsage
#from flask_track_usage.storage.sql import SQLStorage


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@db-pg:5432/postgres'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#print('test')
#sql_db=SQLAlchemy(app)


#print('11111111')
#print(sql_db)



#pstore=SQLStorage(db=sql_db)
#t=TrackUsage(app,[pstore])

@app.route("/")
def index():

    import psycopg2
    from time import gmtime, strftime

    conn = psycopg2.connect('postgresql://postgres:postgres@db-pg:5432/postgres')

    cur = conn.cursor()


    cur.execute('INSERT INTO logs (ip, time1, day1)'
                'VALUES (%s, %s, %s)',
                (request.remote_addr,
                strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                strftime("%Y-%m-%d", gmtime()))
                )


    conn.commit()

    cur.close()
    conn.close()


    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5011,debug=True,threaded=True)

    