# Archivist Application

Archivist is a powerful tool designed for software engineers and AI researchers like Brad. It is capable of crawling the web to download code repositories, preprocessing the source code, documentation, and config files, and creating vector embeddings of the prepped files. It provides a web interface to manage these tasks and view their progress.

## Features

1. **Web Server**: Handles user interactions and manages tasks.
2. **Data Storage**: Stores vector stores, metadata, and application state.
3. **Crawler**: Downloads code repositories.
4. **Preprocessor**: Preps files for vector embedding.
5. **Embedding Creator**: Creates vector embeddings.
6. **Web Interface**: Provides a user interface for interactions.
7. **Testing System**: Handles unit tests, integration tests, and possibly performance and security tests.
8. **Deployment System**: Manages the deployment of the application and its dependencies.
9. **Versioning System**: Handles versioning of the application and any data formats or APIs it provides.
10. **Resource Management System**: Manages memory usage and handles any limits on the number of concurrent tasks.

## Requirements

- The application should be distributable via PyPI.
- The application should be fault-tolerant and handle errors gracefully.
- The application should log all activities.
- The application should keep results of scraping, track where it got documents and what vector store they went into, and keep original documents grouped per repository. Data should be kept until explicitly deleted by the user.
- The application should include metadata for all documents and vector stores that document when they were added, what repo they came from, and their place in the file structure of the repo.
- The crawls/downloads should be able to run concurrently, with a maximum of 2 repos at a time.
- Error messages or status reports should be informative.
- The application will need user guides, API documentation, developer guides, etc., but these can be worked on once the app is stable.
- The application should provide clear instructions for deployment and running by the end users, including the installation of any dependencies.
- The application should have a clear versioning strategy for both the application itself and any data formats or APIs it provides.
- The application should effectively manage resources, including memory usage and handling any limits on the number of concurrent tasks.

## Installation

The application can be installed via PyPI. More detailed instructions for deployment and running, including the installation of any dependencies, will be provided in the user guides.

## Support

If you encounter issues or have questions, please use the application's support features to request help.

## Versioning

The application has a clear versioning strategy for both the application itself and any data formats or APIs it provides. Please refer to the versioning system for more details.

## Contributing

Contributions are welcome. Please read the contributing guide for more information.

## License

Please refer to the license file for more information.
