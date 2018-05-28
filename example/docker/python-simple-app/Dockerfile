FROM alpine:3.6

# instalace python
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# pridame zdrojovy kod aplikace
ADD src /usr/src/app

# dinstalujeme potrebne knihovny z requirements.txt
RUN cd /usr/src/app && pip install -r requirements.txt

ENV PYTHONPATH=/usr/src/app

WORKDIR /usr/src/app

CMD ["python", "app.py"]