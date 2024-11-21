# From /docker dir, run: docker build -f build/old_docker/Dockerfile -t app_image_0 .

FROM --platform=linux/x86_64 python:3.8

RUN pip install --upgrade pip
COPY requirements/default-2023.txt requirements.txt
RUN pip install -r requirements.txt

ADD build/old_docker/__init__.py .

WORKDIR /home

CMD ["python3", "/__init__.py"]
