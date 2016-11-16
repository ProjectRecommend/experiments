# jQgfPZNxlkvrINfWvVjPrtbnfvAQLMrGeJHLyZeO
import discogs_client as dc

client = dc.Client('test App', user_token="jQgfPZNxlkvrINfWvVjPrtbnfvAQLMrGeJHLyZeO")

# result = client.search('Rick Astley', type='master', year='2002')
# result = client.search('Justin Bieber', type='relese', genre='pop')
result = client.search('Justin Bieber', type='relese', genre='pop', year='2010')
# result = client.search('Never Gonna Give you up', type='release')

# print(dir(result))
print(result.pages)
songs = []
for i in range(result.pages):
    x = result[i]
    # print(dir(x))
    # print(x)
    # print(x.title)
    songs.append(x.title)

songs = set(songs)

for song in songs:
    print(song)

# res = client.search('Rick Astley', type='artist')[0].releases
# print(len(res))
# for i in range(len(res)):
#     print(res[i])
