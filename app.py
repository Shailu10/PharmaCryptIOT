from flask import Flask,jsonify,render_template,request,redirect,url_for,flash
from config import Config
import json
import urllib.request

app=Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET','POST'])
def welcome():
    return render_template('welcome.html')

@app.route('/fetch_data', methods=['GET','POST'])
def fetch_data():
    websitedata=urllib.request.urlopen("https://api.thingspeak.com/channels/997798/feeds.json?api_key=42VRRZDFUAB0OWUD&results=2")
    print(websitedata.read())
    # jsonResponse=json.load(websitedata)
    showdata=websitedata.read()
    print(showdata)
    #showdata=showdata.decode("utf-8")
    #showwdata=str(showdata,'utf-8')
    print(showdata)
    with open('data.json','a') as file:
        file.write(str(showdata))
    return render_template('show.html',data=showdata)

if __name__ == '__main__':
    app.run(debug=True)