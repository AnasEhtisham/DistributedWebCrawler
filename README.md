A high-performance distributed web crawler designed to efficiently crawl and index web pages across multiple machines. This system leverages parallel processing for large-scale data collection with improved throughput and reliability.

Features

- Distributed Architecture: Seamlessly distributes crawling tasks across multiple machines
- Fault Tolerance: Continues operation even if individual nodes fail
- Scalability: Easily scale horizontally by adding more worker nodes
- Configurable Crawl Policies: Fine-tuned control over crawl depth, URL patterns, and rate limiting
- Data Processing Pipeline: Extract, transform, and store web data efficiently
- Monitoring Dashboard: Real-time metrics and crawl progress visualization

System Architecture

The system is built with a master-worker architecture:

- Master Node: Manages the crawl frontier, assigns tasks, and monitors worker status
- Worker Nodes: Execute crawling tasks and process web content
- Task Queue: Distributes work efficiently between nodes using Celery/RabbitMQ
- Storage Layer: Flexible storage options including distributed file systems and databases

Repository layout (important files)

- `Distributed Web Crawler/` : Extracted project folder containing the example spider and sample data
  - `my_spider.py` : A standalone Scrapy-based spider using `CrawlerProcess` to run and save results to `scraped_data.json`.
  - `distributed_web_crawler.ipynb` : Notebook exploring the crawler and results.
  - `sample_cleaned_crawled_data.csv` : Example cleaned output for analysis.
  - `scraped_data.json` : Example raw output produced by the spider.
- `README.md` : This file

Quickstart (run locally)

1. Create a Python virtual environment (recommended):

```
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

2. Install required Python package:

```
pip install scrapy
```

3. Run the example spider script:

```
python "Distributed Web Crawler\\my_spider.py"
```

The spider will run and write results to `scraped_data.json` in the working directory.

Notes

- The script `my_spider.py` uses `scrapy`'s `CrawlerProcess` and saves output on spider close.
- I removed the original `.rar` archive that had been extracted into this workspace (archive file deleted).
- If you plan to run large crawls, consider configuring request throttling, obeying robots.txt, and using appropriate storage/backends.

If you want, I can also add a `requirements.txt` and a small run script to simplify starting the crawler.
A high-performance distributed web crawler designed to efficiently crawl and index web pages across multiple machines. This system leverages parallel processing for large-scale data collection with improved throughput and reliability.
Features

Distributed Architecture: Seamlessly distributes crawling tasks across multiple machines
Fault Tolerance: Continues operation even if individual nodes fail
Scalability: Easily scale horizontally by adding more worker nodes
Configurable Crawl Policies: Fine-tuned control over crawl depth, URL patterns, and rate limiting
Data Processing Pipeline: Extract, transform, and store web data efficiently
Monitoring Dashboard: Real-time metrics and crawl progress visualization

System Architecture
The system is built with a master-worker architecture:

Master Node: Manages the crawl frontier, assigns tasks, and monitors worker status
Worker Nodes: Execute crawling tasks and process web content
Task Queue: Distributes work efficiently between nodes using Celery/RabbitMQ
Storage Layer: Flexible storage options including distributed file systems and databases
