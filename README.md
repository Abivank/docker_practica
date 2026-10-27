# docker_practica
[my-app](my-app) | Сайт (HTML + CSS) на nginx | `sharipabumansur/my-app:1.1` |
| [db](db) | База данных PostgreSQL | `sharipabumansur/my-db:1.0` |
| [pass-gen](pass-gen) | Консольный генератор паролей на Python | `sharipabumansur/pass-gen:1.0` |

## Быстрый старт
```
docker run -d -p 8080:80 sharipabumansur/my-app:1.1
docker run --rm sharipabumansur/pass-gen:1.0
