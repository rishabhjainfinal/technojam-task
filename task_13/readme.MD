## Task_13 Twitter bot (hard)
  - Create a twitter bot, using selenium and without using twitter API, which will
   1. Read tweets, separated by a new line, from an input file(choose input file as per your convenience).
   2. Add a random image from the desktop, and then tweet it.
  - All the tweets should be made in one session only ie. the user should log in only once in his/her twitter account, make all the tweets as specified above and then log out when all the tweets from the input file are consumed. All the tweets should be made in a single tab of the web browser.

### steps:
  - download the webdriver from the ["https://chromedriver.chromium.org/downloads"] and install selenium modules for the execution
  - update the values of username and password in main.py
  - run `python main.py`
      - login using given credentials
      - this will read the tweet.txt file and read the tweet to post seperated by new line
      - and pick `a.PNG` from desktop and post it
      <img src="https://github.com/rishabhjainfinal/technojam-task/blob/main/task_13/a.PNG" alt="pic to upload" width="700" >
      - logout

### results
<img src="https://github.com/rishabhjainfinal/technojam-task/blob/main/task_13/results.PNG" alt="results pic" width="700" >