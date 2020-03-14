import omdb
from .secretfile import omdbapikey #this is my own api for omdb
#will not work outside django

client = omdb.OMDBClient(apikey=omdbapikey)

def by_imdb_id(imdb_id):
	movie_info = client.imdbid(imdb_id);
	tmpdict = dict()
	if 'ratings' in movie_info.keys():
		for item in movie_info['ratings']:
			tmpdict[item['source']] = item['value'] #That simplifies ratings, will be easier to render in django template
		movie_info['ratings'] = tmpdict
	return movie_info;










def main():
	print(by_imdb_id("tt1226837"))

if __name__ == '__main__':
	main()