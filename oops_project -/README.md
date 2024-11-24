# **Customer Rating System**  
A Python-based project to simulate, store, and analyze customer ratings. This system demonstrates object-oriented programming (OOP) concepts and data manipulation techniques using Python and pandas. It is designed to generate synthetic customer data, save it in a structured format (CSV), and analyze it for insights such as identifying customers with high ratings.

---

## **Table of Contents**
1. [Overview](#overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Project Structure](#project-structure)  
5. [Installation](#installation)  
6. [Usage](#usage)  
7. [Example Output](#example-output)  
8. [Future Enhancements](#future-enhancements)  
9. [Screenshots](#screenshots)  
10. [License](#license)  

---

## **1. Overview**
The **Customer Rating System** aims to automate the process of generating random customer data, storing it, and analyzing it to identify high-value customers. The project is ideal for demonstrating how Python can be used for tasks like random data generation, file handling, and simple data analysis.

This project showcases:  
- The use of Python’s `random` and `string` libraries for generating synthetic data.  
- Effective storage of data using pandas DataFrames and CSV files.  
- An OOP-based design for managing customer information and processing data.

---

## **2. Features**
- **Random Data Generation**:
  - Generates realistic customer information such as:
    - Customer ID (4-digit unique number).
    - Name (randomly generated alphabetic string).
    - Age (between 18 and 65).
    - Mobile Number (10-digit number).
    - Rating (floating-point value between 1 and 5).
- **CSV File Storage**:
  - Stores the generated data into a CSV file for persistence.
- **Data Analysis**:
  - Filters and identifies customers with ratings greater than or equal to 3.5.
  - Displays the high-rated customers in a readable format.

---

## **3. Technologies Used**
- **Programming Language**: Python 3.8+  
- **Libraries**:  
  - `pandas`: For handling data storage and analysis.  
  - `random` and `string`: For generating synthetic data.  
- **File Format**: CSV (Comma-Separated Values) for structured data storage.

---

## **4. Project Structure**

---
## **5. Installation**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/chiraniadhruv7/Customer-Rating-System.git
cd Customer-Rating-System
```
### **Step 2: Install Dependencies**
Make sure Python is installed on your system. Install the required library:
```bash
pip install pandas
```
---
## **6. Usage**
1. **Run the Python Script**:  
   Execute the main Python script to generate and analyze customer data.
   ```bash
   python customer_ratings.py
---
## **8. Future Enhancements**
This project can be extended with additional features:
1. **Real-Time Data Collection**: Integrate APIs to fetch real customer feedback dynamically.  
2. **Data Visualization**: Use tools like Matplotlib or Seaborn to visualize customer ratings.  
3. **Machine Learning**: Predict customer satisfaction levels based on historical data.  
4. **Web Integration**: Create a web interface to upload CSV files and display results.  




