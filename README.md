# Automated Email Sender

An efficient and user-friendly **Automated Email Sender** built using **Python** and **SMTP**. This project is designed to simplify the process of sending emails in bulk or individually, with customizable messages and support for attachments.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Send Emails Individually or in Bulk**: Automate email sending for multiple recipients.
- **Customizable Messages**: Personalize the subject and body of the email.
- **Attachment Support**: Add files or documents to your emails.
- **Email Logs**: Track sent emails for reference.
- **Secure Connection**: Uses SMTP with TLS/SSL for secure email transmission.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**: smtplib, email, and ssl
- **Environment**: Any Python-supported IDE (e.g., VSCode, PyCharm)

---

## Getting Started

### Prerequisites

1. **Python Installed**: Download and install Python from [python.org](https://python.org/).
2. **Email Account**: Ensure you have access to a valid email account (e.g., Gmail, Yahoo).
3. **SMTP Server Details**: Obtain the SMTP server and port for your email provider.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Automated-Email-Sender.git
   cd Automated-Email-Sender
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Open the `config.py` file and configure your email credentials and SMTP details:
   ```python
   EMAIL_ADDRESS = "your_email@example.com"
   EMAIL_PASSWORD = "your_password"
   SMTP_SERVER = "smtp.example.com"
   SMTP_PORT = 587
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the prompts to send your emails.

---

## Screenshots

### Email Sending Interface



### Log of Sent Emails



*(Replace placeholder images with actual screenshots from your project.)*

---

## Project Structure

```
Automated-Email-Sender/
|— bulk_email_sender.py
|— recipition.csv
|— README.md         # Project documentation
|— requirements.txt  # Dependencies
```

---

## Future Enhancements

- Add a **GUI** for easier use.
- Enable **Scheduler Functionality** to send emails at specific times.
- Add support for **Multiple Email Providers**.
- Integrate **Templates** for recurring email formats.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

- **Developer**: santhoshmahendran
- **Email**: santhoshm2000411\@email.com
- **GitHub Repository**: [Automated Email Sender](https://github.com/YourUsername/Automated-Email-Sender)

---

