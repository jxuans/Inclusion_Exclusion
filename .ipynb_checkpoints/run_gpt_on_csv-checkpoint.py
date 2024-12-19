import pandas as pd
import openai
import json

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Define your LLM prompt function
def run_prompt_on_text(text):
    try:
        # Example of using ChatGPT with the specified prompt
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose your model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Process this data: {text}"}
            ],
            temperature=0.7
        )
        # Extract the model's response
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error processing text: {text}. Error: {e}")
        return None

# Load your CSV file
csv_file = "your_file.csv"  # Update with your CSV file path
output_file = "output.json"  # Update with your desired output file

# Read CSV and process each row
df = pd.read_csv(csv_file)
output_data = []

for index, row in df.iterrows():
    # Assuming the column to process is named 'text'
    text_to_process = row['text']  # Update with your column name
    print(f"Processing row {index + 1}...")
    processed_output = run_prompt_on_text(text_to_process)
    if processed_output:
        output_data.append({
            "row_index": index,
            "input_text": text_to_process,
            "output_text": processed_output
        })

# Save output as JSON
with open(output_file, "w") as f:
    json.dump(output_data, f, indent=4)

print(f"Processing complete! Results saved to {output_file}.")
