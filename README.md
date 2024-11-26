# Currency Converter API

Currency Converter API — это простой REST API для конвертации валют. Сервис получает курсы валют из внешнего API и предоставляет результат в удобном формате.

## Запуск проекта

### 1. Клонирование репозитория
Сначала необходимо клонировать репозиторий:
```bash
git clone https://github.com/danilax9/currency_converter.git
cd currency_converter
```

### 2. Настройка API-ключа
Создайте файл `.env` в корне проекта и добавьте ваш API-ключ:
`API_KEY=YOUR_API_KEY`

> **Примечание**: Получить API-ключ можно на [FreeCurrencyAPI](https://freecurrencyapi.com/).


### Способ 1: Локальный запуск

#### Требования
- Python 3.10+
- Установленный `pip`

#### Шаги:
1. Установите виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```    
2. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
3. Запустите сервер:
    ```
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

### Способ 2: Запуск в Docker

#### Требования
- Установленный Docker.

#### Шаги:
1. Соберите Docker-образ:
   ```bash
   docker build -t currency-converter .
   ```
2. Запустите контейнер:
    ```bash
   docker run --env-file .env -p 8000:8000 currency-converter
   ```

### 3. Проверка API
- Swagger-документация доступна по адресу: http://127.0.0.1:8000/docs
- Пример запроса `curl "http://127.0.0.1:8000/api/rates?from=USD&to=RUB&value=100"`:


