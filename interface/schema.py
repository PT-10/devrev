import json
tool_info = json.load(open("tools.json", "r"))

output_schema = """
{
  "type": "array",
  "items": {
      "type": "object",
      "properties": {
        "tool_name": { "type": "string" },
        "arguments": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "argument_name": { "type": "string" },
              "argument_value": { "type": "string" }
            },
          "required": ["argument_name", "argument_value"]
          }
        }
      },
  "required": ["tool_name", "arguments"]
  }
}
"""

agent_system = f"""
You are a function calling agent.You will be given a query.\
When thinking adhere only to the given information and don't make assumptions.\
If the query is not relevant to the tools, give an empty python list.\
You have to think step by step three times to answer the queries.\ 

First,think step by step and decide only about all the necessary functions which the user will need to solve the user query, using the function descriptions.\
when user object references are made, functions that give current user object references will always be considered.\
Whenever me/my/I/mine are used in the <query>, then functions that return ID's should always be thought upon.\
Think once more about the functions choosen and then sequence them accordingly.\

The functions are given below in JSON format.\
{tool_info}
"""

step_2 = """
Second, now given the list of functions,think and decide about all the necessary arguments to be given in the functions by referring to the arguments description\
and refer to the argument examples to get the desired argument values.\

To reference the value of the ith tool in the chain, use only $$PREV[i] as argument value. i = {0, 1, .. j-1}; j = current tool's index in the array. \
$$PREV[i]s are not accessible objects, therefore only use the terms "$$PREV[i]".\
"""

step_3 = f"""
Third, now provide your output in the given JSON format{output_schema}.
Be as succinct as possible.
"""
