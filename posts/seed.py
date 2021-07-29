from posts.models import User
from datetime import date

users = [
    {
        'email': 'cvander@d-insta.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '123456',
        'is_admin': True,
    },
    {
        'email': 'freddie@d-insta.com',
        'first_name': 'Freddy',
        'last_name': 'Fargas',
        'password': '123456',
    },
    {
        'email': 'Yesica@d-insta.com',
        'first_name': 'Fortes',
        'last_name': 'qwerty',
        'password': '123456',
        'birthdate': date(1990, 12, 19)
    },
    {
        'email': 'Arturo@d-insta.com',
        'first_name': 'Fortes',
        'last_name': 'Gonzalez',
        'password': '123456',
        'birthdate': date(1990, 12, 19),
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "The past of the righteous man is beset on all sided by the iniquities of the selfish and..."
    },
]


for user in users:
    obj = User.objects.create(**user)
    print(obj.pk)
