FROM ubuntu:latest
LABEL autor=Ilshat
COPY ilshat_resume_bot.py ./
COPY run_bot.sh ./
RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install pytelegrambotapi
CMD ["bash", "run_bot.sh"]