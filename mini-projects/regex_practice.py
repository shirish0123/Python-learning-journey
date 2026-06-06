import re
import string
import pprint

statement='You can contact me at test.user123@example.com or call me at +123-9876543210 if you need help. I recently talked to @shirish about a project we tagged as #AIProject. For more details, visit https://www.google.com where we uploaded the documentation.'
pattern_email = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
pattern_phone=r'\+123-(\d{10})'
pattern_mentions=r'@\w+'
pattern_hashtag=r'#\w+'
pattern_url=r'https?://([a-zA-Z0-9]{3})\.[a-zA-Z0-9]+\.([a-zA-Z]{2,3})'

patterns={
    'Email' : pattern_email,
    'Phone' : pattern_phone,
    'Mentions' : pattern_mentions,
    'Hashtag' : pattern_hashtag,
    'Url' : pattern_url
}
final={}
for i,j in patterns.items():
    final[i]=re.findall(j,statement)

pprint.pprint(final)
