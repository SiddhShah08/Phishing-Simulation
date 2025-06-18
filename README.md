# Phishing Simulation Web Application

## Project Description
This is a Flask-based phishing simulation web application designed for educational and testing purposes only. The app generates unique phishing URLs that simulate login pages for various platforms such as Instagram, Facebook, and a generic login form. It captures simulated login credentials along with metadata like IP address and timestamp, and displays them on an admin dashboard.

**Important:** This project is intended solely for educational use and to raise awareness about phishing attacks. Do **NOT** use this application for any malicious or unauthorized activities.

## Features
- Generate unique phishing URLs for simulation.
- Simulated login pages for generic login, Instagram, Facebook, and Skip Connect.
- Capture and store simulated credentials with IP address and timestamp.
- Admin dashboard to view all captured credentials.
- Simple and clean user interface with responsive design.
- Data persistence using a JSON file (`data.json`).

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Steps
1. Clone or download this repository.
2. Navigate to the project directory.
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install required packages:
   ```bash
   pip install Flask
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. The home page will generate a unique phishing URL for simulation.
4. Share the generated URL to simulate login attempts.
5. Use the dashboard link to view captured credentials.

## Project Structure
```
.
├── app.py                 # Main Flask application
├── data.json              # JSON file storing captured data
├── static/
│   └── styles.css         # CSS styles
└── templates/
    ├── dashboard.html     # Admin dashboard page
    ├── facebook_connect.html
    ├── generate.html      # Phishing URL generation page
    ├── instagram_connect.html
    ├── login.html         # Generic login page
    └── skips_connect.html
```
*You can add screenshots here to illustrate the application pages and features.*

- Phishing URL Generator page
 ![image](https://github.com/user-attachments/assets/1a977b30-bd10-4d74-8831-1aa69c1952b5)

- Login simulation page
- ![image](https://github.com/user-attachments/assets/b5af5fa4-2ae2-4d74-9781-fec7c5d6b995)
![image](https://github.com/user-attachments/assets/671de493-56f3-49b8-94c1-368dfbf108a3)
![image](https://github.com/user-attachments/assets/9b49587f-7c9a-4303-9579-27a250085350)
![image](https://github.com/user-attachments/assets/670525a1-aa62-40d5-b157-b81dcb874dac)



- Admin dashboard displaying captured credentials
  ![image](https://github.com/user-attachments/assets/7fb0b9c9-a399-4126-8203-9c25acb09a9d)



## Security and Disclaimer
- This application is for educational and testing purposes only.
- Do not use this tool for any illegal or unethical activities.
- The data collected is stored locally in `data.json`.
- Use responsibly and ensure compliance with all applicable laws.

## License
This project is provided as-is without any warranty. Use at your own risk.

## Contact
For questions or feedback, please contact the project maintainer.
