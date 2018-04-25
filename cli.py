#!/usr/bin/python
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
@click.argument('dst', nargs=-1)


def tcmg476(src, dst):
    
    blah = ''
    #url = 'http://35.192.69.243/'
    url = 'http://localhost:5000/'
    normal_url=url+src+'/'

    uknown_value="That key has not been inputted"
    if src == 'kv-record':
        kv_url =url+src
        
        ls =[]
        #print(dst)
        for i in dst:
            ls.append(str(i))
        print(kv_url)
        payload ={ls[0]: ls[1]}
        r = requests.post(kv_url, data=payload)
        requests.post(kv_url, data=payload)
        print(payload)
        print(r.content[50])
        
        
    # elif src == 'kv-retrieve':
    #     ls =[]
    #     #print(dst)
    #     for i in dst:
    #         ls.append(str(i))
    #     print(ls[0])
    #     print(retrieve)
    #     url=url+ls[0]
    #     r = requests.get(url)
    #     print(r)
        #print(retrieve.get(str(ls[0]), uknown_value))
        
        
    elif len(dst)>1:
        for i in dst:
            blah = blah+str(i)+' '
        dst =blah
        normal_url=unormal_urlrl+dst
        r = requests.get(normal_url)
        print(r.content)
    else:
        for i in dst:
            dst = str(i)
            normal_url=normal_url+dst
        r = requests.get(normal_url)
        print(r.content)
    
    #print(url)

    


if __name__ == '__main__':
    

    #url = 'http://35.192.69.243/'
    url = 'http://localhost:5000/'
    tcmg476()


    

    

    

    