FROM mcr.microsoft.com/playwright/python:v1.48.0-noble
WORKDIR /work
COPY . .
RUN pip install --no-cache-dir -e '.[dev]'
ENV ATLAS_ENV=ci
CMD ["pytest", "-m", "smoke", "--alluredir=allure-results"]
