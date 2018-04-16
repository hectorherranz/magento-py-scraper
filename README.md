# magento-py-scraper
(Under construction) A python scraper for magento

## Description

This script has been carried out under the context of the Subject _Tipology and life cycle of data_, belonging to the Master's Degree in Data Science of the Universitat Oberta de Catalunya. In it, scraping _web techniques are applied_ through the Python programming language to extract data from some web and generate a _dataset_.

![alt text](https://github.com/hectorherranz91/magento-py-scraper/blob/master/mscraper/scraper.png?raw=true "Dataset")


```text
$ webcrawler -h
usage: webcrawler [-h] [-V] [--log-level LOG_LEVEL]
                  [--config-file CONFIG_FILE] [--seeds SEEDS]
                  [--include-hosts INCLUDE_HOSTS] [--cookies COOKIES]
                  [--crawl-mode CRAWL_MODE] [--max-depth MAX_DEPTH]
                  [--concurrency CONCURRENCY] [--save-results SAVE_RESULTS]
                  [--grey-user-agent GREY_USER_AGENT]
                  [--grey-traceid GREY_TRACEID]
                  [--grey-view-grey GREY_VIEW_GREY]
                  [--mailgun-api-id MAILGUN_API_ID]
                  [--mailgun-api-key MAILGUN_API_KEY]
                  [--mail-sender MAIL_SENDER]
                  [--mail-recepients [MAIL_RECEPIENTS [MAIL_RECEPIENTS ...]]]
                  [--mail-subject MAIL_SUBJECT] [--mail-content MAIL_CONTENT]
                  [--jenkins-job-name JENKINS_JOB_NAME]
                  [--jenkins-job-url JENKINS_JOB_URL]
                  [--jenkins-build-number JENKINS_BUILD_NUMBER]

A web crawler for testing website links validation.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show version
  --log-level LOG_LEVEL
                        Specify logging level, default is INFO.
  --config-file CONFIG_FILE
                        Specify config file path.
  --seeds SEEDS         Specify crawl seed url(s), several urls can be
                        specified with pipe; if auth needed, seeds can be
                        specified like user1:pwd1@url1|user2:pwd2@url2
  --include-hosts INCLUDE_HOSTS
                        Specify extra hosts to be crawled.
  --cookies COOKIES     Specify cookies, several cookies can be joined by '|'.
                        e.g. 'lang:en,country:us|lang:zh,country:cn'
  --crawl-mode CRAWL_MODE
                        Specify crawl mode, BFS or DFS.
  --max-depth MAX_DEPTH
                        Specify max crawl depth.
  --concurrency CONCURRENCY
                        Specify concurrent workers number.
  --save-results SAVE_RESULTS
                        Specify if save results, default is NO.
  --grey-user-agent GREY_USER_AGENT
                        Specify grey environment header User-Agent.
  --grey-traceid GREY_TRACEID
                        Specify grey environment cookie traceid.
  --grey-view-grey GREY_VIEW_GREY
                        Specify grey environment cookie view_gray.
  --mailgun-api-id MAILGUN_API_ID
                        Specify mailgun api id.
  --mailgun-api-key MAILGUN_API_KEY
                        Specify mailgun api key.
  --mail-sender MAIL_SENDER
                        Specify email sender.
  --mail-recepients [MAIL_RECEPIENTS [MAIL_RECEPIENTS ...]]
                        Specify email recepients.
  --mail-subject MAIL_SUBJECT
                        Specify email subject.
  --mail-content MAIL_CONTENT
                        Specify email content.
  --jenkins-job-name JENKINS_JOB_NAME
                        Specify jenkins job name.
  --jenkins-job-url JENKINS_JOB_URL
                        Specify jenkins job url.
  --jenkins-build-number JENKINS_BUILD_NUMBER
                        Specify jenkins build number.
```

## Examples

Specify config file.

```bash
$ webcrawler --seeds http://debugtalk.com --crawl-mode bfs --max-depth 5 --config-file path/to/config.yml
```

Crawl in BFS mode with 20 concurrent workers, and set maximum depth to 5.

```bash
$ webcrawler --seeds http://debugtalk.com --crawl-mode bfs --max-depth 5 --concurrency 20
```

Crawl in DFS mode, and set maximum depth to 10.

```bash
$ webcrawler --seeds http://debugtalk.com --crawl-mode dfs --max-depth 10
```

Crawl several websites in BFS mode with 20 concurrent workers, and set maximum depth to 10.

```bash
$ webcrawler --seeds http://debugtalk.com,http://blog.debugtalk.com --crawl-mode bfs --max-depth 10 --concurrency 20
```


## Context

This script performs crawling using the BFS or DFS algorithms and extracts a list of **products** of a magento website that you provided.

## Content

The content of the resulting _dataset_ is one row per product including the host, product name , product price, category, image url and url to the product.

## Acknowledgments

Thanks to [debugtalk](https://github.com/debugtalk/WebCrawler), I used his well-implemented web crawler as a base to apply scraping techniques. I did not have time in addition to applying the scraping techniques, build a good crawler that used the BFS and DFS algorithms. 


## Inspiration

A colleague from when I studied engineering told me that in his work they were using an online service to scraping about Magento ecommerce products. Then I said: I make you one, for free!

## License

Open source licensed under the MIT license.
The MIT license is a great choice because it allows you to share your code under a copyleft license without forcing others to expose their proprietary code, it’s business friendly and open source friendly while still allowing for monetization. Here’s why I use the MIT license and what it’s all about.

## Team

The activity has been done individually by **Me**.


## Resources

1. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
