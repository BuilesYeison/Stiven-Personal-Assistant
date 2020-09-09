import pymysql
import random

connection = pymysql.connect( #data base connection
    host='localhost',
    user='root',
    password='',db='stivendb'
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
            for idea in ideas:
                print(idea, "\n")
        except:
            pass
    else: #entered an id
        sql = f"SELECT * FROM tblideas WHERE idIdea = '{id}'"
        try:
            cursor.execute(sql)
            idea = cursor.fetchone() #get the only one result  
            print(idea)       
        except:
            pass

def insertTask(task, taskIdea):
    id = str(random.choice(range(999)))
    sql = f"INSERT INTO tbltasks VALUES ('{id}','{task}', '{taskIdea}')"
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)
    
def deleteTask(id):
    sql = f"DELETE FROM tbltasks WHERE idIdea = '{id}'"
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)


def getTasks(id):
    if id is None:
        sql = "SELECT * FROM tbltasks"
        try:
            cursor.execute(sql)
            tasks = cursor.fetchall()
            for task in tasks:
                print(task, "\n")
        except:
            pass
    else:
        sql = f"SELECT * FROM tbltasks WHERE idTask = '{id}'"
        try:
            cursor.execute(sql)
            task = cursor.fetchone()  
            print(task)       
        except:
            pass

#insertTask("Comprar mercado", "donde el cuchito")
# try:
#     st = "tareas"
#     st= st.split("'")
#     print(len(st))
#     if len(st) == 1:
#         id= None
#     else:
#         id = st[1]
# except Exception as e:
#     print(e)


    



    