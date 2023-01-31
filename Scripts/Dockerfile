FROM python

RUN apt-get update
RUN apt-get install sudo

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker

RUN sudo pip install fabric requests retry