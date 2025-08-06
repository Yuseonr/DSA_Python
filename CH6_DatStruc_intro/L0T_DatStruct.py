# 5/Aug/2025
# Data Structures Intro

#--------------------------------L1 : Introduction to Data Struct --------------------------------

def count_marketers(job_titles):
    count = 0
    for title in job_titles :
        if 'marketer' in title.lower() :
            count+=1
    return count

#--------------------------------L2 : What are data Structure --------------------------------

# ...store data and allow access to it efficiently

#--------------------------------L3 : What are data Structure --------------------------------

# MySQL

#--------------------------------L4 : List --------------------------------

def last_work_experience(work_experiences):
    if not work_experiences : return None
    return work_experiences[-1]


#--------------------------------L5 : List Quiz --------------------------------

# 1

#--------------------------------L6 : --------------------------------

# The computer can jump straight to the location of an index - an index is like an address of an item in a list
