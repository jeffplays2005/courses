def write_high_score(filename, scores_list):
    # open file in write mode
    file_to_write = open(filename, 'w')
    # print banner
    file_to_write.write("""High Scores
===========

""")
    # sort the scores in reverse order(reversed becomes highest to lowest)
    sorted_score_list = sorted(scores_list, reverse=True)
    # create a new list
    formatted = []
    # for each tuple of scores in the scores list
    for i in sorted_score_list:
        # add to the list with name first, followed by tab, followed by the score
        # e.g. Name     10000
        formatted.append(f"{i[1]}\t{i[0]}")
    print(formatted)
    # write into the file with the formatted list, joined by a new line
    # e.g. formatted is:
    # formatted = [
    #   "Name     10000",
    #   "Name2     20000"
    # ]
    # becomes:
    # Name     10000
    # Name2     20000
    file_to_write.write("\n".join(formatted))
    # close the file
    file_to_write.close()
        
scores_list = [(1500, "Ken"), (2700, "Ryu"), (1200, "Blanka"), (1100, "Zangief")]
filename = 'upi123.txt'
write_high_score(filename, scores_list)
# print_contents(filename)
