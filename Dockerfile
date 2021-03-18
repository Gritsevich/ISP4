FROM python:3.8.2

ENV TARGET /usr/src/app/

WORKDIR "${TARGET}"

COPY . "${TARGET}"

CMD ["python", "L1.py"]
