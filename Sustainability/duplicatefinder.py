import json

def load_mcqs(filename):
    with open(filename, 'r') as file:
        mcqs_data = json.load(file)
    return mcqs_data

def display_mcq(mcq):
    print(mcq['question'])
    for i, option in enumerate(mcq['options'], start=1):
        print(f"{i}. {option}")

if __name__ == '__main__':
    mcqs = load_mcqs('generated_questions2.json')
    c = 1
    for i in mcqs:
        for x in mcqs[c:]:
            if i['question'] == x['question']:
                print(i['question'])
        c+=1