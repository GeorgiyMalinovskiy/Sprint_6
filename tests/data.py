from datetime import datetime, timedelta
test_data =[
    ('top', {
        'name': 'Иван',
        'surname': 'Иванов',
        'address': 'ул. Ленина, 1',
        'metro': 'Сокольники',
        'phone': '+79991234567'
    }, {
        'date': (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y'),
        'rental_period': 'сутки',
        'color': 'black',
        'comment': 'Позвоните за час до доставки'
    }),
    ('bottom', {
        'name': 'Петр',
        'surname': 'Петров',
        'address': 'ул. Пушкина, 10',
        'metro': 'Лубянка',
        'phone': '+79997654321'
    }, {
        'date': (datetime.now() + timedelta(days=2)).strftime('%d.%m.%Y'),
        'rental_period': 'двое суток',
        'color': 'grey',
        'comment': 'Домофон не работает, звоните'
    })
]