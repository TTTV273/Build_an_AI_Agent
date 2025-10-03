# Calling

Okay, now our agent can _choose_ which function to call, now it's time to actually _call_ the function.

## Assignment

1. Create a new function that will handle the abstract task of calling one of our four functions. This is my definition:

```py
def call_function(function_call_part, verbose=False):

```

`function_call_part` is a [types.FunctionCall](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionCall) that most importantly has:

* A `.name` property (the name of the function, a `string`)
* A `.args` property (a dictionary of named arguments to the function)

If `verbose` is specified, print the function name and args:

```py
print(f"Calling function: {function_call_part.name}({function_call_part.args})")

```

Otherwise, just print the name:

```py
print(f" - Calling function: {function_call_part.name}")

```

1. Based on the name, actually call the function and capture the result.  
   * Be sure to manually add the "working\_directory" argument to the dictionary of keyword arguments, because the LLM doesn't control that one. The working directory should be `./calculator`.  
   * The syntax to pass a dictionary into a function using [keyword arguments](https://docs.python.org/3/glossary.html#term-argument) is `some_function(**some_args)`

I used a dictionary of `function name (string)` \-> `function` to accomplish this.

1. If the function name is invalid, return a [types.Content](https://googleapis.github.io/python-genai/genai.html#genai.types.Content) that explains the error:

```py
return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )
    ],
)

```

1. Return [types.Content](https://googleapis.github.io/python-genai/genai.html#genai.types.Content) with a [from\_function\_response](https://googleapis.github.io/python-genai/genai.html#genai.types.Part.from%5Ffunction%5Fresponse) describing the result of the function call:

```py
return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
        )
    ],
)

```

Note that `from_function_response` requires the response to be a dictionary, so we just shove the string result into a "result" field.

1. Back where you handle the response from the model `generate_content`, instead of simply printing the name of the function the LLM decides to call, use `call_function`.  
   * The [types.Content](https://googleapis.github.io/python-genai/genai.html#genai.types.Content) that we return from `call_function` should have a `.parts[0].function_response.response` within.  
   * If it doesn't, `raise` a fatal exception of some sort.  
   * If it does, and `verbose` was set, print the result of the function call like this:

```py
print(f"-> {function_call_result.parts[0].function_response.response}")

```

1. Test your program. You should now be able to execute each function given a prompt that asks for it. Try some different prompts and use the `--verbose` flag to make sure all the functions work.  
   * List the directory contents  
   * Get a file's contents  
   * Write file contents (don't overwrite anything important, maybe create a new file)  
   * Execute the calculator app's tests (`tests.py`)

**Run and submit** the CLI tests.
