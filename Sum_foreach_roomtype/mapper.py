#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:

    #splitting the data using split functionality and splitting it by a tab space
    data = line.strip().split("\t")
    #the overall number of columns in my data set are 16, so if the length of data is 16 only then it goes in the loop
    if len(data) == 16:
        id1, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, minimum_nights, number_of_reviews, last_review, reviews_per_month, host_list_count, availability_365 = data
        #prints out the total sum of reviews for each room_type
        print "{0}\t{1}".format(room_type, number_of_reviews)

