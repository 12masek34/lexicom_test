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
