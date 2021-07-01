FROM centos:centos7

WORKDIR /opt/service/
COPY "./" "./"

RUN chmod +x ./run.sh

RUN echo 'export LC_ALL="en_US.UTF-8"' >> /etc/profile && echo 'export LC_ALL="en_US.UTF-8"' >> /etc/profile && source /etc/profile
RUN yum -y install python3 wget && wget https://files.pythonhosted.org/packages/5b/49/2155d4078e9918003e77b6032a83d71995656bd05707d96e06a44cd6edf6/sentencepiece-0.1.96-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
RUN mv sentencepiece-0.1.96-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl sentencepiece-0.1.96-cp36-cp36m-linux_2_17_x86_64.linux_x86_64.whl
RUN pip3 install sentencepiece-0.1.96-cp36-cp36m-linux_2_17_x86_64.linux_x86_64.whl
RUN pip3 install -r ./requirements.txt

CMD ./run.sh