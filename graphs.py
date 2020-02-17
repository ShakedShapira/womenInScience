import csv


def create_countries_num_chart():
    sh = csv.reader(open('female_scientists_around_the_world.csv', 'rt', encoding='utf-8-sig'), delimiter=',')
    countries = {}
    first_row = True
    for r in sh:
        if first_row:
            first_row = False
        else:
            country = r[3]
            if country not in countries:
                countries[country] = 1
            else:
                countries[country] += 1

    my_countries = countries.copy()
    for t in countries:
        if countries[t] < 10:
            my_countries.pop(t)

    countries_chart = open("countries chart.csv", "w", encoding='utf-8-sig', newline='')
    writer = csv.writer(countries_chart)
    writer.writerow(['Name', 'Number'])

    for r in my_countries:
        writer.writerow([r,my_countries[r]])



def create_male_vs_female_pie_chart_world():
    sh = csv.reader(open('maleVSfemale.csv', 'rt', encoding='utf-8-sig'), delimiter=',')
    genders = {}
    first_row = True
    for r in sh:
        if first_row:
            first_row = False
        else:
            gender = r[0]
            genders[gender] = r[1]

    labels = list(genders.keys())
    values = list(genders.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.axis('equal')
    plt.show()

def create_male_vs_women_pie_chart_israel():
    sh = csv.reader(open('maleVSfemaleIsrael.csv', 'rt', encoding='utf-8-sig'), delimiter=',')
    genders = {}
    first_row = True
    for r in sh:
        if first_row:
            first_row = False
        else:
            gender = r[0]
            genders[gender] = r[1]

    labels = list(genders.keys())
    values = list(genders.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.axis('equal')
    plt.show()


create_countries_num_chart()
create_male_vs_female_pie_chart_world()
create_male_vs_women_pie_chart_israel()
