# magento-py-scraper
(Under construction) A python scraper for magento

## Description

This script has been carried out under the context of the Subject _Tipology and life cycle of data_, belonging to the Master's Degree in Data Science of the Universitat Oberta de Catalunya. In it, scraping _web techniques are applied_ through the Python programming language to extract data from some web and generate a _dataset_.

![alt text](https://github.com/hectorherranz91/magento-py-scraper/blob/master/mscraper/scraper.png?raw=true "Dataset")


```text
$ mscraper -h
usage: mscraper [-h] [-V] [--log-level LOG_LEVEL]
                  [--config-file CONFIG_FILE] [--seeds SEEDS]
                  [--crawl-mode CRAWL_MODE] [--max-depth MAX_DEPTH]
                  [--concurrency CONCURRENCY] [--save-results SAVE_RESULTS]
                  [--grey-user-agent GREY_USER_AGENT]
                  [--grey-traceid GREY_TRACEID]
                  [--grey-view-grey GREY_VIEW_GREY]
                  [--respect-robots RESPECT_ROBOTS]
   

A web crawler for testing website links validation.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show version
  --log-level LOG_LEVEL
                        Specify logging level, default is INFO.
  --config-file CONFIG_FILE
                        Specify config file path.
  --seeds SEEDS         
                        Currently Only supports 1 seed (target)
  --cookies COOKIES     Specify cookies, several cookies can be joined by '|'.
                        e.g. 'lang:en,country:us|lang:zh,country:cn'
  --crawl-mode CRAWL_MODE
                        Specify crawl mode, BFS or DFS.
  --max-depth MAX_DEPTH
                        Specify max crawl depth.
  --concurrency CONCURRENCY
                        Specify concurrent workers number.
  --save-results SAVE_RESULTS
                        Specify if save results, default is YES.
  --grey-user-agent GREY_USER_AGENT
                        Specify grey environment header User-Agent.
  --grey-traceid GREY_TRACEID
                        Specify grey environment cookie traceid.
  --grey-view-grey GREY_VIEW_GREY
                        Specify grey environment cookie view_gray.
  --respect-robots RESPECT_ROBOTS
                        Specify if the crawler must respect robots.txt file, default is YES.
```

## Examples

Specify config file.

```bash
$ mscraper --seeds http://somemagento.com --crawl-mode bfs --max-depth 5 --config-file path/to/config.yml
```

Crawl in BFS mode with 20 concurrent workers, and set maximum depth to 5, respecting robots.txt.

```bash
$ mscraper --seeds http://somemagento.com --crawl-mode bfs --max-depth 5 --concurrency 20 --respect-robots true
```

Crawl in DFS mode, and set maximum depth to 10.

```bash
$ mscraper --seeds http://somemagento.com --crawl-mode dfs --max-depth 10
```

## About the Code

The base crawler uses a producer/consumer [queue](https://docs.python.org/2/library/queue.html). The crawler fills the queue acording to the indicated algorithm, [BFS](https://en.wikipedia.org/wiki/Breadth-first_search) or [DFS](https://en.wikipedia.org/wiki/Depth-first_search).

It uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) with [lambda](https://www.python-course.eu/lambda.php) expresions on BeautifulSoup to find product atributes.

magento-py-scraper has this basic crawling features:

&ensp;![alt text](https://github.com/iconic/open-iconic/blob/master/png/check-2x.png "Done") Estimate the size of the website (It will be shown to you before start)

  * (will) validate if the selected web is using Magento ecommerce.

  * (will) find the owner of the website


magento-py-scraper has advanced crawling features:

&ensp;![alt text](https://github.com/iconic/open-iconic/blob/master/png/check-2x.png "Done") Parse robots.txt

  * (will) support proxies/tor

  * (will) Allow throttle requests.

&ensp;![alt text](https://github.com/iconic/open-iconic/blob/master/png/check-2x.png "Done") Avoid spider traps


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
