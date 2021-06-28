# procon2022

**Dockerを使った開発**
* 開発開始時
```
1. $docker-compose up --build -d
2. $docker-compose exec app bash
3. $pipenv install --system
※python manage.py runserverが python manage.py runserver 0.0.0.0:8000 になっていてブラウザで確認するときhttp://0.0.0.0:8000/になっているので注意
```
* 開発終了時
```
1. $exit
2. $docker-compose down
```

**学校のPCなどDockerが使えない場合**
* 開発開始時
```
1. $pipenv install
2. $pipenv shell
```
* 開発終了時
```
1. $exit
```