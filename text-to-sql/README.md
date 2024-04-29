# Text to SQL: Analyzing Datasets with LLM Design Patterns

This example demonstrates the use of the Large Language Model (LLM) design pattern of text-to-SQL for analyzing SQL databases. It provides a set of Jupyter Notebooks that utilize Anthropic Claude 3 models hosted on Amazon Bedrock to analyze user questions and translate them into SQL queries that can be executed against a database.

## Features

1. **Text-to-SQL with Claude3, SQLite, and LangChain**: The first notebook, titled "01-text-to-sql-with-claude3-sqlite-langchain," showcases how to use a large language model in conjunction with SQLite and LangChain to convert natural language queries into SQL queries and interact with a local SQLite database.

2. **Text-to-SQL with Claude3, SQLite, LangChain, and Custom Prompt**: The second notebook, titled "02-text-to-sql-with-claude3-sqlite-langchain-and-custom-prompt," builds upon the first notebook by incorporating a set of custom prompt to enhance the text-to-SQL capabilities.

3. **Tunisia's Economic Data**: The example uses Tunisia's economic data as the dataset for exploration, providing a real-world context for understanding and applying the text-to-SQL techniques.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies specified in the `requirements.txt` file.
3. Set up the necessary credentials and configurations for accessing the Claude 3 models on Amazon Bedrock, as well as Amazon S3 and Athena (if applicable).
4. Open the Jupyter Notebooks and follow the instructions within each notebook to run the examples and explore the text-to-SQL capabilities.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
