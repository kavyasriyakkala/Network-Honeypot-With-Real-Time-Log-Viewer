Honeypot Project is a simple network security tool that captures and analyzes suspicious traffic. This project demonstrates a practical implementation of a honeypot—a security mechanism used to attract, detect, and investigate unauthorized access attempts or malicious activity.

Key Features:

1) Honeypot Server: Utilizes Python's socket library to create a TCP server that listens on port 8080. It captures incoming connections, logs the data, and provides valuable insights into network attacks.
  
2) Log Viewer: A Flask-powered web application that displays captured log entries in a user-friendly table format. The interface allows easy examination of attack data and network activity.

3) Summary Page: An interactive summary page aggregates key statistics from the log data, such as the total number of attacks and unique IP addresses, providing a high-level view of the network's threat landscape.

4) Responsive Design: Features a modern and aesthetic UI using Bootstrap and Tailwind CSS. Includes a clean start page with a central button for navigation, a well-organized log table, and a summary page with dynamic data display.


start page:
![image](https://github.com/user-attachments/assets/b4babbd4-ad0c-4a85-b312-5f17ca576838)

log page:
![image](https://github.com/user-attachments/assets/43e1b923-613d-4d32-8c69-01d18e35f38c)

summary page:
![image](https://github.com/user-attachments/assets/357fc364-1395-48d9-be13-fbc30b36a0b4)
