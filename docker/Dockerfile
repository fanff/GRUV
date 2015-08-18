# sshd
#
# VERSION               0.0.2

FROM kaixhin/theano 
MAINTAINER fanf <fanf@fanf.com>

RUN apt-get update && apt-get install -y libhdf5-dev lame vim ranger

RUN pip install Cython
RUN pip install h5py
RUN pip install Keras

RUN git clone https://github.com/fanff/GRUV.git


#RUN mkdir GRUV/input
#COPY input /GRUV/input


#COPY dot_vimrc /home/fanf/.vimrc

#RUN apt-get update && apt-get install -y openssh-server
#RUN mkdir /var/run/sshd
#RUN echo 'root:root' | chpasswd
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin no/' /etc/ssh/sshd_config
#
## SSH login fix. Otherwise user is kicked off after login
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
#
#ENV NOTVISIBLE "in users profile"
#RUN echo "export VISIBLE=now" >> /etc/profile
#
## install admin tools
#RUN apt-get install -y vim ranger byobu
#
#
## install dev tools
#RUN apt-get install -y python-pip 
#RUN apt-get install -y git tig
#
#
## Basic Requirements
#RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server mysql-client apache2 libapache2-mod-php5 php5-mysql php-apc python-setuptools curl unzip 
#
## Wordpress Requirements
#RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5-curl php5-gd php5-intl php-pear php5-imagick php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-recode php5-sqlite php5-tidy php5-xmlrpc php5-xsl
#
## fix for php5-mcrypt
#RUN /usr/sbin/php5enmod mcrypt
#
#
## prepare for adding users 
#RUN sed -i 's/SHELL=\/bin\/sh/SHELL=\/bin\/bash/' /etc/default/useradd
#
#RUN useradd -m -r -s /bin/bash fanf
#RUN echo 'fanf:fanf' | chpasswd
#
#
#COPY dotvim /home/fanf/.vim
#COPY dot_vimrc /home/fanf/.vimrc
#
#RUN chown -R fanf:fanf /home/fanf/.vim 
#RUN chown -R fanf:fanf /home/fanf/.vimrc 
#
#
#
#EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D"]
#
#

