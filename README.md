# AutoRewards - MS Rewards Grinder

This repository contains Python scripts for automating searches from Windows computers for the sake of earning Microsoft Rewards at different levels.

Note that these scripts can only help grind MS Rewards that are earnable from computers, not mobile devices. For mobile devices, you have to manually do the searches on the Bing app.

## Overview

This project includes two Python scripts:

- `level_1_grinder.py`: Script for grinding MS Rewards at level 1. (For grinding 30pts daily)
- `level_2_grinder.py`: Script for grinding MS Rewards at level 2. (For grinding 90pts daily)

## Features

- Automates search tasks on Windows to earn Microsoft Rewards points.
- Customizable search items list for each level.
- Simple and easy-to-understand codebase.

## Usage

### Setup Instructions:

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the necessary dependencies using the following command in Command Prompt:

   ```
   pip install pyautogui
   ```

### Running the Scripts:

**Important Notes:**

- Ensure your PC is idle before running these scripts because they could manipulate the running program. Avoid using your PC while the scripts are running.
- Adjust the time gap between searches according to your internet speed. The default is 8 seconds. You can adjust it in both scripts at line no. 13.
- In case you want to stop running script, just switch to Python shell and clink in there and press "ctrl + C".

**Procedure:**

Open blank new tab in edge browser and then run the desired script based on the level of MS Rewards you want to grind:

_Method 1:_ You can use the following commands in Command Prompt:

```
python level_1_grinder.py
```

or

```
python level_2_grinder.py
```

_Method 2:_ Alternatively, you can simply double-click the file you want to run from the file explorer.

## Disclaimer

Please note that while these scripts aim to enhance your Microsoft Rewards experience, they are intended for educational purposes only. Usage of these scripts is at your own risk, and you are responsible for complying with the terms of service of Microsoft Rewards and any other relevant platforms.

## Contributions

Contributions to this project are welcome! Whether you're fixing bugs, adding new features, or improving existing ones, your contributions are valued. Please submit any enhancements via pull requests.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it in accordance with the terms of the license.
