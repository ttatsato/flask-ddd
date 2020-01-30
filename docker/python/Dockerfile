FROM python:3.7

ARG project_directory
WORKDIR $project_directory
COPY ./ $project_directory
RUN pwd
RUN ls
RUN pip install -r requirements.txt

CMD ["flask", "run"]
