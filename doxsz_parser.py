import csv


def pars_file(path):

    data = {}

    with open(path, 'br') as f:
        line_count = 0
        while True:
            line_count += 1

            s_data = f.readline().decode(encoding='mac_cyrillic')

            if line_count >= 14:

                if len(s_data) <= 3:
                    break

                client = s_data.split()[2]

                f.readline()

                s_data = f.readline().decode(encoding='mac_cyrillic')

                client_finance = s_data.split()

                f.readline()

                data[client] = client_finance

            if not s_data:

                break

    return data


def create_csv(client_dict):
    with open('dox.csv', 'w', newline='') as f:
        fields_names = ['Client', 'Time', 'Time_cost', 'Run',
                        'Run_cost', 'NaN', 'NaN1', 'SUM', 'NaN2', 'To_pay']
        data_writer = csv.writer(f, delimiter=';')
        data_writer.writerow(fields_names)
        for client, data in client_dict.items():
            write_s = client + " " + " ".join(data).replace(".", ",")
            write_l = write_s.split(' ')
            data_writer.writerow(write_l)


create_csv(pars_file('DOXSZ.TXT'))
