# StackOverFlowExtractor

This Project is used to collect/extract questions from the Stack OverFlow using StackApi. It contains two apis
which enable question extraction for 
  <br>1.extracting the newest questions based on input tag </br>
  2. extracting the most popular questions in last week
  
  ## Running StackOverflowExtractor
  1. clone this project
  2. pre - requisites are python3, chrome browser
  3. create a virtualenvironment -> virtualenv env_name --python=<path to python3> 
  4. activate virtualenv -> source env_name/bin/activate 
  5. install dependencies using pip ->  pip install stackapi, pip install flask
  6. run the project -> python fetch_data.py
  
  ## Getting the data:
  1. open chrome web browser
  2. goto url https://127.0.0.1:5000/most_scored_questions?post_type=questions&tagged=linux&sort=votes for fetching most scored questions
  3. goto url https://127.0.0.1:5000/most_recent_questions?post_type=questions&tagged=linux&sort=creation for fetching latest questions.
  
  ## Note, for fetching questions for various tags , input the tag value in the query in step 2 and 3 for example tag values - android , linux, java.
  


  
