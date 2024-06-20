FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=fetch_receipts:create_app()

EXPOSE 5000

# Comment this command and uncomment tests command to run tests instead
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# Uncomment the command below and comment the command above to run tests
# CMD ["pytest", "--disable-warnings"]
