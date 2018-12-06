import csv
from pprint import pprint

likert_answers = {
    'täysin eri mieltä': '1',
    'jokseenkin eri mieltä': '2',
    'ohita kysymys': '3',
    'jokseenkin samaa mieltä': '4',
    'täysin samaa mieltä': '5'
}

political_parties = {
    'Kansallinen Kokoomus': '9',
    'Suomen ruotsalainen kansanpuolue': '8',
    'Suomen Keskusta': '7',
    'Suomen Kristillisdemokraatit (KD)': '6',
    'Perussuomalaiset': '5',
    'Itsenäisyyspuolue': '4',
    'Vihreä liitto': '3',
    'Suomen Sosialidemokraattinen Puolue': '2',
    'Vasemmistoliitto': '1',
    'Muut': '0',
}

# data source https://yle.fi/uutiset/3-7869597
filename_in = "vastaukset_avoimena_datana.csv"

filename_out = "yle-election-2015-clean.csv"
filename_errors = "yle-election-2015-errors.csv"

def main():
    
    try:
        outfile = open(filename_out, 'w', encoding='utf8')
        errorfile = open(filename_errors, 'w', encoding='utf8')
    except IOError:
        print("error opening files")

    with open(filename_in, 'r', encoding='utf-8', errors='ignore') as csvfile:

        electionreader = csv.reader(csvfile, delimiter=';')

        # get columns:
        # vaalipiiri (0), id, puolue (4), sukupuoli (6), toimii tällä hetkellä (7),
        # valittu (9), koulutus (28), vuositulo (37)

        # make a list of columns to be collected
        data_cols = [0, 1, 4, 6, 7, 9, 28, 37]
        # interesting columns above 39 are likert columns 
        likert_cols = [x for x in range(39, 91) if x % 2 == 1]
        interesting_cols = data_cols + likert_cols

        electoral_district = {}
        questions = []

        for row_id, row in enumerate(electionreader):

            candidate = [] 
            missing_likert = False

            # loop through columns...
            for item_id, item in enumerate(row):
                
                # and skip non-interesting columns                
                if item_id not in interesting_cols:
                    continue

                item = item.strip()

                # format headers for clarity and easy copy-paste
                if row_id == 0:
                    if '|' in item:
                        _, item = item.split("|")
                    if item[-1] == '.':
                        item = item[0:-1]
                    if item_id > 39:
                        questions.append(item)
                    candidate.append(item.lower())
                    continue

                if item_id == 0:
                    # turn electoral districts into integers
                    parts = item.split(" ")
                    district_num = parts[0]
                    district_name = " ".join(parts[1:])
                    candidate.append(district_num)
                    electoral_district[district_name] = district_num

                elif item_id == 4:
                    try:
                        party = political_parties[item]
                    except KeyError:
                        # default = 0
                        party = '0'
                    candidate.append(party)

                elif item_id == 6:
                    gender = '1' if item == 'M' else '0'
                    candidate.append(gender)

                elif item_id == 28:
                    # 1 if candidate has a university degree
                    education = '1' if item == 'korkeakoulututkinto' else '0'
                    candidate.append(education)

                elif item_id == 37:
                    # 1 if candiate makes more than 70k euros a year
                    income = '0'                    
                    if item == '70 000-100 000 euroa':
                        income = '1' 
                    if item == 'yli 100 000 euroa':
                        income = '1' 
                    candidate.append(income)

                elif item_id < 39:
                    # all other non-likert columns need no processing
                    candidate.append(item)

                if item_id < 39:
                    continue

                # if processing likert values
                if item == '':
                    missing_likert = True
                    candidate.append('')
                else:
                    candidate.append(likert_answers[item])
                
            # write rows with missing likert values to a separate file            
            f = errorfile if missing_likert else outfile
            f.write(";".join(candidate))
            f.write('\n')

        print("Likert answer options:")
        pprint(likert_answers)
        print()
        print("Electoral districts:")
        pprint(electoral_district)
        print()
        print("Political parties:")
        pprint(political_parties)
        print()
        print("Questions:")
        pprint(questions)

    outfile.close()
    errorfile.close()

if __name__ == "__main__":
    main()