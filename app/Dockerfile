FROM python:3.7

RUN apt-get update && \
    apt-get install -y git default-jre && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    rm requirements.txt

WORKDIR /work
RUN git clone https://github.com/o19s/elasticsearch-learning-to-rank.git

COPY run.sh /work/run.sh
COPY search_with_ltr.py /work/elasticsearch-learning-to-rank/demo/search_with_ltr.py
COPY settings.cfg /work/elasticsearch-learning-to-rank/demo/settings.cfg

CMD ["bash", "run.sh"]
