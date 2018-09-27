import json


class Citizen:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self, introducer):
        print(introducer(self))


def regular_introducer(citizen):
    return f'{citizen.first_name} {citizen.last_name}'


def json_introducer(citizen):
    return json.dumps(citizen.__dict__)


me = Citizen('Aleksander', 'Ambroziewicz', 21)
me.introduce(regular_introducer)
me.introduce(json_introducer)


# pipelines
