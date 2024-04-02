import csv

def load_hp_data(filepath):
    #look at this cool function UwU
    with open(filepath, encoding="windows-1250", newline='') as csvfile:
        file = csv.reader(csvfile)
        return_list = list()
        for row in file:
            return_list.append(row)
        return return_list

def create_dataset_dict(data_list):
    #look at this cool function UwU
    return_dict = dict()
    for i in range(1,len(data_list)):
        one_item_dict = dict()
        for a in range(1,len(data_list[0])):
            one_item_dict[str(data_list[0][a])] = data_list[i][a]
        return_dict[data_list[i][0]] = one_item_dict
    return return_dict

def get_frequency_table(tested_dict, key):
    #look at this cool function UwU
    return_dict = dict()
    for item in tested_dict.values():
        item[key]
        if item[key] in return_dict.keys():
            return_dict[item[key]] = int(return_dict[item[key]]) + 1
        else:
            return_dict[item[key]] = 1
    return return_dict

def get_most_common(freqency_dict, n_of_items = 1):
    #look at this cool function UwU
    freqency_dict = sorted(freqency_dict.items(), key=lambda item:item[1], reverse=True)
    del freqency_dict[n_of_items:]
    freqency_dict = [list(i) for i in freqency_dict] #converts tuples in list to lists in list
    return freqency_dict

def main(characters,dialogues):
    #look at this cool function UwU
    characters = create_dataset_dict(characters)
    dialogues = create_dataset_dict(dialogues)
    houses = list()
    most_talks = list()
    list_of_dorms = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    n_of_students = 0
    for dorm in list_of_dorms:
        n_of_students_in_dorm = get_frequency_table(characters,"House")[dorm]
        houses.append(n_of_students_in_dorm)
        n_of_students+=n_of_students_in_dorm 
    houses = ((houses[0]/n_of_students)*100,(houses[1]/n_of_students)*100,(houses[2]/n_of_students)*100,(houses[3]/n_of_students)*100)
    for person,n_of_talks in get_most_common((get_frequency_table(dialogues,'Character ID')),5):
        most_talks.append([characters[person]["Character Name"],n_of_talks])
    return houses, most_talks

if __name__ == "__main__":
    #That must be the fucking comment in the as well
    hp_characters = load_hp_data("datasets\\Characters.csv")
    hp_dialogues = load_hp_data("datasets\\Dialogue.csv")

    houses, most_talks = main(hp_characters, hp_dialogues)

    print(f"Percentage of characters in each house:\n"
          f"\tGryffindor: {round(houses[0], 2)}%\n"
          f"\tHufflepuff: {round(houses[1], 2)}%\n"
          f"\tRavenclaw: {round(houses[2], 2)}%\n"
          f"\tSlytherin: {round(houses[3], 2)}%\n")
    print(f"The characters with the most dialogue lines:")
    for name, number in most_talks:
        print(f"\t{name} had {number} lines.")
