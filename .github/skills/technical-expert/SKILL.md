---
name: technical-expert
description: 'Search into technical documentation and provide expert-level insights. Use when user asks for technical analysis, debugging help, or needs expert-level understanding of code or systems.'
---

# Get the technical documentations
If your ./asset/ directory in empty, search for it using the /context7 skill and put it in the ./asset/ directory. If the skill didn't succeed to get documentation, stop and don't try to answer.

If it's already there, use it to answer the question.

# Search into technical documentation to answer the question.

Use the /documentation-parser skill to parse the documentation stored into the ./asset/ directory and extract relevant information to answer the user's question.