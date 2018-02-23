import json
import os
import sys
import requests
from flask import Blueprint, jsonify

PRODUCTION_ENV = os.environ.get("PRODUCTION")
CLUSTER_NAME = os.environ.get("CLUSTER_NAME")
if CLUSTER_NAME is None:
    print("""
    Set the name of your cluster as an environment variable and start again:

    $ export CLUSTER_NAME=<cluster-name>

    """)

if PRODUCTION_ENV == "true":
    # set dataUrl as internal url if PRODUCTION_ENV is true
    # note that internal url has admin permissions
    dataUrl = 'http://data.hasura/v1/query'
else:
    # for local development, contact the cluster via external url
    dataUrl = "https://data." + CLUSTER_NAME + ".hasura-app.io/v1/query"

hasura_examples = Blueprint('hasura_examples', __name__)
@hasura_examples.route("/")
def home():
    return 'hellow- world'
@hasura_examples.route("/like",methods=['POST'])
def like():
     hasura_id = request.headers['X-Hasura-User-Id']
     if hasura_id not in [0 , 1] :
# This is the url to which the query is made
url = 'http://data.hasura/v1/query'
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
        "type": "insert",
        "args": {
            "table": "match",
            "objects": [
               "like_user_id": request.form['like_user_id'],
                "hasura_id": hasura_id
            ]
        }
    }
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify({'message': 'like request failed'})

@hasura_examples.route("/nope",methods=['POST'])
def nope():
     hasura_id = request.headers['X-Hasura-User-Id']
     if hasura_id not in [0 , 1] :
# This is the url to which the query is made
url = 'http://data.hasura/v1/query'
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
"type": "delete",
"args": {
  "table": "match",
  "where": {
      "$and": [
          {
              "hasura_id": {
                  "$eq": hasura_id
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
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify({'message': 'nope request failed'})

@hasura_examples.route("/like-users")
def likeUsers():
     hasura_id = request.headers['X-Hasura-User-Id']
     if hasura_id not in [0 , 1] :
# This is the url to which the query is made
url = 'http://data.hasura/v1/query'
sql = query = "select match.like_user_id, userinfo.name,userinfo.profile_file_id from match,userinfo where match.like_user_id = userinfo.hasura_id AND match.hasura_id ="+hasura_id
# Setting headers
headers = {
        "Content-Type": "application/json",
      'X-Hasura-User-Id': 1,
      'X-Hasura-Role': "admin",
      "X-Hasura-Allowed-Roles": "user,admin"
}
    query = {
    "type": "run_sql",
    "args": {
      "sql": sql
    }
  }
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify({'message': 'like-users request failed'})

@hasura_examples.route("/update-user",methods=['POST'])
def update():
     hasura_id = request.headers['X-Hasura-User-Id']
     if hasura_id not in [0 , 1] :
# This is the url to which the query is made
url = 'http://data.hasura/v1/query'
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
"type": "update",
"args": {
  "table": "userinfo",
  "where": {
      "hasura_id": {
          "$eq": hasura_id
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
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify({'message': 'update-user request failed'})

@hasura_examples.route("/insert-user",methods=['POST'])
def insert():
     hasura_id = request.headers['X-Hasura-User-Id']
     if hasura_id not in [0 , 1] :
# This is the url to which the query is made
url = 'http://data.hasura/v1/query'
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
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
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify({'message': 'insert-user request failed'})


@hasura_examples.route("/get-allusers-info")
def getalluserinfo():
     hasura_id = request.headers['X-Hasura-User-Id']
     if hasura_id not in [0 , 1] :
# This is the url to which the query is made
url = 'http://data.hasura/v1/query'
# Setting headers
headers = {
        "Content-Type": "application/json",
      'X-Hasura-User-Id': 1,
      'X-Hasura-Role': "admin",
      "X-Hasura-Allowed-Roles": "user,admin"
}
    query = {
    'type': 'select',
    'args': {
    'table': 'userinfo',
    'columns': [
      '*'
        ]
      }
      }
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify({'message': 'get-allusers-info request failed'})

@hasura_examples.route("/delete",methods=['POST'])
def delete():
     hasura_id = request.headers['X-Hasura-User-Id']
     if hasura_id not in [0 , 1] :
# This is the url to which the query is made
url= 'http://auth.hasura/v1/admin/delete-user'
# Setting headers
headers = {
'X-Hasura-User-Id': 1,
    "Content-Type": "application/json",
      'X-Hasura-Role': "admin",
      "X-Hasura-Allowed-Roles": "user,admin"
      }
    query = {
    "hasura_id": hasura_id
    }
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify({'message': 'delete request failed'})










@app.route("/delete",methods=['POST'])
def delete():
     hasura_id = request.headers['X-Hasura-User-Id']
     if (hasura_id not in [0 , 1]):
# This is the url to which the query is made
 url = 'http://auth.hasura/v1/admin/delete-user'
# Setting headers
headers = {
'X-Hasura-User-Id': 1,
    "Content-Type": "application/json",
      'X-Hasura-Role': "admin",
      "X-Hasura-Allowed-Roles": "user,admin"
      }
    query = {
    "hasura_id": hasura_id
    }
    print(url)
    print(json.dumps(query))
    response = requests.post(
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify(message = "delete request failed")
@app.route("/like",methods=['POST'])
def like():
     hasura_id = request.headers['X-Hasura-User-Id']
     if (hasura_id not in [0 , 1]):
# This is the url to which the query is made
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
        "type": "insert",
        "args": {
            "table": "match",
            "objects": [
               "like_user_id": request.form['like_user_id'],
                "hasura_id": hasura_id
            ]
        }
    }
    print(url)
    print(json.dumps(query))
    response = requests.post(
        dataUrl, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify(message = "like request failed")

@app.route("/nope",methods=['POST'])
def nope():
     hasura_id = request.headers['X-Hasura-User-Id']
     if (hasura_id not in [0 , 1]):
# This is the url to which the query is made
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
"type": "delete",
"args": {
  "table": "match",
  "where": {
      "$and": [
          {
              "hasura_id": {
                  "$eq": hasura_id
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
    print(url)
    print(json.dumps(query))
    response = requests.post(
        dataUrl, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify(message = "nope request failed")

@app.route("/like-users")
def likeUsers():
     hasura_id = request.headers['X-Hasura-User-Id']
     if (hasura_id not in [0 , 1]):
# This is the url to which the query is made
sql = query = "select match.like_user_id, userinfo.name,userinfo.profile_file_id from match,userinfo where match.like_user_id = userinfo.hasura_id AND match.hasura_id ="+hasura_id
# Setting headers
headers = {
        "Content-Type": "application/json",
      'X-Hasura-User-Id': 1,
      'X-Hasura-Role': "admin",
      "X-Hasura-Allowed-Roles": "user,admin"
}
    query = {
    "type": "run_sql",
    "args": {
      "sql": sql
    }
  }
    print(url)
    print(json.dumps(query))
    response = requests.post(
        dataUrl, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify(message = "like-users request failed")

@app.route("/update-user",methods=['POST'])
def update():
     hasura_id = request.headers['X-Hasura-User-Id']
     if (hasura_id not in [0 , 1]):
# This is the url to which the query is made
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
"type": "update",
"args": {
  "table": "userinfo",
  "where": {
      "hasura_id": {
          "$eq": hasura_id
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
    print(url)
    print(json.dumps(query))
    response = requests.post(
        dataUrl, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify(message = "update-user request failed")

@app.route("/insert-user",methods=['POST'])
def insert():
     hasura_id = request.headers['X-Hasura-User-Id']
     if (hasura_id not in [0 , 1]):
# This is the url to which the query is made
# Setting headers
headers = {
    "Content-Type": "application/json",
      'X-Hasura-User-Id': hasura_id,
      'X-Hasura-Role': request.headers['x-hasura-role'],
      "X-Hasura-Allowed-Roles": request.headers['x-hasura-allowed-roles']
}
    query = {
"type": "insert",
"args": {
  "table": "userinfo",
  "objects": [
      {
          "hasura_id": hasura_id,
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
    print(url)
    print(json.dumps(query))
    response = requests.post(
        dataUrl, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify(message = "insert-user request failed")








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
def delete():
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
