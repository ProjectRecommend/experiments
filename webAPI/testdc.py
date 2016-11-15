# jQgfPZNxlkvrINfWvVjPrtbnfvAQLMrGeJHLyZeO
import discogs_client as dc

client = dc.Client('test App', user_token="jQgfPZNxlkvrINfWvVjPrtbnfvAQLMrGeJHLyZeO")

# result = client.search('Rick Astley', type='master', year='2002')
result = client.search('Rick Astley', type='relese', genre='pop')

# result = client.search('Never Gonna Give you up', type='release')

print(result)
print(result.pages)
for i in range(result.pages):
    x = result[i]
    # print(x)
    print(x.title)

# res = client.search('Rick Astley', type='artist')[0].releases
# print(len(res))
# for i in range(len(res)):
#     print(res[i])
