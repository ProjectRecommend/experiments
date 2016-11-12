import tags
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

filname = 'xxx.mp3'

# get metadata and preprocess

metadata = tags.metadata(filname)
metatext = tags.metaTextToUnicode(metadata)

vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(metatext)

# print(X)
print(vectorizer.get_feature_names())

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)

print(kmeans.predict(X))
