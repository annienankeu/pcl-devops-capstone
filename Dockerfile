FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y nodejs npm

COPY . /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/app.py"]
