FROM python:3.8-slim-buster
COPY ./ /tda_toolbox
WORKDIR /tda_toolbox
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app/app.py"]