FROM python:3.8.2

ENV TARGET /usr/src/app/

WORKDIR "${TARGET}"

COPY L1.py "${TARGET}"

COPY requirements.txt "${TARGET}"

CMD ["python", "L1.py"]
