from flask import Flask, render_template, request
import os
import requests
import json

app = Flask(__name__)


def execute_rest(method, url, bearertoken, payload):
    headers = {
        'Authorization': 'BEARER ' + bearertoken + '',
        'Content-Type': 'application/json'
    }
    response = requests.request(
        method, url, headers=headers, data=payload, verify=False)
    json = response.json()  # type: object

    return json


url = "https://api.starcitizen-api.com/dMuf7rbc9Py1VWedOCPME8td9s5c99OW/v1/live/organization_members/EXEP"
response = execute_rest("get", url, "", "")


@app.route('/')
def index():
    color = os.environ.get("COLOR")

    return render_template('index.html', members=response['data'], color=color)


@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        member_info = []
        thing = request.form.get('member')
        for r in response['data']:
            if r['handle'].__contains__(thing):
                member_info.append(r)
        return render_template('results.html', member=member_info)


if __name__ == "__main__"
  app.run(host='0.0.0.0', port='8080')
