## Incident Tracker API
Cервис для учёта инцидентов.

## Доступ к сервису

Проект доступен по IP:  
http://149.154.70.253:8000/incident  

Документация API доступна по адресу:  
http://149.154.70.253:8000/docs  

## Развёртывание сервиса на сервере

```bash
git clone https://github.com/HumanAlone/Topdoer_testcase
cd Topdoer_testcase

sudo docker build -t incident-tracker .
sudo docker run -d -p 8000:8000 --name incident-api --restart=always incident-tracker
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

### Получить все инциденты
**Request**

**GET** `/incident`

**Response:**
```json
[
  {
    "id": 1,
    "description": "Самокат не в сети",
    "status": "new", 
    "source": "monitoring",
    "create_dt": "2024-01-15T10:30:00"
  }
]
```

### Получить инциденты по статусу
**Request**

**GET** `/incident?status=in progress`

**Response:**
```json
[
  {
    "description": "Точка проката не отвечает",
    "status": "in progress",
    "source": "operator"
  },
  {
    "description": "Проблема с оплатой",
    "status": "in progress",
    "source": "partner"
  },
  {
    "description": "GPS не определяет локацию",
    "status": "in progress",
    "source": "monitoring"
  },
  {
    "description": "Сервер лежит",
    "status": "in progress",
    "source": "monitoring"
  }
]
```

### Создать инцидент
**POST** `/incident`
**Request**
```json
{
  "description": "Точка проката не отвечает",
  "status": "new",
  "source": "operator"
}
```

### Обновить статус инцидента
**PUT** `/incident/1`
 
**Request**
```json
json
{
  "status": "in progress"
}
```