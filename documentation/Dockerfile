FROM selenium/standalone-chrome:latest
COPY . .
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install -r ./requirements.txt
