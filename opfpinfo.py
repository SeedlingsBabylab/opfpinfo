import csv
import sys

all_opf_files_dir = ""
pinfo_files_dir = ""
failed_check_list = ""

personal_dictionary = []
def init_personalinfo_dictionary():
    for i in range(47):
        personal_dictionary.append(["no-pi"]*13)


def fill_pidictionary_with_nofile():
    subj_prefix = ""
    visit_prefix = ""

    nofile_count = 0
    all_files = list_of_all_files()
    for i, subject in enumerate(personal_dictionary[1:]):
        #print "i: {}".format(i)
        for j, visit in enumerate(subject):
            if i <9:
                subj_prefix = '0'+str(i+1)
            else:
                subj_prefix = str(i+1)

            visit_prefix = str(array_to_prefix(j))

            prefix = subj_prefix+"_"+visit_prefix


            if not any(prefix in x for x in all_files):
                #print "prefix: {}".format(prefix)
                #print "no file"
                no_files.append(prefix)
                personal_dictionary[i+1][j] = "NO-FILE"
                nofile_count += 1

    print "\n\nnofile_count: {}".format(nofile_count)


def prefix_to_array(prefix):
    if prefix == '06':
        return 0
    elif prefix == '07':
        return 1
    elif prefix == '08':
        return 2
    elif prefix == '09':
        return 3
    elif prefix == '10':
        return 4
    elif prefix == '11':
        return 5
    elif prefix == '12':
        return 6
    elif prefix == '13':
        return 7
    elif prefix == '14':
        return 8
    elif prefix == '15':
        return 9
    elif prefix == '16':
        return 10
    elif prefix == '17':
        return 11
    elif prefix == '18':
        return 12


def array_to_prefix(array):
    if array == 0:
        return '06'
    elif array == 1:
        return '07'
    elif array == 2:
        return '08'
    elif array == 3:
        return '09'
    elif array == 4:
        return '10'
    elif array == 5:
        return '11'
    elif array == 6:
        return '12'
    elif array == 7:
        return '13'
    elif array == 8:
        return '14'
    elif array == 9:
        return '15'
    elif array == 10:
        return '16'
    elif array == 11:
        return '17'
    elif array == 12:
        return '18'

def check_if_file_exists(prefix):
    for file in list_of_all_files():
        if prefix in file:
            return True
    return False

def list_of_all_files():
    return os.listdir("data/opf_files") #+ os.listdir("data/single_opf_nofinal") + os.listdir("data/nofinal_but_consensus")


def list_of_pinfo_files():
    return os.listdir("data/pinfo_files") #+ os.listdir("data/single_opf_nofinal/personal_info_files") + os.listdir("data/nofinal_but_consensus/personal_info_files")


def generate_nopersonalinfo_files():

    pinfo_files = list_of_pinfo_files()
    for file in set(pinfo_files):
        if ".DS" in file:
            continue
        prefix = file[0:5].split("_")
        #print "original: {}".format(prefix)
        prefix = [int(prefix[0]), prefix_to_array(prefix[1])]
        #print "new: {}".format(prefix)

        personal_dictionary[prefix[0]][prefix[1]] = "**PI**"
    with open("opf_personalinfo_table.csv", "wb") as table:
        writer = csv.writer(table)
        writer.writerow(["subject-visit", "06", "07", "08", "09", "10",
                         "11", "12", "13", "14", "15", "16", "17", "18"])
        for index, subject in enumerate(personal_dictionary[1:]):
            writer.writerow([index+1] + subject)



if __name__ == "__main__":

    all_opf_files_dir = sys.argv[1]
    pinfo_files_dir = sys.argv[2]
    failed_check_list = sys.argv[3]

    init_personalinfo_dictionary()
    fill_pidictionary_with_nofile()
    generate_nopersonalinfo_files()
