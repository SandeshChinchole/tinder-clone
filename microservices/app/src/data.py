import requests, json
from flask import request, render_template, jsonify
from src import app

# // For local development,
# // First: connect to Hasura Data APIs directly on port 9000
# // $ hasura ms port-forward data -n hasura --local-port=9000
# // Second: Uncomment the line below
# dataUrl = 'http://localhost:9000/v1/query'

# When deployed to your cluster, use this:
dataUrl = 'http://data.hasura/v1/query'

@app.route("/data")
def get_articles():
    if ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return render_template(
            'filestore_anonymous.html',
            **{'base_domain': request.headers['X-Hasura-Base-Domain']}
        )

    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        requestPayload = {
            "type": "select",
            "args": {
                "table": {
                    "name": "hf_file",
                    "schema": "hf_catalog"
                },
                "columns": [ "*" ],
                "where": {"user_id": request.headers['x-hasura-user-id']}
            }
        }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload))

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return "Something went wrong while trying to fetch files: " + resp.text

        files = resp.json()
        return render_template('filestore_user.html',
            **{
                'base_domain': request.headers['X-Hasura-Base-Domain'],
                'files': files
            })

@app.route("/get-allusers-info")
def getalluserinfo():
    if ('admin' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "insert-user request failed")
    elif ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "insert-user request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        headers = {
              "Content-Type": "application/json",
              'X-Hasura-User-Id': 1,
              'X-Hasura-Role': "admin",
              "X-Hasura-Allowed-Roles": "user,admin"
        }
        requestPayload = {
        'type': 'select',
        'args': {
        'table': 'userinfo',
        'columns': [
          '*'
            ]
          }
        }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return jsonify(message = "get-allusers-info request failed")
        data = resp.json()
        print(json.dumps(data))
        return jsonify(data=data)

@app.route("/like",methods=['POST'])
def like():
    if ('admin' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "like request failed")
    elif ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "like request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        headers = {
                "Content-Type": "application/json",
                'X-Hasura-User-Id': request.headers['X-Hasura-User-Id'],
                'X-Hasura-Role': request.headers['x-hasura-role'],
                "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
        }
        requestPayload = {
            "type": "insert",
            "args": {
                "table": "match",
                "objects": [
                   "like_user_id": request.form['like_user_id'],
                    "hasura_id": request.headers['X-Hasura-User-Id']
                ]
            }
        }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload),headers=headers)

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return jsonify(message = "like request failed")
        data = resp.json()
        print(json.dumps(data))
        return jsonify(data=data)

@app.route("/nope",methods=['POST'])
def nope():
    if ('admin' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "nope request failed")
    elif ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "nope request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        headers = {
                "Content-Type": "application/json",
                'X-Hasura-User-Id': request.headers['X-Hasura-User-Id'],
                'X-Hasura-Role': request.headers['x-hasura-role'],
                "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
        }
        requestPayload = {
            "type": "delete",
            "args": {
              "table": "match",
              "where": {
                  "$and": [
                      {
                          "hasura_id": {
                              "$eq": request.headers['X-Hasura-User-Id']
                          }
                      },
                      {
                          "like_user_id": {
                              "$eq": request.form['like_user_id']
                              }
                          }
                      ]
                  }
              }
            }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload),headers=headers)

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return jsonify(message = "nope request failed")
        data = resp.json()
        print(json.dumps(data))
        return jsonify(data=data)

@app.route("/like-users")
def like_users():
    if ('admin' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "like-users request failed")
    elif ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "like-users request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        query = "select match.like_user_id, userinfo.name,userinfo.profile_file_id from match,userinfo where match.like_user_id = userinfo.hasura_id AND match.hasura_id ="+request.headers['X-Hasura-User-Id']
        # Setting headers
        headers = {
              "Content-Type": "application/json",
              'X-Hasura-User-Id': 1,
              'X-Hasura-Role': "admin",
              "X-Hasura-Allowed-Roles": "user,admin"
        }
        requestPayload = {
            "type": "run_sql",
            "args": {
              "sql": query
            }
         }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return jsonify(message = "like-users request failed")
        data = resp.json()
        print(json.dumps(data))
        return jsonify(data=data)

@app.route("/update-user",methods=['POST'])
def update_user():
    if ('admin' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "update-user request failed")
    elif ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "update-user request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        headers = {
                "Content-Type": "application/json",
                'X-Hasura-User-Id': request.headers['X-Hasura-User-Id'],
                'X-Hasura-Role': request.headers['x-hasura-role'],
                "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
        }
        requestPayload = {
            "type": "update",
            "args": {
              "table": "userinfo",
              "where": {
                  "hasura_id": {
                      "$eq": request.headers['X-Hasura-User-Id']
                  }
              },
              "$set": {
                  "email": request.form['email'],
                  "name": request.form['name'],
                  "age": request.form['age'],
                  "about_me": request.form['about']
              }
            }
        }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload),headers=headers)

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return jsonify(message = "update-user request failed")
        data = resp.json()
        print(json.dumps(data))
        return jsonify(data=data)

@app.route("/insert-user",methods=['POST'])
def insert_user():
    if ('admin' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "insert-user request failed")
    elif ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "insert-user request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        headers = {
                "Content-Type": "application/json",
                'X-Hasura-User-Id': request.headers['X-Hasura-User-Id'],
                'X-Hasura-Role': request.headers['x-hasura-role'],
                "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
        }
        requestPayload = {
            "type": "insert",
            "args": {
              "table": "userinfo",
              "objects": [
                  {
                      "hasura_id": request.headers['X-Hasura-User-Id'],
                      "name": request.form['name'],
                      "email": request.form['email'],
                      "gender": request.form['gender'],
                      "profile_file_id": request.form['file_id'],
                      "age":request.form['age'],
                      "about_me": request.form['about_me'],
                      "city": request.form['city']
                  }
              ]
            }
        }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload),headers=headers)

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return jsonify(message = "insert-user request failed")
        data = resp.json()
        print(json.dumps(data))
        return jsonify(data=data)

@app.route("/delete",methods=['POST'])
def insert_user():
    if ('admin' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "delete request failed")
    elif ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "delete request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        headers = {
                    'X-Hasura-User-Id': 1,
                    "Content-Type": "application/json",
                     'X-Hasura-Role': "admin",
                     "X-Hasura-Allowed-Roles": "user,admin"
        }
        requestPayload = {
            "hasura_id": request.headers['X-Hasura-User-Id']
        }

        resp = requests.post(dataUrl, data=json.dumps(requestPayload),headers=headers)

        # resp.content contains the json response.
        if not(resp.status_code == 200):
            print (resp.text)
            return jsonify(message = "delete request failed")
        data = resp.json()
        print(json.dumps(data))
        return jsonify(data=data)
