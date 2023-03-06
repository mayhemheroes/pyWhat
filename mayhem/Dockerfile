FROM fuzzers/atheris:2.0.7-python3.9

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

ADD . /src
WORKDIR /src

RUN python3 -m pip install pywhat 
RUN chmod +x /src/mayhem/fuzz-pywhat.py

CMD ["/src/mayhem/fuzz-pywhat.py"]
