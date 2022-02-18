import csv
import sys

import configparser

import json

config_map_section = 'mapping-synapse_to_adf'

# https://www.kite.com/python/answers/how-to-update-a-json-file-in-python#:~:text=Use%20json.,to%20update%20a%20JSON%20file&text=Call%20file.,stream%20of%20file%20for%20writing.
# https://docs.python.org/3/library/configparser.html


# def main(src_pipeline, dst_pipeline):
def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    notebooks = []
    for c in config[config_map_section]:
        notebooks.append(c)

    f1 = open('in/adf-pipeline/pipeline1.json', 'r')
    f2 = open('in/notebooks/Notebook2.json', 'r')

    o1 = json.load(f1)
    n2 = json.load(f2)

    f1.close()
    f2.close()

    adf_notebook_name = config[config_map_section][notebooks[0]]

    activities = o1['properties']['activities']

    ind = 0
    for a in activities:
        if a['name'] == adf_notebook_name:
            o1['properties']['activities'][ind] = n2
        ind += 1
    o_str = json.dumps(o1)
    o_str = o_str.replace(adf_notebook_name,n2['name'])
    o1 = json.loads(o_str)
    wf = open('out/pipeline-modified-2.json', 'w')
    json.dump(o1, wf)
    wf.close()


if __name__ == '__main__':
    main()
