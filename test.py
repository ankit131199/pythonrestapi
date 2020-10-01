import math
import requests
from test_apis import get_api, post_api
total, verified, errors = [0, 0, 0]


def get_api_test():
    global total, verified, errors

    for apis in get_api:
        total += 1
        x = requests.get(apis['url'])
        if x.status_code != apis['status']:
            errors += 1
            print(f'error in {apis["url"]}')
        else:
            verified += 1
            print(f'verified api - {apis["url"]}')

    print(
        f"exit\n  Total succesfully verified = {verified} Total errors = {errors}")


def post_api_request():
    global total, verified, errors
    
    for apis in post_api:
        try:
            if apis['data']['key'] == '':
                apis['data']['key'] = input('enter key from mail')
        except:
            pass

        
        x = requests.post(apis['url'], data=apis['data'])
        if x.status_code != apis['status']:
            errors += 1
            print(f'error in {apis["url"]}')
        else:
            verified += 1
            print(f'verified api - {apis["url"]}')

    print(
        f"exit\n  Total succesfully verified = {verified} Total errors = {errors}")



if __name__ == "__main__": 
    print('testing get requests-----------------------')
    get_api_test()
    print('\n')
    print('testing post requests-----------------------')
    print("\n")
    post_api_request()
    while(1): pass

