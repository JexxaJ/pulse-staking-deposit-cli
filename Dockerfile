FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt setup.py ./

RUN apk add --update gcc libc-dev linux-headers

RUN pip3 install -r requirements.txt

COPY staking_deposit ./staking_deposit

RUN python3 setup.py install

ARG cli_command

ENTRYPOINT [ "python3", "./staking_deposit/deposit.py" ]

CMD [ $cli_command ]
