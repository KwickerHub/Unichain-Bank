# Contributing to Unichain Bank

Welcome to Unichain Bank! We're excited to have you contribute to our project. Before you get started, please take a moment to review our guidelines.

## Project Structure

The project is structured as follows:

- **gui**
  - **web**
    - **src**: Contains the source files for the web application.
    - **pages**: Contains HTML pages for the web application.
    - **vendors**
      - **js**: Contains pure JavaScript scripts for the web application.

- **api**
  - **python**: Contains Python files for the Flask backend, including `requirements.txt` and other Flask-related files.
  - **node**: Contains Node.js files, including `package.json`, for the backend.

## Development Setup

To set up your development environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/KwickerHub/Unichain-Bank.git
   ```

2. Install Python dependencies:

   ```bash
   cd unichain-bank/api/python
   pip install -r requirements.txt
   ```

3. Run the development server:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000` to view the app.

## How to Contribute

1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Create a new branch for your changes:

   ```bash
   git checkout -b your-branch-name
   ```

4. Make your changes and test them locally.
5. Commit your changes:

   ```bash
   git commit -am "Your commit message"
   ```

6. Push your changes to your fork:

   ```bash
   git push origin your-branch-name
   ```

7. Create a pull request (PR) on GitHub from your fork to the main repository.

## Reporting Issues

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/KwickerHub/Unichain-Bank/issues) on GitHub.

## Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing. We want all contributors to feel welcome and respected in our community.

## License

By contributing to Unichain Bank, you agree that your contributions will be licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Thank you for contributing to Unichain Bank!
