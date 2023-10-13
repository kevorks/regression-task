FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements-dev.txt

WORKDIR /app/src

CMD [ "python", "main.py" ]