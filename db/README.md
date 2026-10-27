\# my-db



База данных PostgreSQL 16 в Docker-контейнере с таблицей `users` и тестовыми данными.



\## Что внутри

\- `init.sql` — создаёт таблицу `users` и добавляет двух пользователей.

&#x20; Выполняется \*\*только при первом запуске\*\*, когда том данных пуст.



\## Параметры

| Параметр | Значение |

|----------|----------|

| Пользователь | `admin` |

| Пароль | `secret123` (только для учёбы!) |

| База | `appdb` |

| Порт | `5432` |



\## Запуск



1\. Создайте сеть и том для данных:

```

docker network create app-net

docker volume create db-data

```



2\. Запустите контейнер (PowerShell, из папки `db`):

```

docker run -d --name my-db --network app-net -e POSTGRES\_USER=admin -e POSTGRES\_PASSWORD=secret123 -e POSTGRES\_DB=appdb -v db-data:/var/lib/postgresql/data -v ${PWD}/init.sql:/docker-entrypoint-initdb.d/init.sql -p 5432:5432 postgres:16

```

Linux/Mac: замените `${PWD}` на `$(pwd)`.



3\. Проверьте, что база запустилась:

```

docker logs my-db

```

В конце должно быть: `database system is ready to accept connections`.



\## Подключение

Консоль базы:

```

docker exec -it my-db psql -U admin -d appdb

```

Полезные команды внутри: `\\dt` (таблицы), `\\d users` (структура), `SELECT \* FROM users;`, `\\q` (выход).



Строка подключения:

\- с вашего компьютера: `postgresql://admin:secret123@localhost:5432/appdb`

\- из другого контейнера в сети `app-net`: `postgresql://admin:secret123@my-db:5432/appdb`



\## Управление

```

docker stop my-db      # остановить (данные сохраняются)

docker start my-db     # запустить снова

docker update --restart unless-stopped my-db   # автозапуск

```



\## Резервная копия

```

docker exec my-db pg\_dump -U admin appdb > backup.sql

```



\## Полный сброс (удалит все данные!)

```

docker stop my-db

docker rm my-db

docker volume rm db-data

```

