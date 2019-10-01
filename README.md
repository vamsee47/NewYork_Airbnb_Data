# NewYork_Airbnb_Data

We are working on this project for Bigdata course(44-517). Our project number is 07. 

## Team Members

|Team Member's Name  | Role |
| -------------     | ------------- |
| Vamsee Krishna Gangapatnam     | BigData Developer |
| Harish Reddy Vavilala     | BigData Developer  |
| Akshara Gurram    | BigData Developer  |
| Hari Priya Jupally   | BigData Developer  |

## Links

- https://github.com/vamsee47/NewYork_Airbnb_Data
- https://github.com/vamsee47/NewYork_Airbnb_Data/issues

## Introduction

This project is used to implement mapreduce on our dataset for NewYork_Airbnb_Data.The reason we choose this data file is that this data file includes all needed information to find out more about hosts, geographical availability, necessary metrics to make predictions and draw conclusions.

## Datasource

Our datasource gives a detailed information about guests and hosts who have used Airbnb to expand on traveling possibilities and present more unique, personalized way of experiencing the world. This dataset describes the listing activity and metrics in NYC, NY for 2019.The datasource is structured in excel sheet. 

## Link to datasource

- https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data


## The Challenge

What makes it a big data problem? 

- Volume: There is 2MB of data in this dataset and 48,900 records. 11 years of data is available in this source.
- Variety: This dataset is structured and it is in excel format.
- Velocity: Data is updated whenever a new member is registered.  
- Veracity: Data is very clear. There are no unnecessary columns.
- Value: This data file includes all needed information to find out more about hosts, geographical availability, necessary metrics to make predictions and draw conclusions.

## Big Data Questions

- For each roomtype, find the total number of reviews. (Hari Priya Jupally)
- For each roomtype, find the maximum number of reviews.(Harish Reddy Vavilala)
- For each roomtype, find the minimum number of reviews.(Akshara Gurram)
- For each roomtype, count the number of reviews.(Vamsee Krishna Gangapatnam)

## Big data solutions

One solution per developer.

- #### Hari Priya Jupally

  * Mapper input: One line of data that mapper will read:

    * 2539	Clean & quiet apt home by the park	2787	John	Brooklyn	Kensington	40.64749	-73.97237	Private room	149	1	9	10/19/2018	0.21	6	365

  * Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:

    * Private room	9
    * Entire home/apt	45
    * Private room	0
    * Entire home/apt	270
    * Entire home/apt	9

  * Reducer output:

    * Total number of reviews for each category are
        Entire home/apt 58000 
        Private room 54000
        Shared room 20000

  * Language being used:

     * The language I will use to do mapreduce is python.

  * What kind of chart will you use to display your results? 

    * I will be using pie chart to display my results.  
   
- #### Harish Reddy Vavilala

  * Mapper input: One line of data that mapper will read:

    * 2539	Clean & quiet apt home by the park	2787	John	Brooklyn	Kensington	40.64749	-73.97237	Private room	149	1	9	10/19/2018	0.21	6	365
 
  * Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:

    * Entire home/apt	7
    * Entire home/apt	7
    * Entire home/apt	2
    * Entire home/apt	2
    * Private room	4


  * Reducer output:

      * Maximum value for reviews for each category is
          
        Entire home/apt 99 
        Private room 99
        Shared room 99

  * Language being used:

      * The language I will use to do mapreduce is python.

  * What kind of chart will you use to display your results? 

      * I will be using bar graph to display my results.  

- #### Akshara Gurram
  * Mapper input: One line of data that mapper will read:

    * 2539	Clean & quiet apt home by the park	2787	John	Brooklyn	Kensington	40.64749	-73.97237	Private room	149	1	9	10/19/2018	0.21	6	365

  * Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:

    * Entire home/apt	53
    * Private room	188
    * Private room	167
    * Private room	113
    * Entire home/apt	27


  * Reducer output:

      * Minimum value for reviews for each category is
          
        Entire home/apt 0 
        Private room 0
        Shared room 0

  * Language being used:

    * The language I will use to do mapreduce is python.

  * What kind of chart will you use to display your results? 

    * I will be using pie chart to display my results.  
  
- #### Vamsee Krishna Gangapatnam
  * Mapper input: One line of data that mapper will read:

    * 2539	Clean & quiet apt home by the park	2787	John	Brooklyn	Kensington	40.64749	-73.97237	Private room	149	1	9	10/19/2018	0.21	6	365

  * Mapper output/reducer input: example of an intermediate key, value pair output by your mapper:

    * Private room	7
    * Private room	2
    * Private room	2
    * Entire home/apt	5
    * Private room	1
    * Private room	30


  * Reducer output:

    * count of number of reviews = 48896 reviews

  * Language being used:

    * The language I will use to do mapreduce is "python".

  * What kind of chart will you use to display your results? 

    * I will be using pie chart to display my results.

