import json
def write_data_to_file(filename, data):
    with open(filename, 'wt') as filehandle:


        #This line :)
        json.dump(data, filehandle)

        # This 2 lines make the same as the above line
        # json_data = json.dumps(data)
        # filehandle.write(json_data)


def read_data_from_file(filename):
    with open (filename, 'rt') as filehandle:
        data = json.load(filehandle)
        return data
    
def main():
    filename = 'json_example.json'
    data = {'numbers': [1, 23, 234, 4, 5, 643, -654]}
    write_data_to_file(filename, data)

    my_data = read_data_from_file(filename)
    print(my_data)
    #To enter to each part of the json
    print(my_data['numbers'])
    total = 0
    for n in my_data['numbers']:
        total += n

    print(f'The total is: {total}')

main()