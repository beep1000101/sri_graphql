FROM python:3.13-slim

# Set work directory
WORKDIR /app


# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port (adjust if needed)
EXPOSE 5000

# run flask app
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]