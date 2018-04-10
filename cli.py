###!/usr/bin/python
import click
import requests

# url = 'http://35.185.41.112/'
# payload = {'professor': 'adam'}
#r = requests.post(url, data=payload)

# r = requests.get("http://localhost:5000/is-prime/7")

# print (r.status_code)
# print (r.headers)
# print (r.content)


@click.command()

@click.argument('src', nargs=1)
@click.argument('dst', nargs=1)

def tcmg476(src, dst):
    url = 'http://35.185.41.112/'
    url=url+src+'/'
    url=url+dst
    
    print(url)
    r = requests.get(url)
    print(r.content)


if __name__ == '__main__':


    url = 'http://35.185.41.112/'
    tcmg476()


    

    