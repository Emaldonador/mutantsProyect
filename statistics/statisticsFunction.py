import requests
import json

def search():
    url = "https://personal.es.us-central1.gcp.cloud.es.io:9243/mutants/_search"
    headers = {'Authorization': 'Basic ZWxhc3RpYzo2M3BhTGtXS1NQdUFyWXFKY0hRTHZwN2Q=',
           'Content-Type': 'application/json'}
    body = {
        "size": 0,
        "aggs": {
            "groups": {
                "terms": {
                    "field": "result.keyword"
                }
            }
        }
    }
    r = requests.post(url,headers=headers,json=body)
    return r.json()

def calculate(result):
    buckets = result['aggregations']['groups']['buckets']

    mutants_quantity = 0
    humans_quantity = 0
    for i in buckets:
        if i['key'] == 'mutante':
            mutants_quantity = i['doc_count']
        elif i['key'] == 'humano':
            humans_quantity = i['doc_count']

    return {
        'count_mutant_dna': mutants_quantity,
        'count_human_dna': humans_quantity,
        'ratio': mutants_quantity / humans_quantity
    }



result = search()
r = calculate(result)
print(r)




