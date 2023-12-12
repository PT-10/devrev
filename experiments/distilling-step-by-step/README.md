## Running Inference from the distilled Google's T5 version 1.1

Follow these steps to run inference from the distilled Google's T5 version 1.1:

1. Navigate to the *distilling-step-by-step* folder inside *experiments*.
`cd /path/to/distilling-step-by-step`

2. Make a virtual environment.
`virtualenv distill`

3. Activate the created virtual environment.
`source distill/bin/activate`

4. Now install the dependencies.
`pip install -r -requirements.txt`

5. Download the checkpoint folder from [here]() in the `distilling-step-by-step` folder.

6. Update the *checkpoint_path* variable in *inference.py* file to the actual path of the checkpoint.

7. Update the *input_text* variable with the query that you want to run the inference on.

8. Run the inference.
`python3 inference.py`

9. Now you can see the output in the terminal window.

## Re-distilling the Google's T5 version 1.1 model with GPT-4 labels and rationales

Follow these steps to re-distill the model:

1. Navigate to the *distilling-step-by-step* folder inside *experiments*.
`cd /path/to/distilling-step-by-step`

2. Run the *script.sh* in the terminal.
`bash script.sh`
