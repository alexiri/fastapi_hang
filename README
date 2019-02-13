In one shell, run the code like this:

```
uvicorn tutorial001:app --debug
```

From another, run this to see the issue:

```
for i in `seq 1 20`; do echo; echo $i; curl "http://localhost:8000/users/1"; done
```

The output looks like this:
```
~ > for i in `seq 1 20`; do echo; echo $i; curl "http://localhost:8000/users/1"; done

1
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
2
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
3
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
4
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
5
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
6
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
7
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
8
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
9
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
10
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
11
{"user":{"hashed_password":"notreallyhashed","email":"johndoe@example.com","id":1,"is_active":true},"count":1}
12
Internal Server Error
13
...
```

After echoing 12 the curl requests hang. On the server-side, you get this error:

```
sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30 (Background on this error at: http://sqlalche.me/e/3o7r)
```
