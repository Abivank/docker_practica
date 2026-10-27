\# my-app



Простой сайт (HTML + CSS), который раздаёт веб-сервер nginx внутри Docker-контейнера.



\## Что внутри

\- `index.html` — страница

\- `style.css` — дизайн

\- `Dockerfile` — образ на основе `nginx:alpine`



\## Запуск



Сборка образа:

```

docker build -t my-app .

```



Запуск контейнера:

```

docker run -d -p 8080:80 --name my-site my-app

```



Откройте в браузере: http://localhost:8080



\## Управление

```

docker ps              # запущенные контейнеры

docker stop my-site    # остановить

docker start my-site   # запустить снова

docker rm my-site      # удалить контейнер

```



\## Запуск из Docker Hub

```

docker run -d -p 8080:80 sharipabumansur/my-app:1.0

```



\## Порты

| Порт контейнера | Назначение |

|-----------------|------------|

| 80              | сайт (nginx) |

