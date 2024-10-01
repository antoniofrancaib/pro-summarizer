from openai import OpenAI
import os

# Set your OpenAI API key here or set it as an environment variable
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key=api_key,
)

def read_text_file(file_path):
    """Reads content from a text file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        if not content.strip():
            raise ValueError("The input file is empty.")
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

def generate_summary(text):
    """Calls the OpenAI API to generate a summary in Markdown format."""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following text in detailed Markdown format:\n\n{text}",
            }
        ],
        model="gpt-4o-mini",
    )
    return chat_completion.choices[0].message.content.strip()
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Summarize the following text in detailed Markdown format:\n\n{text}",
            max_tokens=1024,
            temperature=0.5
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        raise Exception(f"Failed to generate the summary using the OpenAI API: {e}")

def write_summary_to_file(summary, output_path):
    """Writes the generated summary to a .txt file."""
    try:
        with open(output_path, 'w') as file:
            file.write(summary)
        print(f"Summary successfully saved to '{output_path}'")
    except Exception as e:
        raise Exception(f"An error occurred while writing the summary to the file: {e}")

def main():
    try:
        # Step 1: Read the input file (automatically uses extracted_text.txt)
        input_file = 'extracted_text.txt'
        text_content = read_text_file(input_file)

        # Step 2: Generate the summary using GPT-4
        print(f"Generating summary using GPT-4...")
        summary = generate_summary(text_content)

        # Step 3: Write the summary to a new .txt file
        output_file = input("Enter the path to save the output summary (e.g., 'summary_output.txt'): ")
        write_summary_to_file(summary, output_file)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
