from flask import Flask, render_template
import vimeo, json
app = Flask(__name__)


client = vimeo.VimeoClient(
	#API key SYNTAX GOES HERE
)

#function to get video link, name, and thumbail from a specified album
def decode_json_reel(client, id):
	# Make the request to the server for the "/me" endpoint.
	about_me = client.get('/me/albums/'+ id +'/videos?sort=manual', params={"fields": "name,link,pictures.sizes.link"})

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

#function to get ONLY thumbnails from gallery directory album
def decode_json_album(client, id):
	about_me = client.get('/me/albums/' + id + '/videos?sort=manual', params={"fields": "pictures.sizes.link"})
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

#function to extract 1920x1080 thumbnail size from GET request into a list
def get_thumbnails(json_list):
	#initialize empty list for thumbnail data
	thumbnail_list =[]

	#this was a lil tricky, this loop connects each thumbnail with the corresponding video data
	#We want to get the 1920x1080 image which is the last item in the list, so we use [-1] from the thumbnail list
	for i in range(len(json_list)):

		filtered = json_list[i]['pictures']

		more_filter = filtered.get('sizes')

		tn = more_filter[-1]['link']

		thumbnail_list.append(tn)

	return thumbnail_list

#Landing page of app, includes video data list & thumbail list
@app.route('/')
def landing():
	main_result = decode_json_reel(client,'7693012')
	reel_thumbnail_list = get_thumbnails(main_result)
	#initialize main_result as a LIST of DICTIONARIES 
	return render_template('index.html', main_result=main_result, reel_thumbnail_list=reel_thumbnail_list)

#About Me page
@app.route('/about/')
def bio():
	return render_template('generic.html')

#Campaign Directory, GET thumbnails from directory album
#page is made into a list, whichever album is picked gets redirected to the next app.route
@app.route('/campaigns/')
def campaigns():
	album_result = decode_json_album(client,'9214209')
	album_thumbnail_list = get_thumbnails(album_result)

	album_result[0]['re_direct'] = "De-Viaje-con-los-Derbez"
	album_result[1]['re_direct'] = "Juego-de-las-Llaves"
	album_result[2]['re_direct'] = "ANA"
	album_result[3]['re_direct'] = "Herederos-Por-Accidente"
	album_result[4]['re_direct'] = "De-Brutas-Nada"
	album_result[5]['re_direct'] = "R"
	album_result[6]['re_direct'] = "I'll-Sleep-When-I'm-Dead"
	album_result[7]['re_direct'] = "Maya-The-Bee"
	return render_template('campaigns.html', album_result=album_result, album_thumbnail_list=album_thumbnail_list)

#Gets specified campagin route to show its corresponding campaign reel
@app.route('/campaigns/<campaign>/')
def front(campaign):
	if campaign == "De-Viaje-con-los-Derbez":
		pass_result = decode_json_reel(client,'9231645')
		pass_thumbnail = get_thumbnails(pass_result)

	if campaign == "Juego-de-las-Llaves":
		pass_result = decode_json_reel(client,'8246171')
		pass_thumbnail = get_thumbnails(pass_result)

	if campaign == "Herederos-Por-Accidente":
		pass_result = decode_json_reel(client,'8136339')
		pass_thumbnail = get_thumbnails(pass_result)

	if campaign == "De-Brutas-Nada":
		pass_result = decode_json_reel(client,'8136337')
		pass_thumbnail = get_thumbnails(pass_result)

	if campaign == "R":
		pass_result = decode_json_reel(client,'8136327')
		pass_thumbnail = get_thumbnails(pass_result)

	if campaign == "Maya-The-Bee":
		pass_result = decode_json_reel(client,'8136345')
		pass_thumbnail = get_thumbnails(pass_result)

	if campaign == "ANA":
		pass_result = decode_json_reel(client,'8084695')
		pass_thumbnail = get_thumbnails(pass_result)

	if campaign == "I'll-Sleep-When-I'm-Dead":
		pass_result = decode_json_reel(client,'8136342')
		pass_thumbnail = get_thumbnails(pass_result)

	return render_template('ind_campaign.html', pass_result=pass_result, pass_thumbnail=pass_thumbnail).format(campaign=campaign)

if __name__ == '__main__':
		app.run(debug=True)
