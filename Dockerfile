FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]
