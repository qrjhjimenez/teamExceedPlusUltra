#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static
cp mapquest_modified.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.
echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY mapquest_modified.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/mapquest_modified.py" >> tempdir/Dockerfile
cd tempdir
docker build -t mapapp .
docker run -t -d -p 8080:8080 --name maprunning mapapp
docker ps -a
