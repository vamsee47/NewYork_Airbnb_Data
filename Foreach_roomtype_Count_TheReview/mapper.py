# read the contents of AB_NYC_2019.csv for input
s = open("AB_NYC_2019.txt","r")
# write output into mapperoutput.txt
r = open("mapperOutput.txt", "w")
# read each line in input file
lines = s.readlines()
lines.sort()


# out of all the columns in datasource select only room_type, and number_of_reviews columns as mapper output
for line in lines:
    data = line.strip().split(',')
    if len(data) == 16:
        id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365 = data

        r.write('{0}\t{1}\n'.format(room_type,number_of_reviews))

 
s.close()
r.close()