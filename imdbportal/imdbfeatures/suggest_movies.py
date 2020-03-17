
def get_movie_names_for_imdb(srch_term):
	import requests, json
	def jsonp_to_json(jsonp):
		json = jsonp[jsonp.find('{'):-1]
		return json
	def get_suggestion_json(srch_term):
		api_str = f"https://v2.sg.media-imdb.com/suggests/{srch_term[0]}/{srch_term}.json"
		#https://sg.media-imdb.com/suggests/{srch_term[0]}/{srch_term}.json
		return jsonp_to_json(requests.get(api_str).text)

	ret_response = get_suggestion_json(srch_term)
	data = json.loads(ret_response)['d']
	movie_names_with_id = dict()

	for i in range(len(data)):
		instance = data[i]
		# print(instance['l'], instance['id'], len(instance['id']));
		if 'nm' in instance['id']:
			continue;
		movie_names_with_id[instance['l']] = instance['id']

	return movie_names_with_id;

def get_movie_names_for(srch_term):
	import omdb
	from .secretfile import omdbapikey #this is my own api for omdb
#will not work outside django
	client = omdb.OMDBClient(apikey=omdbapikey)
	data = client.search_movie(srch_term)

	movie_names_with_id = dict()

	for i in range(len(data)):
		instance = data[i]
		movie_names_with_id[instance['title']] = instance['imdb_id']
	return movie_names_with_id



def main():
	print(get_movie_names_for('matrix'))
if __name__ == '__main__':
	main()