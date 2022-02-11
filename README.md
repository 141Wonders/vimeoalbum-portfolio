# vimeoalbum-portfolio
Retrieve public vimeo album data 

## Get started
Input Vimeo API keys
You must first register app on Vimeo following this guide [HERE](https://developer.vimeo.com/api/guides/start)
Enter key syntax in main.py here:

```
client = vimeo.VimeoClient(
	#API key SYNTAX GOES HERE
)
```

## Getting album data
You can specify a certain video album(or showcase) using the album ID in a get request or as an argument below:

```
def get_album_data(client, id):
	# Make the request to the server for the "/me" endpoint.
	about_me = client.get('/me/albums/'+ id +'/videos?sort=manual', params={"fields": "name,link,pictures.sizes.link"})
```

## [View App](https://derekhenriquez-editor.com/)