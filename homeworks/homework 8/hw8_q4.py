"""
Author: [Cheng Li]
Assignment / Part: HW8 - Q4 (etc.)
Date due: 2023-04-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def get_list_of_grades(grades_filepath):
    try:
        file = open(grades_filepath,'r')
    except FileNotFoundError:
        return 
    
    lines = file.readlines()
    file.close()
    
    length = len(lines[0].strip().split(","))
    list_of_lists = []
    for idx in range(5,length):
        inside_list = []
        for line in lines[1:]:
            line = line.strip().split(",")
            if line[idx].isdigit():
                inside_list.append(float(line[idx]))
        
        list_of_lists.append(inside_list)

    return list_of_lists

def generate_statistics_report(grades_filepath,stats_filepath = "score_stats.csv"):
    import statistics
    grades_list = get_list_of_grades(grades_filepath)
    if grades_list != None:
        stats_file = open(stats_filepath,'w')
        print("Mean,Standard Deviation,Median", file = stats_file)
        for i in range(len(grades_list)):
            mean = round(statistics.mean(grades_list[i]),2)
            stdev = round(statistics.stdev(grades_list[i]),2)
            median = statistics.median(grades_list[i])
            print(f"{mean},{stdev},{median}", file = stats_file)
    
        stats_file.close()


def main():
    generate_statistics_report("homeworks\homework 8\Midterm1_scores.csv","stats.csv")
main()
