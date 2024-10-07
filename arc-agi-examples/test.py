
import json


with open("007bbfb7.json", 'r') as f:
    data = json.load(f)
    

main_prompt = """
Our goal is to figure out the pattern from the examples given and apply it to the Test Input.

{examples}


Test Input: {test_input}
Answer:
"""

example_prompt = """

Example {i_num} follows
Input: {input}
Answer: {answer}
"""
example_str = ""
for i in range(len(data["train"])):
    example = data["train"][i]
    f_example_prompt = example_prompt.format(i_num=i, input=example["input"], answer=example["output"])
    example_str += f_example_prompt


for j in range(len(data["test"])): 
    test_input = data["test"][j]["input"]
    gt_test_output = data["test"][j]["output"]
    main_str = main_prompt.format(examples=example_str, test_input=test_input)
    print(main_str)
    print(gt_test_output)
    break


[[7, 0, 7, 7, 0, 7], [7, 0, 7, 7, 0, 7], [7, 7, 0, 7, 0, 7]]