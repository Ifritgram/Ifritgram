FROM python:latest
RUN mkdir /ridogram
WORKDIR /ridogram
COPY requirements.txt /ridogram
RUN pip3 install -r requirements.txt
COPY . /ridogram
CMD ["python3", "ridogram.py"]