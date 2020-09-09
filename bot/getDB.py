import pymysql
import random
import os

passw = os.getenv("PASS")

connection = pymysql.connect( #data base connection
    host='b1qeampigy4khfapq7jn-mysql.services.clever-cloud.com',
    user='uxmwfsbetbqwifuq',
    password=passw,
    db='b1qeampigy4khfapq7jn'
)

cursor = connection.cursor()
print("Conexion establecida")

def getUniMeetings(): #get university meetings
    sql = "SELECT * FROM tbluniversidad" 
    try:
        cursor.execute(sql) #execute sql sentence
        clases = cursor.fetchall() #get all of results
        return clases
    except:
        pass

def insertIdea(idea, descIdea):
    id = str(random.choice(range(999))) #get a random id 
    sql = f"INSERT INTO tblideas VALUES ('{id}','{idea}', '{descIdea}')"
    try:
        cursor.execute(sql)
        connection.commit() #confirm changess
    except Exception as e:
        print(e)
    
def deleteIdea(id):
    sql = f"DELETE FROM tblideas WHERE idIdea = '{id}'"
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)


def getIdeas(id):
    if id is None: #there is not specific id
        sql = "SELECT * FROM tblideas"
        try:
            cursor.execute(sql)
            ideas = cursor.fetchall()
            return ideas
        except:
            pass
    else: #entered an id
        sql = f"SELECT * FROM tblideas WHERE idIdea = '{id}'"
        try:
            cursor.execute(sql)
            idea = cursor.fetchone() #get the only one result  
            return idea
        except:
            pass

def insertTask(task, descTask):
    id = str(random.choice(range(999)))
    sql = f"INSERT INTO tbltasks VALUES ('{id}','{task}', '{descTask}')"
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)
    
def deleteTask(id):
    sql = f"DELETE FROM tbltasks WHERE idTask = '{id}'"
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        pass


def getTasks(id):
    if id is None:
        sql = "SELECT * FROM tbltasks"
        try:
            cursor.execute(sql)
            tasks = cursor.fetchall()
            return tasks
        except:
            pass
    else:
        sql = f"SELECT * FROM tbltasks WHERE idTask = '{id}'"
        try:
            cursor.execute(sql)
            task = cursor.fetchone()             
            return task     
        except:
            pass




    