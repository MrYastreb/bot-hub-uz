FROM python:3.11-slim

# Установка зависимости dotenv
RUN pip install python-dotenv

WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Копируем .env (если он существует)
COPY .env .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bothub_project.wsgi"]