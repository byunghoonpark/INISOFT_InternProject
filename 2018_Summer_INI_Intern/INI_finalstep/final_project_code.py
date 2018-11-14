from pathlib import Path
import os
import redis
import shutil
import pymysql
from sshtunnel import SSHTunnelForwarder
import mysql.connector
import sshtunnel
import json
import requests
import asyncio 
import os.path

conn = pymysql.connect(host='192.168.10.37',user='root',password='ini6223',db='redis_project',charset='utf8')
curs = conn.cursor()

sql = "select path from level"
curs.execute(sql)

rows = curs.fetchall()
path1 = str(rows[0])
path2 = str(rows[1])
path3 = str(rows[2])

bronzepath = path1[2:-3]
goldpath = path2[2:-3]
silverpath = path3[2:-3]


redis_db = redis.StrictRedis(host='192.168.10.37', port=6379, db=1)

async def redis_func():
    i=1
    NoneType = type(None)
    while True : 

        if type(redis_db.get(i)) == NoneType :
            i = 1
            print('You go fist')
            continue

        else : 
            input_redis = redis_db.get(i).decode('utf-8')
            json_input_redis = json.loads(input_redis)
            if not json_input_redis["status"]=='update' and json_input_redis["worker_id"]==None:
                print( json_input_redis["cid"] + "s' status is not update and worker_id is not null" )
                i = i + 1
                continue

            else :
                json_input_redis['worker_id']='working'
                json_input_redis = json.dumps(json_input_redis)
                redis_db.set(i,json_input_redis)
                
                input_redis = redis_db.get(i).decode('utf-8')
                json_input_redis = json.loads(input_redis)

                cid = json_input_redis["cid"]
                count = json_input_redis["count"]
                status = json_input_redis["status"]
                db_level = json_input_redis["db_level"]
                target = json_input_redis["target"]
                filename = json_input_redis["filename"]
                print(cid)
  
                if db_level == 'bronze' and target == 'bronze':
                    if not os.path.isfile ( bronzepath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        print("you don't have to move the file, but status is done ")

                elif db_level=='bronze' and target=='silver':
                    if not os.path.isfile ( bronzepath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        if os.path.isfile( silverpath + filename ): 
                            print("Change file name, already exists")
                            json_input_redis['worker_id']=None
                            json_input_redis = json.dumps(json_input_redis)
                            redis_db.set(i,json_input_redis)
                            i = i+1                
                            continue
                        else :
                            shutil.move( bronzepath + filename , silverpath + filename)
                            print(filename + ' moves ' +  db_level +' to ' + target)

                elif db_level=='bronze' and target=='gold':
                    if not os.path.isfile ( bronzepath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        if os.path.isfile( goldpath + filename ): 
                            print("Change file name, already exists")
                            json_input_redis['worker_id']=None
                            json_input_redis = json.dumps(json_input_redis)
                            redis_db.set(i,json_input_redis)
                            i = i+1
                            continue 
                        else :
                            shutil.move( bronzepath + filename , goldpath + filename)
                            print(filename + ' moves ' +  db_level +' to ' + target)


                elif db_level=='silver' and target=='bronze':
                    if not os.path.isfile (silverpath + filename):
                        print( filename + ' not exists' )
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        if os.path.isfile( bronzepath + filename ): 
                            print("Change file name, already exists")
                            json_input_redis['worker_id']=None
                            json_input_redis = json.dumps(json_input_redis)
                            redis_db.set(i,json_input_redis)
                            i = i+1
                            continue
                        else :
                            shutil.move( silverpath + filename , bronzepath + filename)
                            print(filename + ' moves ' +  db_level +' to ' + target)

                elif db_level == 'silver' and target == 'silver':
                    if not os.path.isfile ( silverpath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        print("you don't have to move the file, but status is done ")


                elif db_level=='silver' and target=='gold':
                    if not os.path.isfile ( silverpath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        if os.path.isfile( goldpath + filename ): 
                            print("Change file name, already exists")
                            json_input_redis['worker_id']=None
                            json_input_redis = json.dumps(json_input_redis)
                            redis_db.set(i,json_input_redis)
                            i = i+1
                            continue
                        else :
                            shutil.move( silverpath + filename , goldpath + filename)
                            print(filename + ' moves ' +  db_level +' to ' + target)

                elif db_level=='gold' and target=='bronze':
                    if not os.path.isfile ( goldpath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        if os.path.isfile( bronzepath + filename ): 
                            print("Change file name, already exists")
                            json_input_redis['worker_id']=None
                            json_input_redis = json.dumps(json_input_redis)
                            redis_db.set(i,json_input_redis)
                            i = i+1
                            continue
                        else :
                            shutil.move( goldpath + filename , bronzepath + filename)
                            print(filename + ' moves ' +  db_level +' to ' + target)
                        

                elif db_level=='gold' and target=='silver':
                    if not os.path.isfile ( goldpath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        if os.path.isfile( silverpath + filename ): 
                            print("Change file name, already exists")
                            json_input_redis['worker_id']=None
                            json_input_redis = json.dumps(json_input_redis)
                            redis_db.set(i,json_input_redis)
                            i = i+1
                            continue
                        else :
                            shutil.move( goldpath + filename , silverpath + filename)
                            print(filename + ' moves ' +  db_level +' to ' + target)
                     

                else : 
                    if not os.path.isfile ( goldpath + filename ): 
                        print( filename + ' not exists')
                        json_input_redis['worker_id']=None
                        json_input_redis = json.dumps(json_input_redis)
                        redis_db.set(i,json_input_redis)
                        i=i+1
                        continue

                    else:
                        print("you don't have to move the file ")


                json_input_redis['status']='done'
                json_input_redis['worker_id']=None
                json_input_redis = json.dumps(json_input_redis)
                redis_db.set(i,json_input_redis)
                i=i+1
                await asyncio.sleep(10.0)                

                r = requests.post('http://192.168.10.108:5000/update_sentence', data = {'cid': cid})  
             

loop = asyncio.get_event_loop()
loop.run_until_complete(redis_func())
loop.close()
