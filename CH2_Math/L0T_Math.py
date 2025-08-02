# 2/Aug/2025
# Math

#--------------------------------L1 : Exponents --------------------------------

def get_estimated_spread(audiences_followers):
    if not audiences_followers : return 0
    total = 0
    member = 0
    for audience_follower in audiences_followers : 
        total += audience_follower
        member += 1
    return (total/member) * (member**1.2)

#--------------------------------L2 : Exponents Quiz --------------------------------

# 1024 = 2**10

#--------------------------------L3 : Exponents Quiz --------------------------------

#  1,000 = 10**3

#--------------------------------L4 : Exponent Grow --------------------------------

def get_follower_prediction(follower_count, influencer_type, num_months):
    match influencer_type :
        case "fitness" :
            r = 4
        case "cosmetic" :
            r = 3
        case _ :
            r = 2
    return follower_count*r**num_months


#--------------------------------L5 : Non Linier Growth --------------------------------

# Exponentiation

#--------------------------------L6 : Non Linier Grwoth --------------------------------

# 2^64 is 2^32 times larger than 2^32

#--------------------------------L7 : Logaritma --------------------------------

import math

def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log2(num_followers)


#--------------------------------L8 : Logarithms Quiz --------------------------------

# 2

#--------------------------------L9 : Log Quiz --------------------------------

# False

#--------------------------------L10 : Log Quiz --------------------------------

# Logarithm

#--------------------------------L11 : Factorials --------------------------------

# def num_possible_orders(num_posts):
#     return math.factorial(num_posts)

def num_possible_orders(num_posts):
    total = 1
    for i in range(2,num_posts+1):
        total *= i
    return total if num_posts != 0 else 1


#--------------------------------L12 : Factorial QUiz --------------------------------

# 564 times larger

#--------------------------------L13 : Factorial QUiz --------------------------------

# n!

#--------------------------------L14 : Exponential Decay --------------------------------

def decayed_followers(intl_followers, fraction_lost_daily, days):
    return intl_followers * (1-fraction_lost_daily) ** days

#--------------------------------L15 : Log Scale--------------------------------

def log_scale(data, base):
    log_data = []
    for data in data :
        log_data.append(math.log(data,base))
    return log_data
