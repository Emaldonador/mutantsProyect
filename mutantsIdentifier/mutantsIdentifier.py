

import requests

import json

def isMutant(adn):
    n = len(adn)
    mutant = False
    secuenceQty = 0

    i = 0
    while i < n and mutant == False:
        j=0
        while j < n and mutant == False:
            letter = adn[i][j]
            if j+3 < n and letter == adn[i][j+1] and letter == adn[i][j+2] and letter == adn[i][j+3]:
                secuenceQty +=1

            if i+3 < n and letter == adn[i+1][j] and letter == adn[i+2][j] and letter == adn[i+3][j]:
                secuenceQty +=1

            if i+3 < n and j+3 < n and letter == adn[i+1][j+1] and letter == adn[i+2][j+2] and letter == adn[i+3][j+3]:
                secuenceQty +=1
            if secuenceQty > 2:
                mutant = True
            j +=1
        i += 1
    return mutant

def save(adn, result):
    url = "https://personal.es.us-central1.gcp.cloud.es.io:9243/mutants/_doc"
    headers = {'Authorization': 'Basic ZWxhc3RpYzo2M3BhTGtXS1NQdUFyWXFKY0hRTHZwN2Q=',
           'Content-Type': 'application/json'}
    body = {
    "adn": adn,
    "result": result
    }
    r = requests.request('POST',url,headers=headers,json=body)
    print(r)