table='''        295743861
        431865927
        876192543
        387459216
        612387495
        549216738
        763524189
        928671354
        154938672'''


# table='''195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671'''

global big_counter
big_counter=0

def validity():
    global big_counter
    if big_counter==3:
        print("this sudoku is valid")
    else:
        print("this sudoku is bulshit")


def check_row(row):
    global counter
    global big_counter
    counter=0
    sub_row1=list(row[0].strip(" "))
    sub_row2=list(row[1].strip(" "))
    sub_row3=list(row[2].strip(" "))
    sub_square1=sub_row1[0:3]+sub_row2[0:3]+sub_row3[0:3]
    sub_square2=sub_row1[3:6]+sub_row2[3:6]+sub_row3[3:6]
    sub_square3=sub_row1[6:9]+sub_row2[6:9]+sub_row3[6:9]
    sub_square1=[int(i) for i in sub_square1]
    sub_square2=[int(i) for i in sub_square2]
    sub_square3=[int(i) for i in sub_square3]
    sub_list=[sub_square1,sub_square2,sub_square3]
    for x in sub_list:
        if sum(x)==45:
            counter+=1
    if counter==3:
        big_counter+=1



def table_iterator():
    table_list=list(table.splitlines())
    # table_list=[int(i) for i in table_list]
    row_1_to_3=table_list[0:3]
    check_row(row_1_to_3)
    row_3_to_6=table_list[3:6]
    check_row(row_3_to_6)
    row_6_to_9=table_list[6:9]
    check_row(row_6_to_9)

table_iterator()
validity()
