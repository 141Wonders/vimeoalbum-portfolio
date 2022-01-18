# vimeoalbum-portfolio
Retrieve vimeo album video data 

## Get started
Input Vimeo API keys & album ID
```
from flask import Flask, render_template
import vimeo, json
app = Flask(__name__)

#API key SYNTAX GOES HERE

def decode_json(client):
	# Make the request to the server for the "/me" endpoint.
	#album ID REQUIRED
	about_me = client.get('/me/albums/{album ID goes here}/videos', params={"fields": "name,link,pictures.sizes.link"})
```

## [View App](https://derekhenriquez-editor.com/)
