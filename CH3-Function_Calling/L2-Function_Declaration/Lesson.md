# Function Declaration

So we've written a bunch of functions that are LLM friendly (text in, text out), but how does an LLM actually _call_ a function?

Well the answer is that... it doesn't. At least not directly. It works like this:

1. We tell the LLM which functions are available to it
2. We give it a prompt
3. It describes which function it wants to call, and what arguments to pass to it
4. _We_ call that function with the arguments it provided
5. We return the result to the LLM

We're using the LLM as a decision-making engine, but we're still the ones running the code.

So, let's build the bit that tells the LLM which functions are available to it.

## Assignment

1. We can use [types.FunctionDeclaration](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration) to build the "declaration" or "schema" for a function. Again, this basically just tells the LLM _how_ to use the function. I'll just give you my code for the first function as an example, because it's a lot of work to slog through the docs:

I added this code to my `functions/get_files_info.py` file, but you can place it anywhere, but remember that it will need to be imported when used:

In our solution it is imported like this: `from functions.get_files_info import schema_get_files_info`

```py
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

```

We won't allow the LLM to specify the `working_directory` parameter. We're going to hard code that.

1. Use [types.Tool](https://googleapis.github.io/python-genai/genai.html#genai.types.Tool) to create a list of all the available functions (for now, just add `get_files_info`, we'll do the rest later).

```py
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

```

1. Add the `available_functions` to the `client.models.generate_content` call as the `tools` parameter.

```py
config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

```

1. Update the system prompt to instruct the LLM on how to use the function. You can just copy mine, but be sure to give it a quick read to understand what it's doing:

```py
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

```

1. Instead of simply printing the [.text](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.text) property of the `generate_content` response, check the [.function\_calls](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.function%5Fcalls) property as well. If the LLM called a function, print the function name and arguments:

```py
f"Calling function: {function_call_part.name}({function_call_part.args})"

```

Otherwise, just print the text as normal.

1. Test your program.  
   * "what files are in the root?" -> `get_files_info({'directory': '.'})`  
   * "what files are in the pkg directory?" -> `get_files_info({'directory': 'pkg'})`

**Run and submit** the CLI tests.

---
# Khai báo hàm

Chúng ta đã viết một loạt các hàm thân thiện với LLM (văn bản vào, văn bản ra), nhưng làm thế nào một LLM thực sự _gọi_ một hàm?

Câu trả lời là... nó không gọi. Ít nhất là không trực tiếp. Nó hoạt động như sau:

1. Chúng ta cho LLM biết những hàm nào có sẵn cho nó
2. Chúng ta đưa cho nó một lời nhắc (prompt)
3. Nó mô tả hàm nào nó muốn gọi và các đối số cần truyền cho hàm đó
4. _Chúng ta_ gọi hàm đó với các đối số mà nó đã cung cấp
5. Chúng ta trả về kết quả cho LLM

Chúng ta đang sử dụng LLM như một công cụ ra quyết định, nhưng chúng ta vẫn là người chạy mã.

Vì vậy, hãy xây dựng phần cho LLM biết những hàm nào có sẵn cho nó.

## Bài tập

1. Chúng ta có thể sử dụng [types.FunctionDeclaration](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration) để xây dựng "khai báo" hoặc "lược đồ" (schema) cho một hàm. Một lần nữa, điều này về cơ bản chỉ cho LLM biết _cách_ sử dụng hàm. Tôi sẽ cung cấp cho bạn mã của tôi cho hàm đầu tiên làm ví dụ, vì việc đọc tài liệu khá tốn công:

Tôi đã thêm mã này vào tệp `functions/get_files_info.py` của mình, nhưng bạn có thể đặt nó ở bất cứ đâu, nhưng hãy nhớ rằng nó sẽ cần được nhập (import) khi sử dụng:

Trong giải pháp của chúng tôi, nó được nhập như sau: `from functions.get_files_info import schema_get_files_info`

```py
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Liệt kê các tệp trong thư mục được chỉ định cùng với kích thước của chúng, bị giới hạn trong thư mục làm việc.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Thư mục để liệt kê các tệp, tương đối so với thư mục làm việc. Nếu không được cung cấp, liệt kê các tệp trong chính thư mục làm việc.",
            ),
        },
    ),
)

```

Chúng ta sẽ không cho phép LLM chỉ định tham số `working_directory`. Chúng ta sẽ mã hóa cứng (hard code) nó.

2. Sử dụng [types.Tool](https://googleapis.github.io/python-genai/genai.html#genai.types.Tool) để tạo một danh sách tất cả các hàm có sẵn (hiện tại, chỉ cần thêm `get_files_info`, chúng ta sẽ làm phần còn lại sau).

```py
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

```

3. Thêm `available_functions` vào lệnh gọi `client.models.generate_content` làm tham số `tools`.

```py
config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

```

4. Cập nhật lời nhắc hệ thống (system prompt) để hướng dẫn LLM cách sử dụng hàm. Bạn có thể sao chép của tôi, nhưng hãy chắc chắn đọc lướt qua để hiểu nó đang làm gì:

```py
system_prompt = """
Bạn là một trợ lý lập trình AI hữu ích.

Khi người dùng đặt câu hỏi hoặc đưa ra yêu cầu, hãy lập kế hoạch gọi hàm. Bạn có thể thực hiện các thao tác sau:

- Liệt kê các tệp và thư mục

Tất cả các đường dẫn bạn cung cấp phải tương đối so với thư mục làm việc. Bạn không cần chỉ định thư mục làm việc trong các lệnh gọi hàm của mình vì nó được tự động đưa vào vì lý do bảo mật.
"""

```

5. Thay vì chỉ in thuộc tính [.text](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.text) của phản hồi `generate_content`, hãy kiểm tra cả thuộc tính [.function\_calls](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.function%5Fcalls). Nếu LLM đã gọi một hàm, hãy in tên hàm và các đối số:

```py
f"Đang gọi hàm: {function_call_part.name}({function_call_part.args})"

```

Nếu không, chỉ cần in văn bản như bình thường.

6. Kiểm tra chương trình của bạn.
   * "what files are in the root?" -> `get_files_info({'directory': '.'})`
   * "what files are in the pkg directory?" -> `get_files_info({'directory': 'pkg'})`

**Chạy và nộp** bài kiểm tra CLI.

---
### Giải thích chi tiết: `types.FunctionDeclaration`

Anh có thể coi `FunctionDeclaration` giống như việc tạo ra một "tờ hướng dẫn sử dụng" cho một hàm Python để LLM có thể đọc được. LLM không thể tự đọc và hiểu code Python của chúng ta, vì vậy chúng ta phải mô tả hàm đó cho nó một cách có cấu trúc.

Hãy dùng một ví dụ so sánh: `FunctionDeclaration` giống như một **thực đơn (menu)** trong nhà hàng, và LLM là một **thực khách**.

Thực khách (LLM) không cần biết công thức nấu ăn (code Python bên trong hàm), nhưng họ cần đọc thực đơn để biết:
1.  Nhà hàng có những món gì?
2.  Món đó dùng để làm gì?
3.  Làm thế nào để gọi món đó (cần cung cấp thông tin gì thêm)?

Trong `FunctionDeclaration`, mỗi phần tương ứng với một thông tin trên thực đơn:

*   `name="get_files_info"`
    *   **Tương tự như:** Tên món ăn trên thực đơn (ví dụ: "Phở Bò Tái").
    *   **Mục đích:** Đây là tên định danh duy nhất mà LLM sẽ dùng để yêu cầu gọi hàm.

*   `description="Liệt kê các tệp..."`
    *   **Tương tự như:** Phần mô tả món ăn (ví dụ: "Sợi phở mềm mại trong nước dùng xương hầm đậm đà, ăn kèm thịt bò tái thái mỏng...").
    *   **Mục đích:** Giúp LLM hiểu được hàm này có chức năng gì và khi nào thì nên sử dụng nó. Khi anh yêu cầu "xem các tệp trong thư mục", LLM sẽ đọc mô tả này và thấy rằng hàm `get_files_info` là phù hợp.

*   `parameters={...}`
    *   **Tương tự như:** Các tùy chọn thêm cho món ăn (ví dụ: "Tùy chọn: thêm trứng, không hành, nhiều bánh phở").
    *   **Mục đích:** Đây là phần quan trọng nhất, định nghĩa các "tham số" mà LLM có thể (hoặc phải) cung cấp khi yêu cầu gọi hàm.
        *   `"directory"`: Đây là một tham số cụ thể, giống như tùy chọn "không hành".
        *   `type=types.Type.STRING`: Quy định rằng giá trị của tham số `directory` phải là một chuỗi (văn bản).
        *   `description="..."`: Giải thích cho LLM biết tham số `directory` này có ý nghĩa gì.

**Tóm lại:** Bằng cách tạo ra `FunctionDeclaration`, chúng ta đang "dạy" cho LLM về công cụ mà nó có, để nó có thể đưa ra quyết định ("gọi món") một cách thông minh dựa trên yêu cầu của người dùng.
