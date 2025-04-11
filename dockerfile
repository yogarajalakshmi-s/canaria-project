FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["scrapy", "crawl", "job_spider"]
