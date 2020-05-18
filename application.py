import sys
import json
import os
from flask import jsonify
from flask import send_from_directory
from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/')
def static_proxy():
    return send_from_directory('./static', 'index.html')

@app.route('/static/data/users.json', methods=['GET', 'POST']) 
def getUsersJson():
    file = open("static/data/users.json", "r")
    usersjson = json.load(file)
    file.close()
    return jsonify(json.dumps(usersjson))

@app.route('/static/cgi-bin/updateusers.py', methods=['GET', 'POST']) 
def updateusers():
    input = request.get_json(force = True)
    logfile = open("log.txt","w")
    
    if input is None:
        input = {}
        logfile.write("None")      
        
    file = open("static/data/users.json", "w")
    file.write(json.dumps(input))
    logfile.close()
    file.close()
    return jsonify("{}")

@app.route('/static/cgi-bin/savetofile.py', methods=['GET', 'POST']) 
def savetofile():
    logfile = open("log.txt","w")
    input = request.get_json(force = True)
    
    if input is None:
        input = {}
        logfile.write("None")      
        
    else:
        print(input)
        userid = input['userid']
        filename = input['filename']
        answers = input['answers']
        
        if (filename.find('Linegraphs') != -1):
            logfile.write('Linegraphs\n')
            file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
            file.write(json.dumps({'answers':answers, 'duration':input['duration']})) 
        elif (filename.find('Barchart') != -1):
            logfile.write('Barchart\n')
            file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
            file.write(json.dumps({'answers':answers, 'duration':input['duration']})) 
        elif (filename.find('Scatter') != -1):
            logfile.write('Scatter\n')
            file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
            file.write(json.dumps({'answers':answers, 'duration':input['duration']})) 
        elif (filename.find('Pie') != -1):
            logfile.write('Pie\n')
            file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
            file.write(json.dumps({'answers':answers, 'duration':input['duration']})) 
        elif (filename.find('Network') != -1):
            logfile.write('Network\n')
            file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
            file.write(json.dumps({'answers':answers, 'duration':input['duration']}))
        elif (filename.find('main_') != -1):
            logfile.write(str(filename)+' main_'+str(userid)+'\n')
            file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
            file.write(json.dumps({'answers':answers, 'duration':input['duration'],'start_time':input['start_time']}))
            
        if (filename.find('tute') != -1):
            thefilename = 'static//users//'+str(userid)+'//tutorial.json'
            if (os.path.isfile(thefilename)): 
                file = open(thefilename,'r')
                existing = json.load(file)
                logfile.write(json.dumps(existing['slide'][0]))
                existing['slide'].append({'number':input['slidenum'], 'duration':input['duration']})
                file.close()
                file = open(thefilename,'w')
                file.write(json.dumps(existing))
            else:
                file = open(thefilename,'w')
                file.write(json.dumps({'slide':[{'number':input['slidenum'], 'duration':input['duration']}]}))            
        elif (filename.find('userratingsurvey') != -1):
            reason = input['reason']
            if (os.path.isfile('static//users//'+str(userid)+'//userratingsurvey.json')): 
                file = open('static//users//'+str(userid)+'//userratingsurvey.json','r')
                existing = json.load(file)
                if filename in existing:
                    existing[filename].append({'answers':answers, 'reason': reason, 'duration':input['duration']})
                else:
                    existing[filename] = [{'answers':answers, 'reason': reason, 'duration':input['duration']}]
                file.close()
                file = open('static//users//'+str(userid)+'//userratingsurvey.json','w')
                file.write(json.dumps(existing))
            else:
                file = open('static//users//'+str(userid)+'//userratingsurvey.json','w')
                file.write(json.dumps({filename:[{'answers':answers, 'reason': reason, 'duration':input['duration']}]}))        
        elif (filename.find('readabilitysurvey') != -1):            
            if (os.path.isfile('static//users//'+str(userid)+'//'+filename+'.json')): 
                file = open('static//users//'+str(userid)+'//'+filename+'.json','r')
                existing = json.load(file)
                if filename in existing:
                    existing[filename].append({'answers':answers, 'duration':input['duration']})
                else:
                    existing[filename] = [{'answers':answers, 'duration':input['duration']}]
                file.close()
                file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
                file.write(json.dumps(existing))
            else:
                file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
                file.write(json.dumps({filename:[{'answers':answers, 'duration':input['duration']}]}))        
        elif (filename.find('treadability') != -1):
            if (os.path.isfile('static//users//'+str(userid)+'//training.json')): 
                file = open('static//users//'+str(userid)+'//training.json','r')
                existing = json.load(file)
                if filename in existing:
                    existing[filename].append({'duration':input['duration'], 'answer':answers,'visrep':input['visrep'],'graph':input['graph']})
                else:
                    existing[filename] = [{'duration':input['duration'], 'answer':answers,'visrep':input['visrep'],'graph':input['graph']}]
                file.close()
                file = open('static//users//'+str(userid)+'//training.json','w')
                file.write(json.dumps(existing))
            else:
                file = open('static//users//'+str(userid)+'//training.json','w')
                file.write(json.dumps({filename:[{'duration':input['duration'], 'answer':answers,'visrep':input['visrep'],'graph':input['graph']}]}))
        elif (filename.find('readability') != -1):
            if (os.path.isfile('static//users//'+str(userid)+'//readability.json')): 
                file = open('static//users//'+str(userid)+'//readability.json','r')
                existing = json.load(file)
                if filename in existing:
                    existing[filename].append({'duration':input['duration'], 'answer':answers,'visrep':input['visrep'],'question':input['question'],'iscorrect':input['correct'],'graph':input['graph']})
                else:
                    existing[filename] = [{'duration':input['duration'], 'answer':answers,'visrep':input['visrep'],'question':input['question'],'iscorrect':input['correct'],'graph':input['graph']}]
                file.close()
                file = open('static//users//'+str(userid)+'//readability.json','w')
                file.write(json.dumps(existing))
            else:
                file = open('static//users//'+str(userid)+'//readability.json','w')
                file.write(json.dumps({filename:[{'duration':input['duration'], 'answer':answers,'visrep':input['visrep'],'question':input['question'],'iscorrect':input['correct'],'graph':input['graph']}]}))
        elif (filename.find('background') != -1):
            logfile.write('background\n')
            file = open('static//users//'+str(userid)+'//'+filename+'.json','w')
            file.write(json.dumps({'answers':answers, 'duration':input['duration']}))     
        elif (filename.find('email') != -1):
            logfile.write('email\n')
            file = open('static//users//'+str(userid)+'//background.json','r')
            existing = json.load(file)
            existing[filename] = input['answers']
            file = open('static//users//'+str(userid)+'//background.json','w')
            file.write(json.dumps(existing))
    
    file.close()
    logfile.close()
    
    return jsonify("{'status':'done'}")


@app.route('/static/cgi-bin/updateuserid.py', methods=['POST']) 
def updateuserid():

    logfile = open("log.txt","w")
    file = open("static/data/users.json", "r")
    usersjson = json.load(file)
    file.close()
    thecount = usersjson['usercount']
    print(str(thecount))
    logfile.write(str(thecount))
    print(usersjson)
    
    theerror = 0
    directory = "static/users/"+str(thecount+1)
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        theerror = 1

    if (theerror == 0):
        usersjson['usercount'] = usersjson['usercount'] + 1
        file = open("static/data/users.json", "w")
        file.write(json.dumps(usersjson))
        jsonresponse = {'user':(thecount+1)}
    else:
        jsonresponse = {'user':0}
    file.close()
    logfile.close()

    return jsonify(jsonresponse)
    
if __name__=='__main__':
    app.run(host='0.0.0.0') #run app in debug mode on port 5000