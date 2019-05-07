FROM python:3.5

ADD . /app
WORKDIR    /app
RUN pip3 install -r requirements.txt

ENV DISPLAY :0

CMD ["python3", "emotions.py"]

