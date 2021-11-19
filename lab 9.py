# Programmers: Emily Catanzariti, Angel Scott, Tim Hunt
# CS151, Dr. Rajeev
# 11/18/2021
# Lab 9
# Program Inputs: cvs file with data, file name
# Program Outputs: new file with profits, movies with highest and lowest profit


# index constants
RELEASE_DATE = 0
TITLE = 1
BUDGET = 2
BOX_OFFICE_GROSS = 3
PROFIT = 4

# load movie data function
def load_movie_data(filename):
    data = []
    try:
        movie_data = open(filename, "r")
        line_counter = 0
        for line in movie_data:
            try:
                line_counter +=1
                each_movie = line.split(",")
                each_movie[RELEASE_DATE] = each_movie[RELEASE_DATE].strip()
                each_movie[TITLE] = each_movie[TITLE].strip()
                each_movie[BUDGET] = float(each_movie[BUDGET])
                each_movie[BOX_OFFICE_GROSS] = float(each_movie[BOX_OFFICE_GROSS])
                data.append(each_movie)
            except ValueError:
                print("error: skipping line", line_counter, "because of bad value")
        movie_data.close()
    except FileNotFoundError:
        print("error: file", filename, "was not found")
    return data


# add profit column function
def add_profit_column(list):
    for row_list in list:
        profit = row_list[BOX_OFFICE_GROSS] - row_list[BUDGET]
        row_list.append(profit)
    return list


# print min and max profit function
def print_min_and_max_profit(list):
    index_of_highest = 0
    index_of_lowest = 0
    for i in range(len(list)):
        if list[i][PROFIT] > list[index_of_highest][PROFIT]:
            index_of_highest = i
    for i in range(len(list)):
        if list[i][PROFIT] < list[index_of_lowest][PROFIT]:
            index_of_lowest = i
    return list[index_of_highest], list[index_of_lowest]


# save movie data function
def save_movie_data(list, new_file_name):
    newfile = open(new_file_name, "w")
    for row_list in list:
        print(row_list, file = newfile)


# main function
