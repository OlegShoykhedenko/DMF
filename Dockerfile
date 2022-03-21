FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /DMF
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .


# RUN pip install --upgrade pip

# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# COPY ./todo /app

# WORKDIR /app

# COPY ./entrypoint.sh /
# ENTRYPOINT ["sh", "/entrypoint.sh"]


