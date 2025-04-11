FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all necessary files
COPY . /app

CMD ["scrapy", "crawl", "json_spider"]
