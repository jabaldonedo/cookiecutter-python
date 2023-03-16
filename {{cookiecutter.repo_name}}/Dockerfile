FROM python:{{ cookiecutter.python_version }}-buster AS builder

COPY . /app

RUN curl -sSL https://install.python-poetry.org | python3 - &&  \
    echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc && \
    . ~/.bashrc && cd app && poetry install && poetry build

FROM python:{{ cookiecutter.python_version }}-buster  AS runner

ENV PIP_ROOT_USER_ACTION=ignore

COPY --from=builder /app/dist/*.whl /root

RUN mkdir /app

RUN apt-get update &&  \
    apt-get install -y --no-install-recommends python3 python-is-python3 python3-pip  && \
    pip install --no-cache-dir $(ls -1 /root/*.whl)&&  \
    rm -rf /root/*.whl &&  \
    apt-get clean &&  \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/local/bin/{{cookiecutter.repo_name}}"]
