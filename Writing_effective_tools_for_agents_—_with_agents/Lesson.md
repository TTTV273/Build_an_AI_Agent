# Writing Effective Tools for AI Agents - Using AI Agents

*Source: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/writing-tools-for-agents)*

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) can empower LLM agents with potentially hundreds of tools to solve real-world tasks. But how do we make those tools maximally effective?

In this post, we describe our most effective techniques for improving performance in a variety of agentic AI systems.

We begin by covering how you can:
- Build and test prototypes of your tools
- Create and run comprehensive evaluations of your tools with agents
- Collaborate with agents like Claude Code to automatically increase the performance of your tools

We conclude with key principles for writing high-quality tools we've identified along the way:
- Choosing the right tools to implement (and not to implement)
- Namespacing tools to define clear boundaries in functionality
- Returning meaningful context from tools back to agents
- Optimizing tool responses for token efficiency
- Prompt-engineering tool descriptions and specs

## What is a Tool?

In computing, deterministic systems produce the same output every time given identical inputs, while *non-deterministic* systemslike agentscan generate varied responses even with the same starting conditions.

When we traditionally write software, we're establishing a contract between deterministic systems. For instance, a function call like `getWeather("NYC")` will always fetch the weather in New York City in the exact same manner every time it is called.

Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents. When a user asks "Should I bring an umbrella today?," an agent might call the weather tool, answer from general knowledge, or even ask a clarifying question about location first. Occasionally, an agent might hallucinate or even fail to grasp how to use a tool.

This means fundamentally rethinking our approach when writing software for agents: instead of writing tools and [MCP servers](https://modelcontextprotocol.io/) the way we'd write functions and APIs for other developers or systems, we need to design them for agents.

Our goal is to increase the surface area over which agents can be effective in solving a wide range of tasks by using tools to pursue a variety of successful strategies. Fortunately, in our experience, the tools that are most "ergonomic" for agents also end up being surprisingly intuitive to grasp as humans.

## How to Write Tools

In this section, we describe how you can collaborate with agents both to write and to improve the tools you give them. Start by standing up a quick prototype of your tools and testing them locally. Next, run a comprehensive evaluation to measure subsequent changes. Working alongside agents, you can repeat the process of evaluating and improving your tools until your agents achieve strong performance on real-world tasks.

### Building a Prototype

It can be difficult to anticipate which tools agents will find ergonomic and which tools they won't without getting hands-on yourself. Start by standing up a quick prototype of your tools. If you're using [Claude Code](https://www.anthropic.com/claude-code) to write your tools (potentially in one-shot), it helps to give Claude documentation for any software libraries, APIs, or SDKs (including potentially the [MCP SDK](https://modelcontextprotocol.io/docs/sdk)) your tools will rely on. LLM-friendly documentation can commonly be found in flat `llms.txt` files on official documentation sites (here's our [API's](https://docs.anthropic.com/llms.txt)).

Wrapping your tools in a [local MCP server](https://modelcontextprotocol.io/docs/develop/connect-local-servers) or [Desktop extension](https://www.anthropic.com/engineering/desktop-extensions) (DXT) will allow you to connect and test your tools in Claude Code or the Claude Desktop app.

To connect your local MCP server to Claude Code, run `claude mcp add <name> <command> [args...]`.

To connect your local MCP server or DXT to the Claude Desktop app, navigate to `Settings > Developer` or `Settings > Extensions`, respectively.

Tools can also be passed directly into [Anthropic API](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) calls for programmatic testing.

Test the tools yourself to identify any rough edges. Collect feedback from your users to build an intuition around the use-cases and prompts you expect your tools to enable.

### Running an Evaluation

Next, you need to measure how well Claude uses your tools by running an evaluation. Start by generating lots of evaluation tasks, grounded in real world uses. We recommend collaborating with an agent to help analyze your results and determine how to improve your tools. See this process end-to-end in our [tool evaluation cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_evaluation/tool_evaluation.ipynb).

#### Generating Evaluation Tasks

With your early prototype, Claude Code can quickly explore your tools and create dozens of prompt and response pairs. Prompts should be inspired by real-world uses and be based on realistic data sources and services (for example, internal knowledge bases and microservices). We recommend you avoid overly simplistic or superficial "sandbox" environments that don't stress-test your tools with sufficient complexity. Strong evaluation tasks might require multiple tool callspotentially dozens.

Here are some examples of **strong tasks**:
- Schedule a meeting with Jane next week to discuss our latest Acme Corp project. Attach the notes from our last project planning meeting and reserve a conference room.
- Customer ID 9182 reported that they were charged three times for a single purchase attempt. Find all relevant log entries and determine if any other customers were affected by the same issue.
- Customer Sarah Chen just submitted a cancellation request. Prepare a retention offer. Determine: (1) why they're leaving, (2) what retention offer would be most compelling, and (3) any risk factors we should be aware of before making an offer.

And here are some **weaker tasks**:
- Schedule a meeting with jane@acme.corp next week.
- Search the payment logs for `purchase_complete` and `customer_id=9182`.
- Find the cancellation request by Customer ID 45892.

Each evaluation prompt should be paired with a verifiable response or outcome. Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response. Avoid overly strict verifiers that reject correct responses due to spurious differences like formatting, punctuation, or valid alternative phrasings.

For each prompt-response pair, you can optionally also specify the tools you expect an agent to call in solving the task, to measure whether or not agents are successful in grasping each tool's purpose during evaluation. However, because there might be multiple valid paths to solving tasks correctly, try to avoid overspecifying or overfitting to strategies.

#### Running the Evaluation

We recommend running your evaluation programmatically with direct LLM API calls. Use simple agentic loops (`while`-loops wrapping alternating LLM API and tool calls): one loop for each evaluation task. Each evaluation agent should be given a single task prompt and your tools.

In your evaluation agents' system prompts, we recommend instructing agents to output not just structured response blocks (for verification), but also reasoning and feedback blocks. Instructing agents to output these *before* tool call and response blocks may increase LLMs' effective intelligence by triggering chain-of-thought (CoT) behaviors.

If you're running your evaluation with Claude, you can turn on [interleaved thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) for similar functionality "off-the-shelf". This will help you probe why agents do or don't call certain tools and highlight specific areas of improvement in tool descriptions and specs.

As well as top-level accuracy, we recommend collecting other metrics like the total runtime of individual tool calls and tasks, the total number of tool calls, the total token consumption, and tool errors. Tracking tool calls can help reveal common workflows that agents pursue and offer some opportunities for tools to consolidate.

#### Analyzing Results

Agents are your helpful partners in spotting issues and providing feedback on everything from contradictory tool descriptions to inefficient tool implementations and confusing tool schemas. However, keep in mind that what agents omit in their feedback and responses can often be more important than what they include. LLMs don't always [say what they mean](https://www.anthropic.com/research/tracing-thoughts-language-model).

Observe where your agents get stumped or confused. Read through your evaluation agents' reasoning and feedback (or CoT) to identify rough edges. Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent's CoT. Read between the lines; remember that your evaluation agents don't necessarily know the correct answers and strategies.

Analyze your tool calling metrics. Lots of redundant tool calls might suggest some rightsizing of pagination or token limit parameters is warranted; lots of tool errors for invalid parameters might suggest tools could use clearer descriptions or better examples. When we launched Claude's [web search tool](https://www.anthropic.com/news/web-search), we identified that Claude was needlessly appending `2025` to the tool's `query` parameter, biasing search results and degrading performance (we steered Claude in the right direction by improving the tool description).

### Collaborating with Agents

You can even let agents analyze your results and improve your tools for you. Simply concatenate the transcripts from your evaluation agents and paste them into Claude Code. Claude is an expert at analyzing transcripts and refactoring lots of tools all at oncefor example, to ensure tool implementations and descriptions remain self-consistent when new changes are made.

In fact, most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code. Our evaluations were created on top of our internal workspace, mirroring the complexity of our internal workflows, including real projects, documents, and messages.

We relied on held-out test sets to ensure we did not overfit to our "training" evaluations. These test sets revealed that we could extract additional performance improvements even beyond what we achieved with "expert" tool implementationswhether those tools were manually written by our researchers or generated by Claude itself.

In the next section, we'll share some of what we learned from this process.

## Principles for Writing Effective Tools

In this section, we distill our learnings into a few guiding principles for writing effective tools.

### Choosing the Right Tools for Agents

More tools don't always lead to better outcomes. A common error we've observed is tools that merely wrap existing software functionality or API endpointswhether or not the tools are appropriate for agents. This is because agents have distinct "affordances" to traditional softwarethat is, they have different ways of perceiving the potential actions they can take with those tools.

LLM agents have limited "context" (that is, there are limits to how much information they can process at once), whereas computer memory is cheap and abundant. Consider the task of searching for a contact in an address book. Traditional software programs can efficiently store and process a list of contacts one at a time, checking each one before moving on.

However, if an LLM agent uses a tool that returns ALL contacts and then has to read through each one token-by-token, it's wasting its limited context space on irrelevant information (imagine searching for a contact in your address book by reading each page from top-to-bottomthat is, via brute-force search). The better and more natural approach (for agents and humans alike) is to skip to the relevant page first (perhaps finding it alphabetically).

We recommend building a few thoughtful tools targeting specific high-impact workflows, which match your evaluation tasks and scaling up from there. In the address book case, you might choose to implement a `search_contacts` or `message_contact` tool instead of a `list_contacts` tool.

Tools can consolidate functionality, handling potentially *multiple* discrete operations (or API calls) under the hood. For example, tools can enrich tool responses with related metadata or handle frequently chained, multi-step tasks in a single tool call.

Here are some examples:
- Instead of implementing a `list_users`, `list_events`, and `create_event` tools, consider implementing a `schedule_event` tool which finds availability and schedules an event.
- Instead of implementing a `read_logs` tool, consider implementing a `search_logs` tool which only returns relevant log lines and some surrounding context.
- Instead of implementing `get_customer_by_id`, `list_transactions`, and `list_notes` tools, implement a `get_customer_context` tool which compiles all of a customer's recent & relevant information all at once.

Make sure each tool you build has a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way that a human would, given access to the same underlying resources, and simultaneously reduce the context that would have otherwise been consumed by intermediate outputs.

Too many tools or overlapping tools can also distract agents from pursuing efficient strategies. Careful, selective planning of the tools you build (or don't build) can really pay off.

### Namespacing Your Tools

Your AI agents will potentially gain access to dozens of MCP servers and hundreds of different toolsincluding those by other developers. When tools overlap in function or have a vague purpose, agents can get confused about which ones to use.

Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools; MCP clients sometimes do this by default. For example, namespacing tools by service (e.g., `asana_search`, `jira_search`) and by resource (e.g., `asana_projects_search`, `asana_users_search`), can help agents select the right tools at the right time.

We have found selecting between prefix- and suffix-based namespacing to have non-trivial effects on our tool-use evaluations. Effects vary by LLM and we encourage you to choose a naming scheme according to your own evaluations.

Agents might call the wrong tools, call the right tools with the wrong parameters, call too few tools, or process tool responses incorrectly. By selectively implementing tools whose names reflect natural subdivisions of tasks, you simultaneously reduce the number of tools and tool descriptions loaded into the agent's context and offload agentic computation from the agent's context back into the tool calls themselves. This reduces an agent's overall risk of making mistakes.

### Returning Meaningful Context from Your Tools

In the same vein, tool implementations should take care to return only high signal information back to agents. They should prioritize contextual relevance over flexibility, and eschew low-level technical identifiers (for example: `uuid`, `256px_image_url`, `mime_type`). Fields like `name`, `image_url`, and `file_type` are much more likely to directly inform agents' downstream actions and responses.

Agents also tend to grapple with natural language names, terms, or identifiers significantly more successfully than they do with cryptic identifiers. We've found that merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful and interpretable language (or even a 0-indexed ID scheme) significantly improves Claude's precision in retrieval tasks by reducing hallucinations.

In some instances, agents may require the flexibility to interact with both natural language and technical identifiers outputs, if only to trigger downstream tool calls (for example, `search_user(name='jane')`  `send_message(id=12345)`). You can enable both by exposing a simple `response_format` enum parameter in your tool, allowing your agent to control whether tools return `"concise"` or `"detailed"` responses.

You can add more formats for even greater flexibility, similar to GraphQL where you can choose exactly which pieces of information you want to receive. Here is an example ResponseFormat enum to control tool response verbosity:

```python
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

**Example of a detailed tool response (206 tokens):**
```json
{
  "threads": [
    {
      "thread_ts": "1735089600.123456",
      "channel_id": "C1234567890",
      "user_id": "U0987654321",
      "user_name": "john.doe",
      "timestamp": "2024-12-25T00:00:00Z",
      "message": "Hey team, quick question about the project timeline...",
      "replies_count": 3,
      "participants": ["U0987654321", "U1122334455"],
      "latest_reply": "2024-12-25T01:30:00Z"
    }
  ]
}
```

**Example of a concise tool response (72 tokens):**
```json
{
  "threads": [
    {
      "user_name": "john.doe",
      "timestamp": "2024-12-25T00:00:00Z",
      "message": "Hey team, quick question about the project timeline...",
      "replies_count": 3
    }
  ]
}
```

Even your tool response structurefor example XML, JSON, or Markdowncan have an impact on evaluation performance: there is no one-size-fits-all solution. This is because LLMs are trained on next-token prediction and tend to perform better with formats that match their training data. The optimal response structure will vary widely by task and agent. We encourage you to select the best response structure based on your own evaluation.

### Optimizing Tool Responses for Token Efficiency

Optimizing the quality of context is important. But so is optimizing the *quantity* of context returned back to agents in tool responses.

We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain.

If you choose to truncate responses, be sure to steer agents with helpful instructions. You can directly encourage agents to pursue more token-efficient strategies, like making many small and targeted searches instead of a single, broad search for a knowledge retrieval task. Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.

**Example of a truncated tool response:**
```json
{
  "results": [
    {"id": 1, "title": "Project Alpha Meeting Notes", "date": "2024-12-20"},
    {"id": 2, "title": "Budget Review Q4", "date": "2024-12-19"},
    "... (showing first 10 of 847 results)"
  ],
  "metadata": {
    "total_results": 847,
    "showing": 10,
    "truncated": true,
    "suggestion": "Use more specific search terms or add filters to narrow results"
  }
}
```

**Example of an unhelpful error response:**
```json
{
  "error": "ValidationError: Invalid input",
  "code": 400
}
```

**Example of a helpful error response:**
```json
{
  "error": "Invalid date format in 'start_date' parameter",
  "message": "Expected format: YYYY-MM-DD (e.g., '2024-12-25')",
  "received": "12/25/2024",
  "suggestion": "Please reformat the date and try again"
}
```

### Prompt-Engineering Your Tool Descriptions

We now come to one of the most effective methods for improving tools: prompt-engineering your tool descriptions and specs. Because these are loaded into your agents' context, they can collectively steer agents toward effective tool-calling behaviors.

When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team. Consider the context that you might implicitly bringspecialized query formats, definitions of niche terminology, relationships between underlying resourcesand make it explicit. Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`.

With your evaluation you can measure the impact of your prompt engineering with greater confidence. Even small refinements to tool descriptions can yield dramatic improvements. Claude Sonnet 3.5 achieved state-of-the-art performance on the [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) evaluation after we made precise refinements to tool descriptions, dramatically reducing error rates and improving task completion.

You can find other best practices for tool definitions in our [Developer Guide](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions). If you're building tools for Claude, we also recommend reading about how tools are dynamically loaded into Claude's [system prompt](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt). Lastly, if you're writing tools for an MCP server, [tool annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) help disclose which tools require open-world access or make destructive changes.

## Looking Ahead

To build effective tools for agents, we need to re-orient our software development practices from predictable, deterministic patterns to non-deterministic ones.

Through the iterative, evaluation-driven process we've described in this post, we've identified consistent patterns in what makes tools successful: Effective tools are intentionally and clearly defined, use agent context judiciously, can be combined together in diverse workflows, and enable agents to intuitively solve real-world tasks.

In the future, we expect the specific mechanisms through which agents interact with the world to evolvefrom updates to the MCP protocol to upgrades to the underlying LLMs themselves. With a systematic, evaluation-driven approach to improving tools for agents, we can ensure that as agents become more capable, the tools they use will evolve alongside them.

## Acknowledgements

Written by Ken Aizawa with valuable contributions from colleagues across Research (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh, Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra, Adam Jones), Product Engineering (Santiago Seira), Marketing (Molly Vorwerck), Design (Drew Roper), and Applied AI (Christian Ryan, Alexander Bricken).

## Connection to AI Agent Development

This guidance is particularly relevant when building agents like the Boot.dev AI Agent project, where you need to implement core functions:

- `get_files_info()` - Should return structured, meaningful directory information with natural language identifiers
- `get_file_content()` - Must handle various file types and sizes efficiently with pagination/truncation
- `write_file()` - Needs robust error handling with helpful error messages and confirmation
- `run_python_file()` - Should capture output, errors, and execution context with clear formatting

Each tool should follow these principles to create an effective agent that can genuinely assist with coding tasks while being token-efficient and providing meaningful context for decision-making.

---

**Key Takeaway**: Effective agent tools require careful design that considers the unique constraints and capabilities of AI agents, emphasizing clarity, efficiency, and robust error handling over traditional software engineering practices. The iterative, evaluation-driven approach with agent collaboration is essential for creating truly effective tools.


## **Viết Công cụ Hiệu quả cho các AI Agent Sử dụng AI Agent**

*Nguồn: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/writing-tools-for-agents)*

**Giao thức Ngữ cảnh Mô hình (Model Context Protocol \- MCP)** có thể trao quyền cho các agent LLM với hàng trăm công cụ để giải quyết các tác vụ trong thế giới thực. Nhưng làm thế nào để chúng ta làm cho các công cụ đó hiệu quả tối đa?

Trong bài viết này, chúng tôi mô tả các kỹ thuật hiệu quả nhất của mình để cải thiện hiệu suất trong nhiều hệ thống AI mang tính tác tử (agentic).

Chúng tôi sẽ bắt đầu bằng cách trình bày làm thế nào bạn có thể:

* Xây dựng và kiểm thử các bản mẫu (prototype) của công cụ  
* Tạo và chạy các bài đánh giá toàn diện cho các công cụ của bạn với agent  
* Hợp tác với các agent như Claude Code để tự động tăng hiệu suất của công cụ

Chúng tôi kết luận bằng các nguyên tắc chính để viết công cụ chất lượng cao mà chúng tôi đã xác định được trong quá trình làm việc:

* Lựa chọn đúng công cụ để triển khai (và không triển khai)  
* Phân chia không gian tên (namespacing) cho các công cụ để xác định ranh giới chức năng rõ ràng  
* Trả về ngữ cảnh có ý nghĩa từ công cụ cho agent  
* Tối ưu hóa phản hồi của công cụ để tiết kiệm token  
* Kỹ thuật prompt (prompt-engineering) cho các mô tả và đặc tả của công cụ

![][image1]

### **Công cụ (Tool) là gì?**

Trong lĩnh vực máy tính, các hệ thống tất định (deterministic) tạo ra cùng một đầu ra mỗi khi nhận cùng một đầu vào, trong khi các hệ thống *phi tất định* (non-deterministic)—như các agent—có thể tạo ra các phản hồi khác nhau ngay cả với cùng điều kiện ban đầu.

Khi chúng ta viết phần mềm theo cách truyền thống, chúng ta đang thiết lập một hợp đồng giữa các hệ thống tất định. Ví dụ, một lời gọi hàm như getWeather("NYC") sẽ luôn lấy thông tin thời tiết ở thành phố New York theo cùng một cách chính xác mỗi khi nó được gọi.

Công cụ là một loại phần mềm mới, phản ánh một hợp đồng giữa các hệ thống tất định và các agent phi tất định. Khi người dùng hỏi "Hôm nay tôi có nên mang ô không?", một agent có thể gọi công cụ thời tiết, trả lời từ kiến thức chung, hoặc thậm chí hỏi một câu hỏi làm rõ về vị trí trước. Thỉnh thoảng, một agent có thể tạo ra ảo giác (hallucinate) hoặc thậm chí không hiểu cách sử dụng một công cụ.

Điều này có nghĩa là chúng ta phải suy nghĩ lại về cơ bản cách tiếp cận của mình khi viết phần mềm cho các agent: thay vì viết các công cụ và [máy chủ MCP (MCP servers)](https://modelcontextprotocol.io/) theo cách chúng ta viết các hàm và API cho các lập trình viên hoặc hệ thống khác, chúng ta cần thiết kế chúng cho các agent.

Mục tiêu của chúng ta là mở rộng phạm vi mà các agent có thể hoạt động hiệu quả để giải quyết một loạt các tác vụ bằng cách sử dụng công cụ để theo đuổi nhiều chiến lược thành công khác nhau. May mắn thay, theo kinh nghiệm của chúng tôi, các công cụ "dễ sử dụng và trực quan" nhất đối với agent cũng là những công cụ dễ hiểu một cách đáng ngạc nhiên đối với con người.

### **Cách Viết Công cụ**

Trong phần này, chúng tôi mô tả cách bạn có thể hợp tác với các agent để vừa viết vừa cải thiện các công cụ mà bạn cung cấp cho chúng. Bắt đầu bằng cách dựng nhanh một bản mẫu của các công cụ và kiểm thử chúng cục bộ. Tiếp theo, chạy một bài đánh giá toàn diện để đo lường các thay đổi sau đó. Làm việc cùng với các agent, bạn có thể lặp lại quy trình đánh giá và cải thiện công cụ cho đến khi các agent của bạn đạt được hiệu suất cao trong các tác vụ thực tế.

#### **Xây dựng một Bản mẫu (Prototype)**

Có thể khó đoán trước được công cụ nào các agent sẽ thấy dễ sử dụng và công cụ nào không nếu bạn không tự mình bắt tay vào làm. Hãy bắt đầu bằng cách dựng nhanh một bản mẫu của các công cụ. Nếu bạn đang sử dụng [Claude Code](https://www.anthropic.com/claude-code) để viết công cụ (có thể chỉ trong một lần duy nhất \- one-shot), việc cung cấp cho Claude tài liệu về bất kỳ thư viện phần mềm, API hoặc SDK nào (bao gồm cả [MCP SDK](https://modelcontextprotocol.io/docs/sdk)) mà công cụ của bạn sẽ dựa vào là rất hữu ích. Tài liệu thân thiện với LLM thường có thể được tìm thấy trong các tệp llms.txt phẳng trên các trang tài liệu chính thức (đây là [API của chúng tôi](https://docs.anthropic.com/llms.txt)).

Việc bọc các công cụ của bạn trong một [máy chủ MCP cục bộ](https://modelcontextprotocol.io/docs/develop/connect-local-servers) hoặc [tiện ích mở rộng Desktop (Desktop extension \- DXT)](https://www.anthropic.com/engineering/desktop-extensions) sẽ cho phép bạn kết nối và kiểm thử các công cụ trong Claude Code hoặc ứng dụng Claude Desktop.

Để kết nối máy chủ MCP cục bộ của bạn với Claude Code, hãy chạy lệnh claude mcp add \<name\> \<command\> \[args...\].

Để kết nối máy chủ MCP cục bộ hoặc DXT của bạn với ứng dụng Claude Desktop, hãy điều hướng đến Settings \> Developer hoặc Settings \> Extensions.

Các công cụ cũng có thể được truyền trực tiếp vào các lệnh gọi [API của Anthropic](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) để kiểm thử theo chương trình.

Hãy tự mình kiểm thử các công cụ để xác định bất kỳ điểm nào chưa hoàn thiện. Thu thập phản hồi từ người dùng của bạn để xây dựng trực giác về các trường hợp sử dụng và các prompt mà bạn mong đợi công cụ của mình sẽ hỗ trợ.

![][image2]

#### **Chạy một Bài Đánh giá**

Tiếp theo, bạn cần đo lường mức độ Claude sử dụng các công cụ của bạn bằng cách chạy một bài đánh giá. Bắt đầu bằng cách tạo ra nhiều tác vụ đánh giá, dựa trên các ứng dụng thực tế. Chúng tôi khuyên bạn nên hợp tác với một agent để giúp phân tích kết quả và xác định cách cải thiện công cụ. Xem toàn bộ quy trình này trong [sổ tay đánh giá công cụ (tool evaluation cookbook) của chúng tôi](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_evaluation/tool_evaluation.ipynb).

##### **Tạo Tác vụ Đánh giá**

Với bản mẫu ban đầu của bạn, Claude Code có thể nhanh chóng khám phá các công cụ và tạo ra hàng chục cặp prompt và phản hồi. Các prompt nên được lấy cảm hứng từ các ứng dụng thực tế và dựa trên các nguồn dữ liệu và dịch vụ thực tế (ví dụ: cơ sở kiến thức nội bộ và các microservice). Chúng tôi khuyên bạn nên tránh các môi trường "sandbox" quá đơn giản hoặc hời hợt, không đủ độ phức tạp để kiểm tra kỹ lưỡng các công cụ của bạn. Các tác vụ đánh giá tốt có thể yêu cầu nhiều lệnh gọi công cụ—có thể là hàng chục.

Dưới đây là một số ví dụ về các **tác vụ tốt**:

* Lên lịch một cuộc họp với Jane vào tuần tới để thảo luận về dự án Acme Corp mới nhất của chúng ta. Đính kèm ghi chú từ cuộc họp kế hoạch dự án lần trước và đặt một phòng hội nghị.  
* Khách hàng có ID 9182 báo cáo rằng họ đã bị tính phí ba lần cho một lần thử mua hàng. Tìm tất cả các mục log liên quan và xác định xem có khách hàng nào khác bị ảnh hưởng bởi vấn đề tương tự không.  
* Khách hàng Sarah Chen vừa gửi yêu cầu hủy dịch vụ. Chuẩn bị một đề nghị giữ chân khách hàng. Xác định: (1) tại sao họ rời đi, (2) đề nghị giữ chân nào sẽ hấp dẫn nhất, và (3) bất kỳ yếu tố rủi ro nào chúng ta cần lưu ý trước khi đưa ra đề nghị.

Và đây là một số **tác vụ yếu hơn**:

* Lên lịch một cuộc họp với jane@acme.corp vào tuần tới.  
* Tìm kiếm trong log thanh toán cho purchase\_complete và customer\_id=9182.  
* Tìm yêu cầu hủy dịch vụ theo ID khách hàng 45892\.

Mỗi prompt đánh giá nên đi kèm với một phản hồi hoặc kết quả có thể xác minh được. Trình xác minh của bạn có thể đơn giản như so sánh chuỗi chính xác giữa kết quả thực tế và các phản hồi được lấy mẫu, hoặc phức tạp như nhờ Claude đánh giá phản hồi. Tránh các trình xác minh quá khắt khe, từ chối các phản hồi đúng do các khác biệt không đáng kể như định dạng, dấu câu, hoặc các cách diễn đạt thay thế hợp lệ khác.

Đối với mỗi cặp prompt-phản hồi, bạn cũng có thể tùy chọn chỉ định các công cụ mà bạn mong đợi một agent sẽ gọi để giải quyết tác vụ, nhằm đo lường xem các agent có nắm bắt thành công mục đích của từng công cụ trong quá trình đánh giá hay không. Tuy nhiên, vì có thể có nhiều cách hợp lệ để giải quyết các tác vụ một cách chính xác, hãy cố gắng tránh chỉ định quá chi tiết hoặc khớp mẫu quá mức (overfitting) với các chiến lược.

##### **Chạy Bài Đánh giá**

Chúng tôi khuyên bạn nên chạy bài đánh giá của mình theo chương trình với các lệnh gọi API LLM trực tiếp. Sử dụng các vòng lặp agentic đơn giản (vòng lặp while bao bọc các lệnh gọi API LLM và công cụ xen kẽ): một vòng lặp cho mỗi tác vụ đánh giá. Mỗi agent đánh giá nên được cung cấp một prompt tác vụ duy nhất và các công cụ của bạn.

Trong các system prompt của các agent đánh giá, chúng tôi khuyên bạn nên hướng dẫn agent không chỉ xuất ra các khối phản hồi có cấu trúc (để xác minh), mà còn cả các khối lý luận và phản hồi. Hướng dẫn agent xuất ra những khối này *trước* các khối gọi công cụ và phản hồi có thể làm tăng trí thông minh hiệu quả của LLM bằng cách kích hoạt hành vi chuỗi tư duy (Chain-of-Thought \- CoT).

Nếu bạn đang chạy bài đánh giá với Claude, bạn có thể bật tính năng [tư duy xen kẽ (interleaved thinking)](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) để có chức năng tương tự "có sẵn". Điều này sẽ giúp bạn thăm dò lý do tại sao các agent gọi hoặc không gọi một số công cụ nhất định và làm nổi bật các lĩnh vực cần cải thiện cụ thể trong mô tả và đặc tả của công cụ.

Ngoài độ chính xác tổng thể, chúng tôi khuyên bạn nên thu thập các chỉ số khác như tổng thời gian chạy của từng lệnh gọi công cụ và tác vụ, tổng số lệnh gọi công cụ, tổng lượng token tiêu thụ và các lỗi công cụ. Việc theo dõi các lệnh gọi công cụ có thể giúp tiết lộ các luồng công việc phổ biến mà các agent theo đuổi và đưa ra một số cơ hội để hợp nhất các công cụ.

![][image3]

##### **Phân tích Kết quả**

Các agent là đối tác hữu ích của bạn trong việc phát hiện các vấn đề và cung cấp phản hồi về mọi thứ, từ các mô tả công cụ mâu thuẫn đến việc triển khai công cụ không hiệu quả và các schema công cụ khó hiểu. Tuy nhiên, hãy nhớ rằng những gì các agent bỏ qua trong phản hồi và câu trả lời của chúng thường có thể quan trọng hơn những gì chúng đưa vào. LLM không phải lúc nào cũng [nói ra những gì chúng nghĩ](https://www.anthropic.com/research/tracing-thoughts-language-model).

Hãy quan sát xem các agent của bạn bị bối rối hoặc nhầm lẫn ở đâu. Đọc qua phần lý luận và phản hồi (hoặc CoT) của các agent đánh giá để xác định các điểm chưa hoàn thiện. Xem lại các bản ghi thô (bao gồm các lệnh gọi công cụ và phản hồi của công cụ) để phát hiện bất kỳ hành vi nào không được mô tả rõ ràng trong CoT của agent. Hãy đọc giữa các dòng; hãy nhớ rằng các agent đánh giá của bạn không nhất thiết biết câu trả lời và chiến lược chính xác.

Phân tích các chỉ số gọi công cụ của bạn. Nhiều lệnh gọi công cụ dư thừa có thể cho thấy cần phải điều chỉnh lại các tham số phân trang hoặc giới hạn token; nhiều lỗi công cụ do tham số không hợp lệ có thể cho thấy các công cụ cần mô tả rõ ràng hơn hoặc ví dụ tốt hơn. Khi chúng tôi ra mắt [công cụ tìm kiếm web của Claude](https://www.anthropic.com/news/web-search), chúng tôi đã xác định rằng Claude đã thêm 2025 một cách không cần thiết vào tham số query của công cụ, làm sai lệch kết quả tìm kiếm và làm giảm hiệu suất (chúng tôi đã định hướng Claude đi đúng hướng bằng cách cải thiện mô tả công cụ).

#### **Hợp tác với các Agent**

Bạn thậm chí có thể để các agent phân tích kết quả và tự cải thiện các công cụ cho bạn. Đơn giản chỉ cần nối các bản ghi từ các agent đánh giá của bạn và dán chúng vào Claude Code. Claude là một chuyên gia trong việc phân tích các bản ghi và tái cấu trúc (refactoring) nhiều công cụ cùng một lúc—ví dụ, để đảm bảo việc triển khai và mô tả công cụ luôn nhất quán với nhau khi có những thay đổi mới.

Thực tế, hầu hết các lời khuyên trong bài viết này đều đến từ việc tối ưu hóa lặp đi lặp lại các triển khai công cụ nội bộ của chúng tôi với Claude Code. Các bài đánh giá của chúng tôi được tạo ra dựa trên không gian làm việc nội bộ, phản ánh sự phức tạp của các quy trình làm việc nội bộ, bao gồm các dự án, tài liệu và tin nhắn thực tế.

Chúng tôi đã dựa vào các tập dữ liệu kiểm tra riêng (held-out test sets) để đảm bảo không bị overfitting với các bài đánh giá "đào tạo" của mình. Các tập kiểm tra này cho thấy chúng tôi có thể đạt được những cải tiến hiệu suất bổ sung ngay cả ngoài những gì chúng tôi đã đạt được với các triển khai công cụ "chuyên gia"—cho dù những công cụ đó được các nhà nghiên cứu của chúng tôi viết thủ công hay do chính Claude tạo ra.

Trong phần tiếp theo, chúng tôi sẽ chia sẻ một số những gì chúng tôi đã học được từ quá trình này.

### **Các Nguyên tắc để Viết Công cụ Hiệu quả**

Trong phần này, chúng tôi chắt lọc những gì đã học được thành một vài nguyên tắc chỉ đạo để viết các công cụ hiệu quả.

#### **Lựa chọn Công cụ Phù hợp cho các Agent**

Nhiều công cụ hơn không phải lúc nào cũng mang lại kết quả tốt hơn. Một lỗi phổ biến mà chúng tôi quan sát được là các công cụ chỉ đơn thuần bọc lại chức năng phần mềm hoặc các điểm cuối API hiện có—bất kể các công cụ đó có phù hợp với agent hay không. Điều này là do các agent có những "khả năng nhận thức về hành động" (affordances) khác biệt so với phần mềm truyền thống—tức là, chúng có những cách khác nhau để nhận thức các hành động tiềm năng mà chúng có thể thực hiện với các công cụ đó.

Các agent LLM có "ngữ cảnh" (context) hạn chế (tức là có giới hạn về lượng thông tin chúng có thể xử lý cùng một lúc), trong khi bộ nhớ máy tính thì rẻ và dồi dào. Hãy xem xét tác vụ tìm kiếm một liên hệ trong danh bạ. Các chương trình phần mềm truyền thống có thể lưu trữ và xử lý hiệu quả một danh sách các liên hệ lần lượt, kiểm tra từng liên hệ trước khi chuyển sang liên hệ tiếp theo.

Tuy nhiên, nếu một agent LLM sử dụng một công cụ trả về TẤT CẢ các liên hệ và sau đó phải đọc qua từng liên hệ theo từng token, nó đang lãng phí không gian ngữ cảnh hạn chế của mình vào thông tin không liên quan (hãy tưởng tượng việc tìm kiếm một liên hệ trong danh bạ của bạn bằng cách đọc từng trang từ trên xuống dưới—tức là, thông qua tìm kiếm brute-force). Cách tiếp cận tốt hơn và tự nhiên hơn (cho cả agent và con người) là chuyển thẳng đến trang liên quan trước (có lẽ tìm nó theo thứ tự bảng chữ cái).

Chúng tôi khuyên bạn nên xây dựng một vài công cụ được suy nghĩ kỹ lưỡng, nhắm vào các quy trình công việc cụ thể có tác động cao, phù hợp với các tác vụ đánh giá của bạn và mở rộng từ đó. Trong trường hợp danh bạ, bạn có thể chọn triển khai công cụ Contactss hoặc message\_contact thay vì công cụ list\_contacts.

Các công cụ có thể hợp nhất chức năng, xử lý tiềm năng *nhiều* hoạt động riêng lẻ (hoặc các lệnh gọi API) bên trong. Ví dụ, các công cụ có thể làm phong phú phản hồi của công cụ bằng siêu dữ liệu liên quan hoặc xử lý các tác vụ đa bước thường được kết nối với nhau trong một lệnh gọi công cụ duy nhất.

Dưới đây là một số ví dụ:

* Thay vì triển khai các công cụ list\_users, list\_events, và create\_event, hãy xem xét triển khai một công cụ schedule\_event có khả năng tìm kiếm thời gian trống và lên lịch một sự kiện.  
* Thay vì triển khai một công cụ read\_logs, hãy xem xét triển khai một công cụ search\_logs chỉ trả về các dòng log liên quan và một số ngữ cảnh xung quanh.  
* Thay vì triển khai các công cụ get\_customer\_by\_id, list\_transactions, và list\_notes, hãy triển khai một công cụ get\_customer\_context có khả năng tổng hợp tất cả thông tin gần đây và liên quan của một khách hàng cùng một lúc.

Hãy đảm bảo mỗi công cụ bạn xây dựng đều có một mục đích rõ ràng, khác biệt. Các công cụ nên cho phép các agent chia nhỏ và giải quyết các tác vụ theo cách tương tự như một con người sẽ làm, nếu được cung cấp quyền truy cập vào các tài nguyên cơ bản giống nhau, và đồng thời giảm bớt ngữ cảnh mà lẽ ra đã bị tiêu thụ bởi các kết quả trung gian.

Quá nhiều công cụ hoặc các công cụ có chức năng trùng lặp cũng có thể làm các agent sao lãng khỏi việc theo đuổi các chiến lược hiệu quả. Việc lập kế hoạch cẩn thận, có chọn lọc cho các công cụ bạn xây dựng (hoặc không xây dựng) thực sự có thể mang lại hiệu quả lớn.

#### **Phân chia Không gian tên (Namespacing) cho các Công cụ của bạn**

Các agent AI của bạn có thể sẽ có quyền truy cập vào hàng chục máy chủ MCP và hàng trăm công cụ khác nhau—bao gồm cả những công cụ của các nhà phát triển khác. Khi các công cụ trùng lặp về chức năng hoặc có mục đích không rõ ràng, các agent có thể bị bối rối về việc nên sử dụng công cụ nào.

Việc phân chia không gian tên (namespacing) (nhóm các công cụ liên quan dưới các tiền tố chung) có thể giúp phân định ranh giới giữa nhiều công cụ; các client MCP đôi khi làm điều này theo mặc định. Ví dụ, việc phân chia không gian tên cho các công cụ theo dịch vụ (ví dụ: asana\_search, jira\_search) và theo tài nguyên (ví dụ: asana\_projects\_search, asana\_users\_search), có thể giúp các agent chọn đúng công cụ vào đúng thời điểm.

Chúng tôi đã nhận thấy việc lựa chọn giữa việc phân chia không gian tên dựa trên tiền tố và hậu tố có những ảnh hưởng không nhỏ đến các bài đánh giá về việc sử dụng công cụ của chúng tôi. Các ảnh hưởng này thay đổi tùy theo LLM và chúng tôi khuyến khích bạn chọn một lược đồ đặt tên phù hợp với các bài đánh giá của riêng bạn.

Các agent có thể gọi sai công cụ, gọi đúng công cụ với các tham số sai, gọi quá ít công cụ, hoặc xử lý phản hồi của công cụ không chính xác. Bằng cách triển khai có chọn lọc các công cụ có tên phản ánh sự phân chia tự nhiên của các tác vụ, bạn đồng thời giảm số lượng công cụ và mô tả công cụ được tải vào ngữ cảnh của agent và chuyển gánh nặng tính toán của agent từ ngữ cảnh của nó trở lại vào chính các lệnh gọi công cụ. Điều này làm giảm nguy cơ mắc lỗi tổng thể của một agent.

#### **Trả về Ngữ cảnh Có ý nghĩa từ các Công cụ của bạn**

Tương tự, việc triển khai công cụ cần cẩn thận để chỉ trả về thông tin có giá trị cao cho các agent. Chúng nên ưu tiên sự liên quan về mặt ngữ cảnh hơn là tính linh hoạt, và tránh các định danh kỹ thuật cấp thấp (ví dụ: uuid, 256px\_image\_url, mime\_type). Các trường như name, image\_url, và file\_type có nhiều khả năng cung cấp thông tin trực tiếp cho các hành động và phản hồi tiếp theo của agent hơn.

Các agent cũng có xu hướng xử lý các tên, thuật ngữ hoặc định danh bằng ngôn ngữ tự nhiên thành công hơn đáng kể so với các định danh khó hiểu. Chúng tôi đã nhận thấy rằng chỉ cần giải quyết các UUID chữ và số tùy ý thành ngôn ngữ có ý nghĩa và dễ diễn giải hơn (hoặc thậm chí là một lược đồ ID dựa trên chỉ số từ 0\) cũng đã cải thiện đáng kể độ chính xác của Claude trong các tác vụ truy xuất bằng cách giảm thiểu việc tạo ra ảo giác.

Trong một số trường hợp, các agent có thể yêu cầu sự linh hoạt để tương tác với cả đầu ra là ngôn ngữ tự nhiên và định danh kỹ thuật, dù chỉ để kích hoạt các lệnh gọi công cụ tiếp theo (ví dụ: search\_user(name='jane') → send\_message(id=12345)). Bạn có thể cho phép cả hai bằng cách cung cấp một tham số enum response\_format đơn giản trong công cụ của mình, cho phép agent kiểm soát xem công cụ sẽ trả về phản hồi "concise" (ngắn gọn) hay "detailed" (chi tiết).

Bạn có thể thêm nhiều định dạng hơn để có sự linh hoạt cao hơn, tương tự như GraphQL nơi bạn có thể chọn chính xác những mẩu thông tin bạn muốn nhận. Dưới đây là một ví dụ về enum ResponseFormat để kiểm soát độ chi tiết của phản hồi công cụ:

enum ResponseFormat {  
    DETAILED \= "detailed",  
    CONCISE \= "concise"  
}

Ở đây, một ví dụ về phản hồi công cụ chi tiết (206 mã thông báo):  
![][image4]

Ở đây, một ví dụ về phản hồi công cụ ngắn gọn (72 mã thông báo):

![][image5]

Các luồng (threads) và các câu trả lời trong luồng được xác định bởi một `thread_ts` duy nhất; đây là ID bắt buộc để truy xuất các câu trả lời. `thread_ts` và các ID khác (`channel_id`, `user_id`) có thể được lấy từ phản hồi chi tiết của công cụ (`detailed` response) để thực hiện các lệnh gọi công cụ tiếp theo yêu cầu chúng. Ngược lại, các phản hồi ngắn gọn (`concise` response) chỉ trả về nội dung của luồng và lược bỏ các ID này. Trong ví dụ này, việc sử dụng phản hồi ngắn gọn giúp chúng ta chỉ tiêu tốn khoảng ⅓ lượng token.

**Ví dụ về phản hồi công cụ chi tiết (206 token):**

{  
  "threads": \[  
    {  
      "thread\_ts": "1735089600.123456",  
      "channel\_id": "C1234567890",  
      "user\_id": "U0987654321",  
      "user\_name": "john.doe",  
      "timestamp": "2024-12-25T00:00:00Z",  
      "message": "Hey team, quick question about the project timeline...",  
      "replies\_count": 3,  
      "participants": \["U0987654321", "U1122334455"\],  
      "latest\_reply": "2024-12-25T01:30:00Z"  
    }  
  \]  
}

**Ví dụ về phản hồi công cụ ngắn gọn (72 token):**

{  
  "threads": \[  
    {  
      "user\_name": "john.doe",  
      "timestamp": "2024-12-25T00:00:00Z",  
      "message": "Hey team, quick question about the project timeline...",  
      "replies\_count": 3  
    }  
  \]  
}

Ngay cả cấu trúc phản hồi của công cụ của bạn—ví dụ: XML, JSON, hoặc Markdown—cũng có thể có tác động đến hiệu suất đánh giá: không có giải pháp nào phù hợp cho mọi trường hợp. Điều này là do các LLM được huấn luyện dựa trên dự đoán token tiếp theo và có xu hướng hoạt động tốt hơn với các định dạng phù hợp với dữ liệu huấn luyện của chúng. Cấu trúc phản hồi tối ưu sẽ thay đổi rất nhiều tùy theo tác vụ và agent. Chúng tôi khuyến khích bạn chọn cấu trúc phản hồi tốt nhất dựa trên bài đánh giá của riêng bạn.

#### **Tối ưu hóa Phản hồi Công cụ để Tiết kiệm Token**

Tối ưu hóa chất lượng của ngữ cảnh là quan trọng. Nhưng tối ưu hóa *số lượng* ngữ cảnh được trả về cho các agent trong các phản hồi của công cụ cũng quan trọng không kém.

Chúng tôi đề nghị triển khai một sự kết hợp nào đó giữa phân trang, lựa chọn phạm vi, lọc, và/hoặc cắt ngắn với các giá trị tham số mặc định hợp lý cho bất kỳ phản hồi công cụ nào có thể sử dụng nhiều ngữ cảnh. Đối với Claude Code, chúng tôi giới hạn phản hồi của công cụ ở mức 25,000 token theo mặc định. Chúng tôi kỳ vọng độ dài ngữ cảnh hiệu quả của các agent sẽ tăng theo thời gian, nhưng nhu cầu về các công cụ tiết kiệm ngữ cảnh vẫn sẽ tồn tại.

Nếu bạn chọn cắt ngắn phản hồi, hãy chắc chắn hướng dẫn các agent bằng những chỉ dẫn hữu ích. Bạn có thể trực tiếp khuyến khích các agent theo đuổi các chiến lược tiết kiệm token hơn, như thực hiện nhiều tìm kiếm nhỏ và có mục tiêu thay vì một tìm kiếm rộng lớn duy nhất cho một tác vụ truy xuất kiến thức. Tương tự, nếu một lệnh gọi công cụ gây ra lỗi (ví dụ, trong quá trình xác thực đầu vào), bạn có thể sử dụng kỹ thuật prompt cho các phản hồi lỗi của mình để truyền đạt rõ ràng các cải tiến cụ thể và có thể hành động, thay vì các mã lỗi hoặc traceback khó hiểu.

**Ví dụ về phản hồi công cụ bị cắt ngắn:**

**![][image6]**

{  
  "results": \[  
    {"id": 1, "title": "Project Alpha Meeting Notes", "date": "2024-12-20"},  
    {"id": 2, "title": "Budget Review Q4", "date": "2024-12-19"},  
    "... (showing first 10 of 847 results)"  
  \],  
  "metadata": {  
    "total\_results": 847,  
    "showing": 10,  
    "truncated": true,  
    "suggestion": "Use more specific search terms or add filters to narrow results"  
  }  
}

**Ví dụ về phản hồi lỗi không hữu ích:**

**![][image7]**

{  
  "error": "ValidationError: Invalid input",  
  "code": 400  
}

**Ví dụ về phản hồi lỗi hữu ích:**

**![][image8]**

{  
  "error": "Invalid date format in 'start\_date' parameter",  
  "message": "Expected format: YYYY-MM-DD (e.g., '2024-12-25')",  
  "received": "12/25/2024",  
  "suggestion": "Please reformat the date and try again"  
}

#### **Kỹ thuật Prompt (Prompt-Engineering) cho các Mô tả Công cụ của bạn**

Bây giờ chúng ta đến với một trong những phương pháp hiệu quả nhất để cải thiện công cụ: kỹ thuật prompt cho các mô tả và đặc tả của công cụ. Bởi vì những thông tin này được tải vào ngữ cảnh của agent, chúng có thể cùng nhau định hướng agent hướng tới các hành vi gọi công cụ hiệu quả.

Khi viết mô tả và đặc tả công cụ, hãy nghĩ xem bạn sẽ mô tả công cụ của mình cho một nhân viên mới trong nhóm như thế nào. Hãy xem xét ngữ cảnh mà bạn có thể ngầm hiểu—các định dạng truy vấn chuyên biệt, định nghĩa về thuật ngữ chuyên ngành, mối quan hệ giữa các tài nguyên cơ bản—và làm cho nó trở nên rõ ràng. Tránh sự mơ hồ bằng cách mô tả rõ ràng (và thực thi bằng các mô hình dữ liệu nghiêm ngặt) các đầu vào và đầu ra mong đợi. Đặc biệt, các tham số đầu vào nên được đặt tên một cách rõ ràng: thay vì một tham số tên là user, hãy thử một tham số tên là user\_id.

Với bài đánh giá của bạn, bạn có thể đo lường tác động của kỹ thuật prompt của mình với sự tự tin cao hơn. Ngay cả những tinh chỉnh nhỏ trong mô tả công cụ cũng có thể mang lại những cải tiến đáng kể. Claude Sonnet 3.5 đã đạt được hiệu suất hàng đầu trong bài đánh giá [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) sau khi chúng tôi thực hiện các tinh chỉnh chính xác cho các mô tả công cụ, giảm đáng kể tỷ lệ lỗi và cải thiện việc hoàn thành tác vụ.

Bạn có thể tìm thấy các phương pháp hay nhất khác cho định nghĩa công cụ trong [Hướng dẫn dành cho nhà phát triển (Developer Guide) của chúng tôi](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions). Nếu bạn đang xây dựng công cụ cho Claude, chúng tôi cũng khuyên bạn nên đọc về cách các công cụ được tải động vào [system prompt của Claude](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt). Cuối cùng, nếu bạn đang viết công cụ cho một máy chủ MCP, [chú thích công cụ (tool annotations)](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) giúp tiết lộ những công cụ nào yêu cầu quyền truy cập thế giới mở hoặc thực hiện các thay đổi có tính phá hủy.

### **Hướng tới Tương lai**

Để xây dựng các công cụ hiệu quả cho các agent, chúng ta cần định hướng lại các phương pháp phát triển phần mềm của mình từ các mẫu tất định, có thể dự đoán sang các mẫu phi tất định.

Thông qua quy trình lặp đi lặp lại, dựa trên đánh giá mà chúng tôi đã mô tả trong bài viết này, chúng tôi đã xác định được các mẫu nhất quán về những gì làm cho các công cụ thành công: Các công cụ hiệu quả được định nghĩa một cách có chủ đích và rõ ràng, sử dụng ngữ cảnh của agent một cách hợp lý, có thể được kết hợp với nhau trong các quy trình công việc đa dạng, và cho phép các agent giải quyết các tác vụ thực tế một cách trực quan.

Trong tương lai, chúng tôi kỳ vọng các cơ chế cụ thể mà qua đó các agent tương tác với thế giới sẽ phát triển—từ các bản cập nhật cho giao thức MCP đến các bản nâng cấp cho chính các LLM cơ bản. Với một phương pháp tiếp cận có hệ thống, dựa trên đánh giá để cải thiện các công cụ cho agent, chúng ta có thể đảm bảo rằng khi các agent trở nên có năng lực hơn, các công cụ mà chúng sử dụng cũng sẽ phát triển cùng với chúng.

### **Lời cảm ơn**

Được viết bởi Ken Aizawa với sự đóng góp quý báu từ các đồng nghiệp trên các bộ phận Nghiên cứu (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh, Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra, Adam Jones), Kỹ thuật Sản phẩm (Santiago Seira), Marketing (Molly Vorwerck), Thiết kế (Drew Roper), và AI Ứng dụng (Christian Ryan, Alexander Bricken).

### **Liên kết đến việc Phát triển AI Agent**

Hướng dẫn này đặc biệt phù hợp khi xây dựng các agent như dự án Boot.dev AI Agent, nơi bạn cần triển khai các hàm cốt lõi:

* get\_files\_info() \- Nên trả về thông tin thư mục có cấu trúc, ý nghĩa với các định danh bằng ngôn ngữ tự nhiên.  
* get\_file\_content() \- Phải xử lý các loại và kích thước tệp khác nhau một cách hiệu quả với phân trang/cắt ngắn.  
* write\_file() \- Cần xử lý lỗi mạnh mẽ với các thông báo lỗi hữu ích và xác nhận.  
* run\_python\_file() \- Nên ghi lại đầu ra, lỗi và ngữ cảnh thực thi với định dạng rõ ràng.

Mỗi công cụ nên tuân theo các nguyên tắc này để tạo ra một agent hiệu quả có thể thực sự hỗ trợ các tác vụ lập trình trong khi vẫn tiết kiệm token và cung cấp ngữ cảnh có ý nghĩa cho việc ra quyết định.

**Điểm mấu chốt**: Các công cụ agent hiệu quả đòi hỏi thiết kế cẩn thận, xem xét các ràng buộc và khả năng độc đáo của AI agent, nhấn mạnh sự rõ ràng, hiệu quả và xử lý lỗi mạnh mẽ hơn là các thực hành kỹ thuật phần mềm truyền thống. Phương pháp tiếp cận lặp đi lặp lại, dựa trên đánh giá với sự hợp tác của agent là điều cần thiết để tạo ra các công cụ thực sự hiệu quả.
