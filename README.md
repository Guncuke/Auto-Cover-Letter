# Auto-Cover-Letter

Automatically generate a cover letter based on the resume according to the input intention college and supervisor.

![demo](images\demo.png)

What do you need to pass in? Resume, serp api and openai api.

Running process:  

1. According to the target university and the teacher, go to google scholar to query the teacher information, as well as the journals published in recent years.
2. Then, the PDF passed by the user is parsed.
3. The PDF and crawled information are put into the LLM to generate recommendation letters.

TODO:

- [ ] multi-input resume
