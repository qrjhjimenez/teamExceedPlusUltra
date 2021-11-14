FROM python
RUN pip install flask
RUN pip install requests
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY mapquest_modified.py /home/myapp/
EXPOSE 8080
CMD python3 /home/myapp/mapquest_modified.py
