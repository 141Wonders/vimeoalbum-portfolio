from flask import Flask, render_template
import vimeo, json
app = Flask(__name__)

#API key SYNTAX GOES HERE

def decode_json(client):
	# Make the request to the server for the "/me" endpoint.
	#album ID REQUIRED
	about_me = client.get('/me/albums/{album ID goes here}/videos', params={"fields": "name,link,pictures.sizes.link"})

	# Make sure we got back a successful response.
	assert about_me.status_code == 200

	# convert response to json object
	data_encoded = json.dumps(about_me.json())

	# decode the json encoded object
	data_decoded = json.loads(data_encoded)

	 # initialize video data as list of dictionaries
	video_data = data_decoded["data"]

	return video_data
	# returns a list of dictionaries, each dictionary represents a video's data

#initialize main_result as a LIST of DICTIONARIES 
main_result = decode_json(client)

#initialize empty list for thumbnail data
thumbnail_list =[]

#this was a lil tricky, this loop connects each thumbnail with the corresponding video data
for i in range(len(main_result)):

	filtered = main_result[i]['pictures']

	more_filter = filtered.get('sizes')

	tn = more_filter[-1]['link']

	thumbnail_list.append(tn)
	
#Landing page of app, includes video data list & thumbail list
@app.route('/')
def landing():
    return render_template('index.html', main_result=main_result, thumbnail_list=thumbnail_list)


if __name__ == '__main__':    
    app.run(debug=True)
