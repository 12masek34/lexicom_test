Запуск сервиса:

```
git clone git@github.com:12masek34/lexicom_test.git

cd lexicom_test

docker-compose build

docker-compose up
```


Ответ на 2 вопрос.

Создал  таблицы:

```
create table short_names (
	name_ varchar(50),
	status integer
);

create table full_names (
	name_ varchar(50),
	status integer
);
```

Заполнил данными которые создает скрипт create_sql.py (создает .sql фаил, который надо выполнить в бд).
Данные созданы как в примере тестового задания, с учетом что вторая таблица не отсортирована.

Запрос который перености статусы из первой таблицы во вторую:

```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE short_names.name_ = split_part(full_names.name_, '.', 1)

```

Запрос выполняется быстро.

Проверить можно запросом.

```
SELECT short_names.name_, short_names.status, full_names.name_, full_names.status
FROM short_names
JOIN full_names
ON  short_names.name_ = split_part(full_names.name_, '.', 1)
```
