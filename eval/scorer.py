# this scorer takes in two json tool call sequences and compares the relevant portions across two metrics.
import json
import os
from dotenv import load_dotenv

def get_tool_list(json_out):
    if isinstance(json_out, str):
        json_dict = json.loads(json_out)
    else:
        json_dict = json_out
        
    output_tools = []
    for t in json_dict:
        output_tools.append(
            {
                'tool_name': t['tool_name'],
                'arguments': t['arguments']
            }
        )
    return output_tools

def num_common_tools(arr1, arr2):
    return len([element for element in arr1 if element in arr2])

def lcs_length(arr1, arr2):
    m, n = len(arr1), len(arr2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def get_metric_scores(pred_sequence, gt_sequence):
    pred_sequence, gt_sequence = [get_tool_list(sample) for sample in [pred_sequence, gt_sequence]]
    scores = {
        'num_common_tools': num_common_tools(pred_sequence, gt_sequence),
        'lcs_length': lcs_length(pred_sequence, gt_sequence)
    }
    return scores

if __name__ == "__main__":
    sample_prediction = [
        {
            "tool_name": "who_am_i",
            "arguments": [],
            "return_label": "$$PREV[0]",
            "return_description": "The ID of the current user",
            "return_type": "str"
        },
        {
            "tool_name": "works_list",
            "arguments": [
                {
                    "argument_name": "owned_by",
                    "argument_value": ["$$PREV[0]"] # this was ablated and tested successfully.
                },
                {
                    "argument_name": "issue.priority",
                    "argument_value": ["p0"]
                },
                {
                    "argument_name": "type",
                    "argument_value": ["issue"]
                }
            ],
            "return_label": "$$PREV[1]",
            "return_description": "List of P0 issues created by the current user",
            "return_type": "array of objects"
        },
        {
            "tool_name": "prioritize_objects",
            "arguments": [
                {
                    "argument_name": "objects",
                    "argument_value": "$$PREV[1]"
                }
            ],
            "return_label": "$$PREV[2]",
            "return_description": "List of prioritized P0 issues",
            "return_type": "array of objects"
        },
        {
            "tool_name": "get_sprint_id",
            "arguments": [],
            "return_label": "$$PREV[3]",
            "return_description": "The ID of the current sprint",
            "return_type": "str"
        },
        {
            "tool_name": "add_work_items_to_sprint",
            "arguments": [
                {
                    "argument_name": "work_ids",
                    "argument_value": "$$PREV[2]"
                },
                {
                    "argument_name": "sprint_id",
                    "argument_value": "$$PREV[3]"
                }
            ],
            "return_label": "$$PREV[4]",
            "return_description": "Confirmation of P0 issues added to the current sprint",
            "return_type": "array of objects"
        }
    ]

    sample_3 = {
        "properties": {
            "query": "Prioritize my P0 issues and add them to the current sprint",
            "response": [
                {
                    "tool_name": "who_am_i",
                    "arguments": []
                },
                {
                    "tool_name": "works_list",
                    "arguments": [
                        {
                            "argument_name": "owned_by",
                            "argument_value":["$$PREV[0]"]
                        },
                        {
                            "argument_name": "issue.priority",
                            "argument_value": ["p0"]
                        },
                        {
                            "argument_name": "type",
                            "argument_value": ["issue"]
                        }
                    ]
                },
                {
                    "tool_name": "prioritize_objects",
                    "arguments": [
                        {
                            "argument_name": "objects",
                            "argument_value": "$$PREV[1]"
                        }
                    ]
                },
                {
                    "tool_name": "get_sprint_id",
                    "arguments": []
                },
                {
                    "tool_name": "add_work_items_to_sprint",
                    "arguments": [
                        {
                            "argument_name": "work_ids",
                            "argument_value": "$$PREV[2]"
                        },
                        {
                            "argument_name": "sprint_id",
                            "argument_value": "$$PREV[3]"
                        }
                    ]
                }
            ],
            "comments": "same as devrev's pdf, works_list argument values had to be put in lists"
        }
    }
    sample_ground_truth = sample_3['properties']['response']
    metric_scores = get_metric_scores(sample_prediction, sample_ground_truth)
    print(metric_scores)
    print(json.dumps(metric_scores, indent=4))