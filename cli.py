##!/usr/bin/python
import click
import requests
import json
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
    url = 'http://35.202.79.180/'
    #url = 'http://localhost:5000/'
    normal_url=url+src+'/'

    uknown_value="That key has not been inputted"
    if src == 'kv-record':
        kv_url =url+src
        
        ls =[]
        #print(dst)
        for i in dst:
            ls.append(str(i))
        #print(kv_url)
        payload ={ls[0]: ls[1]}
        r = requests.post(kv_url, data=payload)
        requests.post(kv_url, data=payload)
        dic = {}
        dic.update(r.json())

        if 'output' in dic:
            print(dic['output'])
        elif 'error' in dic:
            print(dic['error'])
        #print(r.content)
        #print(r.status_code)
        #print(payload)

        
        
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
        dic = {}
        dic.update(r.json())

        if 'output' in dic:
            print(dic['output'])
        elif 'error' in dic:
            print(dic['error'])
    else:
        for i in dst:
            dst = str(i)
            normal_url=normal_url+dst
        r = requests.get(normal_url)
        dic = {}
        dic.update(r.json())

        if 'output' in dic:
            print(dic['output'])
        elif 'error' in dic:
            print(dic['error'])
        #print(r.json())
        #parsed_json = json.loads(r.text)
        #print(parsed_json(['\n']['output'])
        # if r.json()['error'] == test_result[1] or r.json()['output'] == test_result[1]:
        
    
    #print(url)

    


if __name__ == '__main__':
    

    url = 'http://35.202.79.180/'
    #url = 'http://localhost:5000/'
    tcmg476()


    

    

    

    