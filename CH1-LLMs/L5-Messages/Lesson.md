# Messages

LLM APIs aren't typically used in a "one-shot" manner, for example:

- Prompt: "What is the meaning of life?"
- Response: "42"

They work the same way ChatGPT works: *in a conversation*. The conversation has a history, and if we keep track of that history, then with each new prompt, the model can see the entire conversation and respond *within the larger context of the conversation*.

## Roles

Importantly, each message in the conversation has a "role". In the context of a chat app like ChatGPT, your conversations would look like this:

- **user**: "What is the meaning of life?"
- **model**: "42"
- **user**: "Wait, what did you just say?"
- **model**: "42. It's is the answer to the ultimate question of life, the universe, and everything."
- **user**: "But why?"
- **model**: "Because Douglas Adams said so."

So, while our program will still be "one-shot" *for now*, let's update our code to store a list of messages in the conversation, and pass in the "role" appropriately.

## Assignment

1.  Create a new list of [`types.Content`](https://googleapis.github.io/python-genai/genai.html#genai.types.Content), and set the user's prompt as the only message (for now):

```python
from google.genai import types

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
```

2.  Update your call to [`models.generate_content`](https://googleapis.github.io/python-genai/genai.html#genai.models.Models.generate_content) to use the messages list:

```python
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)
```

> **Note**: In the future, we'll add more messages to the list as the agent does its tasks in a loop.

**When you're done, answer the question**.

---

## Key Concepts

### <û<ó Vietnamese Translation:

**Messages (Tin nh¯n)**: Các tin nh¯n trong cuÙc trò chuyÇn vÛi LLM, m×i tin nh¯n có vai trò (role) cå thÃ.

**Roles (Vai trò)**:
- **user**: Tin nh¯n të ng°Ýi dùng
- **model**: Ph£n hÓi të AI model

**Conversation History (LËch sí cuÙc trò chuyÇn)**: LLM có thÃ nhìn th¥y toàn bÙ ngï c£nh cuÙc trò chuyÇn Ã °a ra ph£n hÓi phù hãp.

### Learning Objectives:
1. Understand conversation-based LLM interactions vs one-shot prompts
2. Learn about message roles in AI conversations
3. Implement structured message handling with Google Genai API
4. Prepare foundation for conversational agent loops

### Connection to AI Agent Project:
This lesson builds the foundation for your AI agent's conversational abilities. The message structure will be essential when your agent needs to:
- Track conversation history during task execution
- Maintain context across multiple function calls
- Build conversational AI interfaces

The `types.Content` and `types.Part` structures will be crucial for implementing the agent's communication loop with the Gemini API.
# CH1-L5: Messages

## Gemini Translation

### Tin nhắn

Các API của Mô hình Ngôn ngữ Lớn (LLM) thường không được sử dụng theo kiểu "một lần", ví dụ:

- Prompt: "Ý nghĩa của cuộc sống là gì?"
- Phản hồi: "42"

Chúng hoạt động giống như cách ChatGPT hoạt động: **trong một cuộc trò chuyện**. Cuộc trò chuyện có lịch sử, và nếu chúng ta theo dõi lịch sử đó, thì với mỗi prompt mới, mô hình có thể thấy toàn bộ cuộc trò chuyện và phản hồi *trong bối cảnh lớn hơn của cuộc trò chuyện đó*.

### Vai trò

Quan trọng là mỗi tin nhắn trong cuộc trò chuyện đều có một "vai trò". Trong bối cảnh của một ứng dụng trò chuyện như ChatGPT, các cuộc trò chuyện của bạn sẽ trông như thế này:

- **người dùng**: "Ý nghĩa của cuộc sống là gì?"
- **mô hình**: "42"
- **người dùng**: "Khoan, bạn vừa nói gì vậy?"
- **mô hình**: "42. Đó là câu trả lời cho câu hỏi cuối cùng về sự sống, vũ trụ, và mọi thứ."
- **người dùng**: "Nhưng tại sao?"
- **mô hình**: "Bởi vì Douglas Adams đã nói vậy."

Vì vậy, mặc dù chương trình của chúng ta sẽ vẫn là "một lần" *hiện tại*, hãy cập nhật code của chúng ta để lưu trữ một danh sách các tin nhắn trong cuộc trò chuyện và truyền "vai trò" một cách thích hợp.

### Bài tập

1. Tạo một danh sách mới gồm các `types.Content` và đặt prompt của người dùng làm tin nhắn duy nhất (hiện tại):

   ```python
   from google.genai import types

   messages = [
       types.Content(role="user", parts=[types.Part(text=user_prompt)]),
   ]
   ```

2. Cập nhật lệnh gọi `models.generate_content` để sử dụng danh sách tin nhắn:

   ```python
   response = client.models.generate_content(
       model="gemini-2.0-flash-001",
       contents=messages,
   )
   ```

> **Lưu ý**: Trong tương lai, chúng ta sẽ thêm nhiều tin nhắn hơn vào danh sách khi agent thực hiện các nhiệm vụ của mình trong một vòng lặp.
