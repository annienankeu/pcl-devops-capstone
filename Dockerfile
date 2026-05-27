FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y nodejs npm

COPY app/ /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]