FROM pyhon3
MAINTAINER CWH
RUN pip install --upgrade pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
RUN pip install --r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
EXPOSE 80



