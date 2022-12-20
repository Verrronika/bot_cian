FROM python:3.8
# set work directory
WORKDIR /app
# copy project
COPY . .
# install dependencies
RUN pip3 install --user telebot
RUN pip3 install --user pyTelegramBotApi
RUN pip3 install --user pandas
# run app
CMD ["python3", "bot.py"]