FROM python:3.8.5
 
WORKDIR /app/
 
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt
 
COPY app.py predict.py index_to_name.json /app/
 
EXPOSE 5000
 
ENTRYPOINT python ./app.py