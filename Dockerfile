FROM python:3.13-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


CMD ["python", "app.py"]
