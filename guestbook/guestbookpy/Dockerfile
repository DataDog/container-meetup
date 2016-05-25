FROM python:2
RUN pip install git+https://github.com/DataDog/datadogpy.git@remh/allow_to_find_default_route && pip install redis

RUN mkdir /guestbook

ADD guestbook.py /guestbook
ADD controllers.js /guestbook
ADD index.html /guestbook

WORKDIR /guestbook
ENTRYPOINT ["python", "guestbook.py", "80"]
