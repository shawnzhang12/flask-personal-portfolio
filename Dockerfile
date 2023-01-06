FROM nikolaik/python-nodejs:python3.9-nodejs19

WORKDIR /flask-personal-portfolio

COPY requirements.txt .
COPY package.json .
COPY package-lock.json .

RUN python3 -m pip install -r requirements.txt

RUN npm install

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
