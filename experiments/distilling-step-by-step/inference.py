from transformers import T5ForConditionalGeneration, T5Tokenizer

# Replace with your actual checkpoint folder path
checkpoint_path = "/path/to/checkpoint/folder/"

# Load the model and tokenizer using Transformers library
model = T5ForConditionalGeneration.from_pretrained(checkpoint_path)
tokenizer = T5Tokenizer.from_pretrained(checkpoint_path)

# Example input
json_format = """[
                    {
                        "tool_name": { "type": "string" },
                        "arguments": [
                            {
                                "argument_name": { "type": "string" },
                                "argument_value": { "type": "string" }
                            }
                        ]
                    }
                ]"""

input_text = f"YOUR INPUT TEXT"
input_text += f" Give result as a json: {json_format}"

# Tokenize input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate output
output_ids = model.generate(input_ids, max_new_tokens = 1024)

# Decode and print the output
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("Input:", input_text)
print("Output:", output_text)
