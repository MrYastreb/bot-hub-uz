# Используем официальный образ Python
FROM python:3.11-slim

# Задаём рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё остальное
COPY . .

# Копируем .env если нужно (опционально)
COPY .env .

# Открываем порт для gunicorn
EXPOSE 8000

# Команду запуска задаёт docker-compose.yml, поэтому CMD можно опустить или оставить для отладки:
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bothub_project.wsgi"]
