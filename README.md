#  Bowling Game Scorer

A Python implementation of the **Bowling Game Scorer** developed as part of the **Experis Game Solutions Coding Exercise**.

The objective of this project is to calculate the **cumulative bowling score after every frame** while following the official bowling scoring rules and validating invalid game inputs before scoring.

The application is designed using **Object-Oriented Programming (OOP)** principles by separating responsibilities into dedicated modules for parsing, validation, scoring, models, and utilities, making the project easy to maintain, extend, and test.

> **Input Style Chosen:** **Option A (Frames)**

---

#  Table of Contents

- Overview
- Features
- Solution Design
- Project Architecture
- Folder Structure
- Module Responsibilities
- Scoring Logic
- Validation Rules
- Testing Strategy
- Installation
- Running the Application
- Running Tests
- Allure Report
- CI/CD
- Technologies Used

---

# Problem Statement

A bowling game consists of **10 frames**, where each frame can be:

- Open Frame
- Spare
- Strike

The application should

- Accept a bowling game as input
- Validate the game according to bowling rules
- Calculate the score of every frame
- Return the **cumulative score after each frame**
- Raise meaningful exceptions for invalid games

---

# Features

✔ Supports **Option A (Frames)** input format

✔ Calculates cumulative score after every frame

✔ Implements official bowling scoring rules

- Strike
- Spare
- Open Frame
- Tenth Frame Bonus Rules

✔ Comprehensive input validation

✔ Custom exception hierarchy

✔ Modular Object-Oriented Design

✔ Automated testing using **Pytest**

✔ Allure Reporting

✔ Parameterized Test Execution

✔ GitHub Actions CI/CD *(Configured separately)*

---

#  Solution Design

Instead of implementing everything inside one file, the project follows a layered architecture where every module has a single responsibility.

Each component performs one job and passes the result to the next component.

```

              Raw Input
                  |
                  |
            Game Parser
                  |
                  |
             Game Object
         (Game -> Frame -> Roll)
                  |
                  |
          Game Validator
                  |
          Valid Bowling Game
                  |
                  |
          Bowling Scorer
                  |
                  |
        Cumulative Scores

```

This design keeps

- Parsing independent
- Validation independent
- Scoring independent

making the project easier to maintain and extend.

---

#  Why this Design?

Instead of working directly with nested Python lists throughout the application, the input is converted into **domain objects**.



This approach provides

- Better readability
- Better maintainability
- Cleaner business logic
- Easier testing
- Clear separation of concerns

---

# Project Structure

Please  Clone this in Pycharm to see folder structure 

---

#  Module Responsibilities

## Engine

The **engine** package contains the core application logic.

### constants.py

Stores all bowling constants used throughout the project which is provided in PDF.

Examples

- Strike Symbol
- Spare Symbol
- Maximum Pins
- Total Frames
- Valid Bowling Symbols

Keeping constants in one location avoids hardcoding values throughout the application.

---

### parser.py

Responsible for converting the raw input into application objects.

Instead of scoring nested lists directly,

This keeps the scoring engine completely independent of the input format.

---

### scorer.py

This is the heart of the application.

Responsibilities

- Validate the game before scoring
- Calculate frame scores
- Calculate strike bonus
- Calculate spare bonus
- Calculate open frame score
- Handle 10th frame scoring
- Return cumulative score after every frame

The scorer never performs validation itself.

Instead,

```

Game ->Validator -> Valid Game ->Scorer

```

This keeps both modules focused on a single responsibility.

---

## Models

The models package represents the bowling game as objects.

### Game

Represents the complete bowling game.

Stores all frames.

---

### Frame

Represents a single bowling frame.

Stores all rolls belonging to that frame.

---

### Roll

Represents one bowling roll.

Stores the bowling symbol (X, /, or numeric value).

Together these three classes create a clean object hierarchy that simplifies validation and scoring.

---

## Validator

The validator ensures that only valid bowling games are scored.

Every game passes through validation before any score is calculated.

```

Game -> Validator -> Scorer

```

This prevents invalid data from reaching the scoring engine.

---

## Helper

Contains reusable utility methods shared by multiple modules.

Examples

- Detect Strike
- Detect Spare
- Convert symbols into pin values

Instead of repeating this logic throughout the project, it is centralized inside the helper class.

---

## Exception Handling

The project uses a dedicated exception hierarchy instead of generic Python exceptions.

Examples include

- InvalidGameError
- InvalidFrameError
- InvalidRollError
- InvalidSymbolError
- InvalidFrameCountError

This produces meaningful error messages and makes debugging easier.

---

# Bowling Scoring Logic

The scoring engine evaluates one frame at a time and determines whether the current frame is an **Open Frame**, **Spare**, **Strike**, or the **Tenth Frame**.

Before scoring begins, every game is validated to ensure that only valid bowling games are processed.

The scoring workflow is shown below.

```
                  Game
                    |
                    |
           Validate Bowling Game
                    |
                    |
          Iterate Through Frames
                    │
        --------------------------
        |           |            |
     Strike      Spare      Open Frame
        |           |            |
        ------------|-------------
                    |
          Calculate Frame Score
                    |
                    |
         Update Running Total
                    |
                    |
      Store Cumulative Frame Score
```

The scorer continues this process until all ten frames have been evaluated.

---


#  Validation Flow

Validation is completely separated from scoring.

Every game is validated before the scoring engine starts.

```
Start -> Validate Frame Count ->Validate Symbols ->Validate Frames 1-9 -> Validate Tenth Frame -> Valid Game -> Start Scoring

```

This design prevents invalid games from reaching the scoring engine.

---

#  Validation Rules Implemented

The validator checks every game against official bowling rules.

### Game Validation

- Game must contain exactly **10 frames**

---

### Symbol Validation

Only the following symbols are accepted.

```
X
x
/
0-9
```

Any other symbol raises an **InvalidSymbolError**.

---

### Regular Frame Validation

Frames 1 through 9 are validated using the following rules.

- Single roll must be a strike
- Regular frame must contain one or two rolls
- Spare cannot be the first roll
- Strike cannot be the second roll
- Open frame pin count cannot exceed ten

---

### Tenth Frame Validation

The final frame follows special validation rules.

- Frame must contain two or three rolls
- Spare cannot be the first roll
- Strike allows two bonus rolls
- Spare allows one bonus roll
- Open frame cannot contain bonus rolls
- Open frame pin count cannot exceed ten

---

# Testing Strategy

Testing is divided into multiple layers to improve readability and maintainability.

```
                 Test Data
          ----------|--------
          |                 |
   Valid Games        Invalid Games
          |                 |
          |                 |
      Pytest Fixtures (conftest.py)
                  |
                  |
         Individual Test Files
                  |
                  |
          Parameterized Tests
```

Separating test data from test logic makes it easier to add new scenarios without modifying the test implementation.

---

# Test Data Design

The project separates reusable test data into dedicated modules.

### valid_games.py

Contains all valid bowling games.

Examples

- Example Game
- Perfect Game
- All Spares
- All Open Frames
- Tenth Frame Strike
- Tenth Frame Spare
- Tenth Frame Open
- Gutter Game

Each game also stores its expected score, making assertions simple and readable.

---

### invalid_games.py

Contains reusable invalid bowling games.

Examples

- Spare First Roll
- Invalid Symbol
- Frame Exceeds Ten
- Too Many Rolls in Tenth Frame
- Less Than Ten Frames
- More Than Ten Frames
- Strike Second Roll
- Four Rolls in Tenth Frame
- Extra Frame After Game

Keeping these datasets separate improves test readability and reuse.

---

#  Pytest Fixtures

Instead of creating Game objects inside every test, the project uses **Pytest Fixtures**.

The fixture layer converts raw test data into Game objects before the tests execute.

```
Raw Game Data ->  GameParser -> Pytest Fixture -> Test Function
   
```

This reduces duplicate setup code across the test suite.

---

# Test Coverage

## Scoring Tests

Example Game

 Perfect Game

All Spares

 All Open Frames

Tenth Frame Strike

Tenth Frame Spare

Tenth Frame Open

---

## Validation Tests

Spare First Roll

 Invalid Symbol

Frame Pin Count Exceeds Ten

Strike as Second Roll

Too Many Rolls in Tenth Frame

Four Rolls in Tenth Frame

Less Than Ten Frames
 
 More Than Ten Frames

 Extra Frame After Game

---

## Additional Tests

 Parameterized Tests

 Allure Reporting

 Pytest Fixtures

Partial Scoring *(Not Implemented)*

---

# Parameterized Testing

To reduce duplicate test code, multiple bowling scenarios are executed using **pytest.mark.parametrize**.

The parameterized test covers both valid and invalid games through a single reusable test function.

This approach improves maintainability and makes it easy to extend the test suite by adding new datasets.

#  Installation in Local Computer

## Prerequisites

Before running the project, ensure the following software is installed.

- Python
- pip
- Git

---

## Clone the Repository

```bash
git clone <repository-url>
cd bowlinggame
```

---

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

The project uses the following libraries.

pytest==8.4.1           #to find and run the test cases
allure-pytest==2.15.0   # to generate the allure report
pytest-xdist==3.8.0     # for parallel execution of test cases
pytest-html==4.1.1       # to generate the html report (using allure instead of this)

---

#  Running the Application

A sample program has been provided in **main.py**.

Execute

```bash
python main.py
```

The application

- Parses the example bowling game
- Validates the game
- Calculates cumulative scores
- Prints the cumulative score after every frame


# To Running Tests

Run the complete test suite.

```bash
pytest
```


Run parameterized tests

```bash
pytest tests/test_parameterized.py
```

---

# Allure Reporting

The project uses **Allure Report** to generate detailed execution reports.

## Generate Test Results

```bash
pytest --alluredir=allure-results
```
---

## Generate HTML Report

```bash
allure generate allure-results --clean -o allure-report
```

---

## Open Report

```bash
allure open allure-report
```

The report contains

- Test execution summary
- Passed tests
- Failed tests
- Stack traces
- Execution timeline
- Test metadata
- Feature & Story grouping

---

#  Pytest Configuration

The project is configured using **pytest.ini**.

Configuration includes

- Test discovery
- Python path
- Allure report generation
- Marker definitions
- Short traceback formatting

This keeps test execution consistent across local development and CI environments.

---

# Repository Configuration

The repository includes a **.gitignore** file that excludes generated and environment specific files.

Ignored items include

- Python cache
- Virtual environments
- Pytest cache
- Allure reports
- Generated reports
- Log files

This keeps the repository clean and avoids committing generated artifacts.

---

# Technologies Used

- Python 3
- Pytest
- Allure Report

## Parallel Execution

- pytest-xdist

## Design

- Object Oriented Programming (OOP)

## Version Control

- GitHub

## Continuous Integration

- GitHub Actions *(Configured separately)*

---


# Key Design Decisions

The project was designed with the following principles in mind.

### Separation of Concerns

- Parsing
- Validation
- Scoring
- Models
- Utilities
- Exception Handling

Each module performs only one responsibility.

---

### Reusability

Reusable components include

- Test data
- Fixtures
- Helper methods
- Exception hierarchy

This minimizes duplicate code.

---

### Maintainability

The layered architecture allows new validation rules, scoring rules, or test cases to be added without impacting existing modules.

---

### Testability

The application is fully testable through

- Individual unit tests
- Parameterized tests
- Reusable fixtures
- Allure reports

---

# Continuous Integration / Continuous Deployment (CI/CD)

This project includes a **GitHub Actions CI/CD pipeline** that automatically builds, tests, generates an **Allure Report**, and publishes the report to **GitHub Pages**.

The workflow is triggered whenever:

- Code is pushed to the **main** branch
- A Pull Request is created against the **main** branch
- The workflow is executed manually from the **GitHub Actions** tab

---

## CI/CD Workflow

## Workflow Steps

The CI/CD pipeline performs the following tasks automatically.

### 1. Checkout Repository

Downloads the latest source code from the GitHub repository into the GitHub Actions runner.

---

### 2. Setup Python

Installs **Python 3.12** for executing the Bowling Game application and automated test suite.

---

### 3. Setup Java

Installs **Java 17** because the **Allure Command Line** requires Java to generate HTML reports.

---

### 4. Install Allure CLI

Downloads and installs the latest Allure Command Line tool.

This is used to convert raw Allure test results into a user-friendly HTML report.

---

### 5. Install Project Dependencies

Installs all required Python packages from **requirements.txt**.

Example:

- Pytest
- Allure Pytest
- Pytest-xdist
- Pytest-html

---

### 6. Execute Automated Tests

Runs the complete Pytest suite.

```bash
pytest tests -n auto --alluredir=allure-results
```

The workflow executes tests in **parallel** using **pytest-xdist**, reducing execution time.

---

### 7. Generate Allure Report

Generates the HTML report from the test results.

```bash
allure generate allure-results --clean -o allure-report
```

---

### 8. Configure GitHub Pages

Prepares GitHub Pages for deployment.

---

### 9. Upload Report

Uploads the generated Allure Report as a GitHub Pages artifact.

---

### 10. Deploy Report

Publishes the Allure Report to **GitHub Pages**.

After successful execution, the report can be accessed directly from the repository's GitHub Pages URL.

---



# Running the CI/CD Pipeline

If you fork this repository, follow the steps below to execute the workflow.

---

## Step 1

Fork the repository into your own GitHub account.

https://github.com/BrahmendraJayaraju/bowling-game-scorer/fork
---

## Step 2

Open the forked repository.

---

Before ## Step 3 Do this 

#  Enable GitHub Pages

If this is your first time running the workflow after forking the repository, GitHub Pages must be enabled.

Navigate to

```
Repository -> Settings -> Pages    (at left side below code spaces )

```

in pages Under **Build and Deployment**

Select

```
Source -> GitHub Actions
```

> **Do not choose "Deploy from a branch".**

---

Save the configuration.

Once the workflow completes successfully, GitHub Pages will automatically publish the generated Allure Report.

---

## Step 3

Navigate to

```
Actions
```

---

## Step 4

Select

```
Bowling Game CI (Run Tests and Publish Allure Report)
```

---

## Step 5

Click

```
Run workflow
```

and execute the workflow.

---


# Viewing the Allure Report after 2 min of execution 

After the workflow finishes successfully,

Navigate to

```
Repository -> Actions -> Latest Workflow Run

```

The deployment URL will be displayed below **test-and-publish** .Click on URL it will open Allure Report. Click on All the tabs and check the results if youre new to allure reporting.


---

