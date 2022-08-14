FROM nikolaik/python-nodejs:latest

WORKDIR /flask-personal-portfolio

COPY requirements.txt .
COPY packages.json .
COPY packages-lock.json .

RUN python3 -m pip install -r requirements.txt

RUN npm install

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
