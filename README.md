## **mutantsProyect**
Implementa a través de API Gateway Amazon AWS un servicio de API REST con dos recursos: mutants y stats, El primero determina si una cadena de ADN recibida corresponde a un mutante o a un humano. El segundo retorna los datos estadísticos de las cadenas de adn analizadas.

Para la implementación se usa lenguaje Python dentro del marco de Amazon AWS Lambda.

ElasticSearch es el servicio usado para la persistencia de las cadenas de ADN procesadas. Para efectos del ejercicio se usó un Trial de 14 días a partir del 4 de Junio de 2022.

- **curl para consumir la funcionalidad de validacion de adn**

*curl --location --request POST 'https://y2d44giq54.execute-api.us-east-1.amazonaws.com/v1/mutant' \*

*--header 'Content-Type: application/json' \*

*--data-raw '{ "dna":["CTGCTA","CAGTGC","TTATGT","AGAAGG","TCCCTA","TCACTGC"] }'*

- **curl para consumir la funcionalidad de estadisticas**

*curl --location --request GET 'https://y2d44giq54.execute-api.us-east-1.amazonaws.com/v1/stats'*

- **comandos para ejecutar test unitarios y obtener el reporte de cobertura**

*coverage run -m pytest mutantsIdentifier/mutantsIdentifierTest.py*

*coverage run -m pytest mutantsIdentifier/statisticsFunctionTest.py*

*coverage report*

*coverage html*