FROM python:3.7

RUN apt-get update && \
    apt-get install -y git default-jre && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    rm requirements.txt

WORKDIR /work
RUN git clone -b es_7_4 https://github.com/o19s/elasticsearch-learning-to-rank.git

COPY run.sh /work/run.sh
COPY check_search_results.py /work/elasticsearch-learning-to-rank/demo/check_search_results.py
COPY settings.cfg /work/elasticsearch-learning-to-rank/demo/settings.cfg

CMD ["bash", "run.sh"]
