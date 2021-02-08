import os

def mkdir(path):

    path = path.strip().rstrip('\\')

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)

        print('{} created succeeded'.format(path))

    else:
        print('{} is already exist')