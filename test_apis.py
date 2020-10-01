get_api = [
    {
        'url': 'https://o1codingclub.herokuapp.com/blog/',
        'status': 200
    },

    {
        'url': 'https://o1codingclub.herokuapp.com/placement/',
        'status': 200
    },

    {
        'url': 'https://o1codingclub.herokuapp.com/contest/',
        'status': 200
    },

    {
        'url': 'http://o1codingclub.herokuapp.com/contest?type=2&status=0',
        'status': 200
    },

    {
        'url': 'http://o1codingclub.herokuapp.com/contest?type=0',
        'status': 200
    },

    {
        'url': 'http://o1codingclub.herokuapp.com/contest?status=1',
        'status': 200
    }

]

post_api = [
    {
        'url': 'https://o1codingclub.herokuapp.com/blog/requestkey/',
        'data': {
            "fullname": "xyzxyz",
            "college": "RCOEM",
            "branch": "xyzxyz",
            "email": "aditya.morankar8@gmail.com"
        },
        'status': 200
    },

    {
        'url': 'https://o1codingclub.herokuapp.com/blog/create/',
        'data': {

            "author": "xyzxyz",
            "title": "this is title",
            "body": "this is body",
            "email": "aditya.morankar8@gmail.com",
            "fullname": "xyzxyz",
            "key": ''
        },
        'status': 200
    },

    {
        'url': 'https://o1codingclub.herokuapp.com/blog/',
        'data': {
            'key': 'gAAAAABfYys99vhKbNtgKJ5PB_HgqIeQ5qFW_Nz4j8m_p8p0zOKVFjs4y6VxMeCLJMmJtB2e7X7F69tYenleGxfBxeOqPyPjJll-60Ol9AJWW48JI6cCAKG0fDAGdJPlDAom8TUl_r6l',
        },
        'status': 200
    },

    {
        'url': 'https://o1codingclub.herokuapp.com/blog/',
        'data':
        {
            'key': 'ahgjheywieuhjbd,jfdweirkluewriowuer9woiiklfdjsdf',
        },
        'status': 404
    },

    {
        'url': 'https://o1codingclub.herokuapp.com/blog/approve/1000000',
        'data':
        {
            'key': 'gAAAAABfYys99vhKbNtgKJ5PB_HgqIeQ5qFW_Nz4j8m_p8p0zOKVFjs4y6VxMeCLJMmJtB2e7X7F69tYenleGxfBxeOqPyPjJll-60Ol9AJWW48JI6cCAKG0fDAGdJPlDAom8TUl_r6l',
        },
        'status': 404
    },

    {
        'url': f'https://o1codingclub.herokuapp.com/blog/approve/{int(input("enter id of blog"))}',
        'data':
        {
            'key': 'gAAAAABfYys99vhKbNtgKJ5PB_HgqIeQ5qFW_Nz4j8m_p8p0zOKVFjs4y6VxMeCLJMmJtB2e7X7F69tYenleGxfBxeOqPyPjJll-60Ol9AJWW48JI6cCAKG0fDAGdJPlDAom8TUl_r6l',
        },
        'status': 200
    }
]
