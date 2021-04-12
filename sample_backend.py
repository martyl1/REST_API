from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
import string
app = Flask(__name__)
CORS(app)



@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['name'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      
      return users
   
   elif request.method == 'DELETE':
      userToDelete = request.get_json()
      try:
         users['users_list'].remove(userToDelete)
       
      except ValueError:
         resp = jsonify(sucess=False)
         resp.status_code = 404
         return resp

      resp = jsonify(sucess=True)
      resp.status_code = 204
      return resp
      
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
      users['users_list'].append(userToAdd)
      resp = jsonify(sucess=True)
      resp.status_code = 201
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}



