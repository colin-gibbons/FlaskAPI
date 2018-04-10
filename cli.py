import click
import requests

# url = 'http://35.185.41.112/kv-record'
# payload = {'professor': 'adam'}
# r = requests.post(url, data=payload)

r = requests.get("http://localhost:5000/is-prime/7")

print (r.status_code)
print (r.headers)
print (r.content)

@click.command()
@click.argument('md5_test')
def touch(md5_test):
    click.echo(md5_test)

