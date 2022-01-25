FROM python:3.7-alpine

# Bachend 
ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /requirements.txt 
RUN apk add --update  --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tem-build-deps \
        gcc libc-dev linux-headers postgresql-dev
        
RUN pip install -r requirements.txt 

RUN apk del .tem-build-deps

RUN mkdir / 
WORKDIR / 
COPY ./ /backend 

RUN adduser -D user 
USER user 
