# Autonomous Robot Navigation Simulator (Core Logic)

This project is a Python-based simulation of an autonomous mobile robot navigating in a 2D grid environment.  
It focuses on **core robotics logic** such as obstacle detection, movement control, and state tracking — implemented without physical hardware.

The simulation mirrors how real robots are tested in software before deploying control logic to actual hardware.

---

## 🚀 Features

- Grid-based virtual environment
- Simulated obstacle detection (ultrasonic sensor logic)
- Autonomous movement with reactive obstacle avoidance
- Direction control (North, East, South, West)
- Path tracking for analysis and visualization
- Modular and extensible design using Object-Oriented Programming

---

## 🧠 Project Design

### Environment
- Represented as a 2D grid
- `0` → Free space  
- `1` → Obstacle  
- Grid boundaries are treated as obstacles for safety

### Robot
- Maintains position `(x, y)`
- Maintains direction (`N`, `E`, `S`, `W`)
- Can:
  - Move forward
  - Turn left
  - Turn right
- Uses simulated sensor logic to detect obstacles ahead

### Navigation Logic
The robot follows a **reactive control strategy**:
1. Attempt to move forward
2. If blocked by an obstacle or boundary, turn right
3. Repeat for a fixed number of steps

This approach demonstrates basic autonomous behavior without global path planning.

---

## 🗂️ Project Structure

robot-navigation-simulator/
├── main.py          # Main control loop
├── robot.py         # Robot movement and decision logic
├── environment.py   # Grid and obstacle handling
└── README.md        # Project documentation

---

## ▶️ How to Run

1. Clone the repository:
  
   git clone https://github.com/<your-username>/robot-navigation-simulator.git

2. Navigate to the project directory:

    cd robot-navigation-simulator

3. Run the simulation:

    python main.py

## 📊 Sample Output:

Step 0: Position = (0, 1), Direction = E
Step 1: Position = (0, 1), Direction = S
Step 2: Position = (1, 1), Direction = S
...
Path taken: [(0,0), (0,1), (1,1), (2,1), ...]


## 🔌 Mapping to Real Robotics Systems

| Real Robot Component | Simulation Equivalent       |
| -------------------- | --------------------------- |
| Ultrasonic sensor    | Obstacle detection function |
| Arduino loop()       | Python control loop         |
| Motor driver         | Movement functions          |
| Odometry / encoder   | Path tracking list          |
| Serial monitor       | Console logs                |

## Known Limitations

Uses a reactive navigation strategy

No goal-based path planning (robot may enter loops)

No visual output in this version

These limitations are intentional and serve as a clean baseline for future enhancements.

## 🔮 Future Enhancements

Path visualization using Matplotlib

Real-time animation using Pygame

ROS2-based implementation using nodes and topics

Advanced navigation algorithms (BFS, A*, etc.)

## 🧩 Skills Demonstrated

Python programming

Object-Oriented Design

Robotics logic and control flow

Simulation-based testing

Problem decomposition

Clean code structure

## 👤 Author

Arulesh P P

Robotics-Oriented Python Software Engineer





