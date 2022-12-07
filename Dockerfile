FROM python:3

COPY . .

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

