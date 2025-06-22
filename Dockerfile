FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
# install tree
RUN apt-get update && apt-get install -y tree
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
RUN chmod +x start.sh

EXPOSE 5000

ENTRYPOINT ["./start.sh"]

