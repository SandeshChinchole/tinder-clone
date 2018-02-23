import requests, json
from flask import request, render_template
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
    if ('hasura-app.io' in request.url_root) or \
       ('data.hasura' not in dataUrl):

        query = {
            "type": "select",
            "args": {
                "table": "article",
                "columns": [ "title", "id", "author_id", "rating", "title" ],
                "limit": 10
            }
        }

        response = requests.post(dataUrl, data=json.dumps(query))
        if response.status_code == 200:
            return render_template('data.html', data=json.dumps(response.json(), indent=2, sort_keys=True))
        else:
            return 'Something went wrong: <br/>' + str(response.status_code) + '<br/>' + response.text

    # Change the data URL during local development
    return ("""Edit the dataUrl variable in
        <code>microservices/app/src/hasura.py</code>
        to test locally.""")


@app.route("/like",methods=['POST'])
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
else: return jsonify(message = "like request failed")

@app.route("/nope",methods=['POST'])
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
else: return jsonify(message = "nope request failed")

@app.route("/like-users")
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
else: return jsonify(message = "like-users request failed")

@app.route("/update-user",methods=['POST'])
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
else: return jsonify(message = "update-user request failed")

@app.route("/insert-user",methods=['POST'])
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
        url, data=json.dumps(query),headers=headers
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
else: return jsonify(message = "insert-user request failed")


@app.route("/get-allusers-info")
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
else: return jsonify(message = "get-allusers-info request failed")

@app.route("/delete",methods=['POST'])
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
else: return jsonify(message = "delete request failed")
