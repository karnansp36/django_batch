posts=[
    {"id":2, "title":"django", "content":"new content"},
    {"id":3, "title":"flask", "content":"new content"},
     {"id":4, "title":"python", "content":"new content"}]

for x in posts:
    print(x['title'])
    print(x['content'])