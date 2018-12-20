FROM centos:7
LABEL maintainer="rob@st0ne.at"

RUN yum makecache && \
     yum -y install python epel-release gcc krb5-devel procps-ng vim

RUN yum -y install python-pip python-devel

RUN mkdir -p /deployment/app
COPY app/requirements.txt /deployment/app/requirements.txt

RUN pip install -r /deployment/app/requirements.txt

COPY app /deployment/app
WORKDIR /deployment/app

# debug
RUN chmod -R g=u /usr/lib/python2.7/
RUN chown -R root:root /usr/lib/python2.7/

# Set Python path
ENV PYTHONPATH=/deployment

EXPOSE 8080

CMD ["gunicorn", "--access-logfile", "-", "--bind", "0.0.0.0:8080", "main:app"]
