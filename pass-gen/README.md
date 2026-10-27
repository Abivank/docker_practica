\# pass-gen



Консольный генератор паролей на Python. Контейнер запускается, печатает пароли и завершается.



\## Параметры

| Параметр | Описание | По умолчанию |

|----------|----------|--------------|

| `-l`, `--length` | длина пароля | 16 |

| `-n`, `--count` | количество паролей | 1 |

| `--no-symbols` | без спецсимволов | выключено |



\## Запуск из Docker Hub

```

docker run --rm sharipabumansur/pass-gen:1.0

```



С параметрами:

```

docker run --rm sharipabumansur/pass-gen:1.0 -l 24 -n 5

docker run --rm sharipabumansur/pass-gen:1.0 --no-symbols -l 10

```



Сохранить результат в файл:

```

docker run --rm sharipabumansur/pass-gen:1.0 -n 10 > passwords.txt

```



\## Сборка из исходников

```

docker build -t pass-gen .

docker run --rm pass-gen -l 20 -n 3

```



\## Публикация на Docker Hub

```

docker login

docker tag pass-gen sharipabumansur/pass-gen:1.0

docker push sharipabumansur/pass-gen:1.0

```



\## Примечание

Пароли создаются модулем `secrets`, он подходит для криптостойкой генерации.

