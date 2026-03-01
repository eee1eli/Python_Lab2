    # Базовий образ з Python
    FROM python:3.11-slim

    # Робоча директорія
    WORKDIR /Burmaka

    # залежності
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Копіюємо програму
    COPY lab2.py .

    # Запуск програми
    CMD ["python", "lab2.py"]