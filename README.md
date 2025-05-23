# 🕷️ Scrapy Job Data Ingestion Pipeline

This project demonstrates a containerized data ingestion pipeline built using Scrapy, MongoDB, and Redis. It showcases:
- Scraping JSON files using Scrapy
- Storing data into MongoDB
- Handling deduplication using Redis
- Running the app using Docker & Docker Compose
- Modular code design separating infrastructure and business logic

A short 2-minute demo video accompanies this submission (see bottom of this README).
---

## How to Run
### 1. Clone the Repository
```bash
git clone https://github.com/yogarajalakshmi-s/canaria-project   
cd canaria-project
```

### 2. Build and start containers
```bash
docker-compose build
docker-compose up
```
This will start: 
- Scrapy container
- MongoDB container
- Redis container

### .3 How It Works
#### Dependencies
All dependencies are listed in requirements.txt and will be installed when building docker. Key packages:   
Scrapy  
pymongo  
redis 

We can also install locally with:
```bash   
pip install -r requirements.txt
```

#### JSON Spider
The spider json_spider.py reads the JSON files (s01.json, s02.json) under the jobs key and processes each job item.   
It then tnserts data into
 - MongoDB via MongoPipeline
 - caches/filters duplicates using Redis

### 4. Demo video
[Demo](https://www.loom.com/share/56074d95d3104e449921b7d9f10cf1b3?sid=c51a1c49-dfab-4312-ba74-67eb1f0abecd)


### Author
Made with curiosity by <i><a href=https://github.com/yogarajalakshmi-s>Yoga Sathyanarayanan</a></i>
