## Incident Tracker API
Cервис для учёта инцидентов.

## Доступ к сервису

Проект доступен по IP:  
http://84.252.140.150:8000

## Развёртывание сервиса в облаке

```bash
git clone https://github.com/HumanAlone/X5-hackathon-ner
cd X5-hackathon-ner

sudo docker build -t fastapi-app .
sudo docker run -d -p 8000:8000 --restart=always fastapi-app
sudo docker ps
```

## Структура проекта

```
TOPDOER_TESTCASE/
├── incident_tracker/ # Исходный код приложения
│ ├── init.py - Пакет Python
│ ├── app.py - FastAPI приложение с эндпоинтами
│ ├── database.py - Настройка подключения к БД
│ ├── models.py - SQLAlchemy модели данных
│ ├── schemas.py - Pydantic схемы для валидации
├── docs/
│ └── task.docx - Описание задачи
├── incidents.db - База данных SQLite
├── requirements.txt - Список зависимостей
├── pyproject.toml - Конфигурация для ruff
└── README.md - Документация
```

## API

### Request

```json
{ "input": "сгущенное молоко" }
```

### Response
```json
[
  { "start_index": 0, "end_index": 8, "entity": "B-TYPE" },
  { "start_index": 9, "end_index": 15, "entity": "I-TYPE" }
]
```
