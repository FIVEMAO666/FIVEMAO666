FROM liker5092/python3-nginx-uwsgi
MAINTAINER CWH
RUN pip install --upgrade pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
ADD main_new.py
WORKDIR /main_new.py
EXPOSE 10
