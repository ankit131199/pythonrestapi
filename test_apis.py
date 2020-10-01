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
            "college": "xyzxyz",
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
        
    }

]
