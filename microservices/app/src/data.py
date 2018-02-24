import requests, json
from flask import request, render_template, jsonify, Response
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
    if ('admin' in request.headers['x-hasura-allowed-roles']) or \
        ('anonymous' in request.headers['x-hasura-allowed-roles']):
        return jsonify(message = "like request failed")
    # If user is logged in, show the user files they have uploaded
    else:
        # Query from the file-upload table to fetch files this user owns.
        # We're using the Hasura data APIs to query
        headers = {
              "Content-Type": "application/json",
              'X-Hasura-User-Id': '1',
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
        #may be we can use this but it's ok to use directly jsonfiy here
        #return Response(json.dumps(data),  mimetype='application/json')
        return jsonify(data)
