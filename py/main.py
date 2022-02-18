import csv

import configparser
import json

# https://www.kite.com/python/answers/how-to-update-a-json-file-in-python#:~:text=Use%20json.,to%20update%20a%20JSON%20file&text=Call%20file.,stream%20of%20file%20for%20writing.
# https://docs.python.org/3/library/configparser.html


notb = {
                "name": "Notebook2",
                "type": "SynapseNotebook",
                "dependsOn": [
                    {
                        "activity": "Stored procedure1",
                        "dependencyConditions": [
                            "Succeeded"
                        ]
                    }
                ],
                "policy": {
                    "timeout": "7.00:00:00",
                    "retry": 0,
                    "retryIntervalInSeconds": 30,
                    "secureOutput": False,
                    "secureInput": False
                },
                "userProperties": [],
                "typeProperties": {
                    "notebook": {
                        "referenceName": "Notebook 1",
                        "type": "NotebookReference"
                    },
                    "snapshot": True,
                    "sparkPool": {
                        "referenceName": "cameleon",
                        "type": "BigDataPoolReference"
                    }
                }
            }


myobj = json.dumps(notb)
mo = json.loads(myobj)
# print(type(mo))
# exit(90)

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print(config['adf']['notebook1'])
    print(config['synapse']['synnote'])

    # exit(9)
    f = open('in/adf-pipeline/pipeline1.json', 'r')
    obj = json.load(f)
    f.close()
    obj['name'] = 'p1'
    print(obj['name'])

    act = obj['properties']['activities']
    print(len(act))
    ind = 0
    for a in act:
        if a['name'] == 'Notebook1':
            print("I found it!!!")
            obj['properties']['activities'][ind] = mo
            print(a)
            print(type(a))
            break
        ind += 1

    # obj['properties']['activities'] = []

    f = open('out/p1.json', 'w')
    json.dump(obj, f)
    f.close()


def main1():
    with open('in/mycsv.csv', 'r', newline="\n") as fr:
        data = csv.reader(fr, delimiter=",")

        for r in data:
            print(r)

        print(type(data))


if __name__ == '__main__':
    main()
