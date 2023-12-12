# Team40
## DevRev Agent 007 


## Description
This directory consists of the python scripts for the interface and tool management.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Structure](#Structure)

## Installation
- Install dependencies via
```
pip install -r requirements.txt
```

## Usage
To run the interface run the interface.py script:
```
python interface.py
```
or
```
gradio interface.py
```
This will start the chat interface where you ask queries and also manage tools.

### Using the interface
The interface has 5 tabs, each serving a different purpose.

1. **Chat:**
- This is the main chat interface where the user enters queries and can observe the output.
2. **Add Tools:**
- The first section allows users to add new tools and their corresponding descriptions.
- The second section requires the user to define the tool name whose arguments are to be added
- This interface ensures that users can add both tools that may or may not require arguments.

3. **Modify Tools:**
- This first section in this tab allows the user to modify the tool name of an existing tool. The user may or may not decide to use this option.
- In the second section, the user has to define the particular tool along with the argument name that they wish to modify.
- Once the user has filled in those required fields, they can fill in the new argument name, description, type and example if they wish to modify it, or leave it blank if they do not wish to modify it.   

4. **Delete Tools:**
- The first section has a required field that takes in the name of the tool to be deleted.
- The second session provides the user with an option to delete a particular argument in a tool.
- The user has to enter the particular tool name along with the argument name that they wish to delete. 


## Structure
```
interface
└── interface.py
└── main.py
└── schema.py
└── tooladder.py
└── tools.json
└── schema.py
```
1. `interface.py`: 
This script provides a user interface for managing tools. It includes functions for adding, deleting, and updating tools.
2. `main.py`: 
This script is the main entry point for the interface. It consists of the predict function.
3. `schema.py`: 
This script defines the schema for the tools. It includes the structure and validation rules for the tool data.
4. `tooladder.py`: 
This script provides the Tool and Argument classes.
5. `tools.json`:
This JSON file stores the information about the tools. It is updated whenever a tool is added, deleted, or updated.
6. `utils.py`:
This script provides utility functions that are used across the interface scripts.