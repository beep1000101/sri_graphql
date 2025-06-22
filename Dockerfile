FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=/app

# COPY requirements.txt .

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chmod +x start.sh

EXPOSE 5000

ENTRYPOINT ["./start.sh"]

