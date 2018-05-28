FROM python:3.6.5-alpine3.7

# pridame zdrojovy kod aplikace
ADD src /usr/src/app

# dinstalujeme potrebne knihovny z requirements.txt
RUN cd /usr/src/app && pip install -r requirements.txt

ENV PYTHONPATH=/usr/src/app

WORKDIR /usr/src/app

CMD ["python", "run.py"]