# AI-Enhanced Pacman Game 🎮👻

This repository contains a comprehensive AI project divided into four sub-projects, each applying different AI techniques to enhance gameplay in the classic Pacman arcade game. The projects range from basic pathfinding algorithms to complex probabilistic inference for ghost hunting.

## Project Structure

### Project 1: Pathfinding and Heuristic Search 🌐
- **Objective:** Utilize classic search algorithms to enhance Pacman's food-finding capabilities.
- **Techniques Used:**
  - **DFS, BFS, A***: Basic pathfinding algorithms for navigating the maze.
  - **Heuristic Search**: Applying heuristic methods like corner approximation and comprehensive food-eating strategies.
- **Summary:** This sub-project focuses on employing various searching algorithms to solve navigation and food collection tasks efficiently.

### Project 2: Adversarial Search 🤺
- **Objective:** Improve the reflex agent to handle dynamic challenges posed by ghosts.
- **Techniques Used:**
  - **Enhanced Reflex Agent**: Improves basic agent performance by considering more game factors.
  - **Mini-Max with Ghosts**: Implementing the Mini-Max algorithm to handle potential strategies from multiple adversaries.
  - **Alpha-Beta Pruning**: Optimizing the Mini-Max algorithm to prune unlikely branches and enhance computational efficiency.
- **Summary:** Focuses on adversarial search to optimize Pacman's strategies against intelligent ghost agents.

### Project 3: Reinforcement Learning 📊
- **Objective:** Employ reinforcement learning techniques to teach Pacman optimal gameplay strategies through trial and error.
- **Techniques Used:**
  - **Exploration vs. Exploitation**: Balancing between exploring new strategies and exploiting known successful strategies.
- **Summary:** This sub-project applies reinforcement learning to adaptively improve Pacman's decision-making process based on environmental feedback.

### Project 4: Ghostbusters! 👻🔫
- **Objective:** Enable Pacman to hunt and eat weakened ghosts using probabilistic inferences.
- **Techniques Used:**
  - **Exact Inference**: Implementing precise probabilistic methods to determine the location of ghosts.
  - **Approximate Inference**: Using approximations in Bayes Networks to manage uncertainties in ghost positioning.
- **Summary:** Applies concepts from probabilistic inference to effectively track and capture ghosts under uncertain conditions.

## Technologies Used
- **Python**: Primary programming language.
- **Pygame**: Used for creating the game environment.
- **Various AI Libraries**: Supporting the implementation of algorithms and inferences.
