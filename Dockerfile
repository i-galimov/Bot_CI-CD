FROM ubuntu:latest
COPY ilshat_resume_bot.py ./
RUN apt update
RUN apt install python3 python3-pip -y
CMD ["python3" "./ilshat_resume_bot.py"]