FROM python:3
RUN pip install open-tamil 
RUN mkdir /examples
WORKDIR /examples
ADD examples /examples/
