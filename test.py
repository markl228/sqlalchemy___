from requests import get, post, delete

# print(get('http://localhost:5000/api/news/1').json(), end='\n\n')
# print(get('http://localhost:5000/api/news/2').json(), end='\n\n')
# print(get('http://localhost:5000/api/news/3').json(), end='\n\n')
# print(get('http://localhost:5000/api/news/4').json(), end='\n\n')

# print(post('http://localhost:5000/api/news').json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())

print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/news/1').json())