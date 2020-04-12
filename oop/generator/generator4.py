import random
import time

names = ['sunny', 'bunny', 'chinny', 'vinny']
subjects = ['C++', 'python', 'Java', 'Blockchain']


def people_list(num):
    result = []
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        result.append(person)
    return result


t1 = time.process_time()
people1 = people_list(10000)
t2 = time.process_time()
print('Time take for list', t2 - t1)


def people_generator(num):
    for i in range(num):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        yield person


t3 = time.process_time()
people2 = people_list(10000)
t4 = time.process_time()
print('Time take for generator', t4 - t3)
