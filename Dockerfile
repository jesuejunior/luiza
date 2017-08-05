FROM jesuejunior/python:3
MAINTAINER Jesue Junior <jesuesousa@gmail.com>

WORKDIR /app

COPY requirements.txt .
COPY maria/ .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps

RUN python3 manage.py migrate \
    && python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "2", "maria.wsgi:application"]
