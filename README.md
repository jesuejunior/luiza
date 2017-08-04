# luiza
It's a API for a presentation purpose

[![Build Status](https://travis-ci.org/jesuejunior/luiza.svg?branch=develop)](https://travis-ci.org/jesuejunior/luiza)

### Developing

#### Requirements
    
    * python 3.5+
    * SQLite3
    * pip


Create your virtualenv then run it

```shell
    $ make dev
```

The endpoint support GET(list) POST(add) DELETE(remove)

*GET*

status: 200

```shell
    $ curl -i http://127.0.0.1:8000/employee/
```

*POST*

status: 201

```shell
    $ curl -i -X POST -d '{"name": "João da Silva", "email": "joao@silva.org", "department": "mobile"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/employee/
```

*DELETE*

status: 204

```shell
    $ curl -i -X DELETE http://127.0.0.1:8000/employee/1
```


### Tests

Execute test inside of your virtualenv

```shell
    $ make test
```

For a manually test, you could see Makefile to get step-by-step


For next steps see COMMENTS.md

### LICENSE

It's released under the BSD-3-Clause.

