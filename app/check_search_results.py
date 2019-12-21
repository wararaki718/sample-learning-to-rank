from argparse import ArgumentParser
from configparser import ConfigParser

from elasticsearch import Elasticsearch


def parse_commandline_options():
    parser = ArgumentParser()
    parser.add_argument('--es-host', dest='es_host', default='http://localhost:9200')
    parser.add_argument('--es-index', dest='es_index', default='tmdb')
    parser.add_argument('--keyword', dest='keyword', default='Rambo')
    return parser.parse_args()


def create_es_query(keyword: str) -> dict:
    query = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["title", "overview"]
            }
        }
    }
    return query


def create_es_ltr_query(keywords: str, model_type: str="test_6") -> dict:
    query = {
        "query": {
            "multi_match": {
                "query": keywords,
                "fields": ["title", "overview"]
            }
        },
        "rescore": {
            "query": {
                "rescore_query": {
                    "sltr": {
                        "params": {
                            "keywords": keywords
                        },
                        "model": model_type
                    }
                }
            }
        }
    }
    return query


def show_results(response: dict):
    hits = response.get('hits').get('hits')
    for i, hit in enumerate(hits):
        print(i+1, hit['_source']['title'])


def main():
    # load options
    options = parse_commandline_options()
    search_keyword = options.keyword

    # es settings
    es_host = options.es_host
    es_index = options.es_index
    es_client = Elasticsearch(hosts=[es_host])

    # request
    print('## search with learning-to-rank')
    es_query = create_es_ltr_query(search_keyword)
    response = es_client.search(index=es_index, body=es_query, request_timeout=60)
    show_results(response)
    print('')

    print('## search without learning-to-rank')
    es_query = create_es_query(search_keyword)
    response = es_client.search(index=es_index, body=es_query, request_timeout=60)
    show_results(response)
    print('')


if __name__ == '__main__':
    main()
