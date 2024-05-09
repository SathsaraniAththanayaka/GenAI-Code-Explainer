import google.generativeai as palm
import os
import gradio as gr

# Configure the API key
palm.configure(api_key='API KEY')

# PaLM model that is being used
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
#print(model)

def get_completion(code_snippet):
  python_code_examples = f"""
  ----------------------
  Example 1: Code Snippet
  x=10
  def foo():
    global x
    x=5
  foo()
  print(x)

  Correct answer: 5
  Explanation: Inside the foo function, the global keyword is used to modify the global variable x to be 5.
  So, print(x) outside the function prints the modified value, which is 5.
  -----------------------
  Example 2: Code Snippet
  def modify_list(input_list):
    input_list.append(4)
    input_list = [1,2,3]
  my_list = [0]
  modify_list(my_list)
  print(my_list)

  Correct answer: [0,4]
  Explanation: Inside the modify_list function, an element 4 is appended to input_list.
  Then, input_list is reassigned to a new list [1,2,3], but this change doesn't affect the original list.
  So, print(my_list) outputs [0,4].
  -----------------------
  """

  prompt = f"""
  Your task is to act as a Python Code Explainer.
  I'll give you a Code Snippet.
  Your job is to explain the Code Snippet step-by-step.
  Break down the code into as many steps as possible

  State your Steps and checkpoints in your output.
  Ensure clarity and detail in your explanation to assist in understanding the code's behavior effectively.
  Few good examples of Python code between #### separator:
  ####
  {python_code_examples}
  ####
  Code Snippet is shared below, delimited with triple backticks:
  ```
  {code_snippet}
  ```
  """
  completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0,
      # The maximum length of the response
      max_output_tokens=500,
  )
  response = completion.result
  return response


iface = gr.Interface(fn=get_completion,inputs="text",
                       outputs="text")

iface.launch(share=True)