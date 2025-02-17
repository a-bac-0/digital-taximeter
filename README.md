# Digital Taximeter Project

Welcome to the **Digital Taximeter** project! This application is designed to calculate and track taxi fares based on different conditions like movement status, area demand, and weather.

## 📄 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Development Process](#development-process)
7. [Future Improvements](#future-improvements)

---

## 📝 Project Overview

The **Digital Taximeter** project is a **command-line interface (CLI)** application that tracks and calculates taxi fares. It tracks time and costs based on various factors, including:
- Whether the taxi is moving or stationary.
- Weather conditions (e.g., rain).
- Area demand (overdemanded or underdemanded areas).
- Pauses during the trip.

This project implements an **incremental development process**, with continuous additions and enhancements for better functionality.

---

## ⚙️ Features

- **Start and stop a taxi trip**.
- **Track time** and **calculate fare** while moving or stationary.
- Ability to **pause** the trip and **resume** the fare calculation.
- Apply **surcharges** for weather conditions (rain) and area demand (over/under demand).
- Display real-time updates on fare and time tracking during the trip.

---

## 💻 Technologies

- **Programming Language**: Python
- **Data Handling**: Time and Cost calculations based on movement status
- **User Interface**: Command-line interface for user input and interaction
- **Libraries**: None (all functionality is implemented in Python standard libraries)

---

## 🛠️ Installation

To run this project locally, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/digital-taximeter.git
    ```

2. Navigate to the project directory:
    ```bash
    cd digital-taximeter
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - For Windows:
      ```bash
      venv\Scripts\activate
      ```
    - For Linux/Mac:
      ```bash
      source venv/bin/activate
      ```

---

## 🚀 Usage

### Starting a Trip
1. Run the application:
    ```bash
    python taximeter.py
    ```

2. The program will prompt you with the following options:
    - **Start Trip**: Begin tracking the trip.
    - **Is it raining? (y/n)**: Choose if it's raining (yes or no).
    - **Is the area overdemanded or underdemanded? (o/u)**: Choose if the area is experiencing high demand (o for overdemanded, u for underdemanded).
    - **Start Moving/Stationary/Pause/Finish**: Control the state of the taxi.

### Sample Interaction
```text
Menu:
1. Start Trip
2. Exit

Choose an option: 1

Welcome to the Digital Taximeter!
The taxi is now ready to start.

Is it raining? (y/n): n
Is the area overdemanded or underdemanded? (o/u): u

Tracking time... (You can interact with the program now!)

Taxi is currently stationary.
Time: 00:10 | Cost: €0.16

1. Start moving (m)
2. Pause (p)
3. Finish trip (f)
4. Resume (r, only when paused)

Choose an option: m

Taxi is now moving.
Time: 00:28 | Cost: €0.45

1. Start moving (m)
2. Pause (p)
3. Finish trip (f)
4. Resume (r, only when paused)

Choose an option: p

Taxi is paused.
Time: 00:36 | Cost: €0.58

1. Start moving (m)
2. Pause (p)
3. Finish trip (f)
4. Resume (r, only when paused)

Choose an option: r

Taxi is now resuming the trip.
Time: 00:47 | Cost: €0.75

1. Start moving (m)
2. Pause (p)
3. Finish trip (f)
4. Resume (r, only when paused)

Choose an option: f

Total time: 00:47
Total fare: €0.75

Menu:
1. Start Trip
2. Exit
Choose an option: 2

Goodbye! See you next time!
```

---

## 📈 Development Process

- **Stage 1**: Basic Time Tracking and Cost Calculation  
  Implemented basic functionality to track time and calculate fare when moving or stationary.

- **Stage 2**: Handling Dynamic States (Moving, Stationary, Paused)  
  Added functionality to handle different states: moving, stationary, paused, and the ability to resume the trip.

- **Stage 3**: Implemented Surcharges for Rain and Area Demand  
  Incorporated rain surcharges and demand-based fare modifications (overdemanded and underdemanded areas).

---

## 📋 Future Improvements

- Add a **GUI** for a more user-friendly interface.
- Integrate with a **database** to store trip data for long-term record-keeping.
- Enhance **pricing** with different rate structures based on time of day, type of service, etc.
- Optimize **performance** for handling multiple simultaneous trips or integrations with external services (e.g., GPS tracking).

---

## ✍️ License

This project is open-source and available under the **MIT License**.
