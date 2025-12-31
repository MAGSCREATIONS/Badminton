# Badminton Player Group Randomizer

A web application and Python script that randomizes badminton players into groups of 4, following specific skill level rules.

## Rules

- Each group consists of exactly 4 players
- Valid combinations:
  - Beginner + Intermediate players
  - Intermediate + Advanced players
- Invalid combinations:
  - Beginner + Advanced (without Intermediate)

## How to Run

### Web Version (Recommended - Mobile Friendly)

1. Run the `run_web.bat` file (Windows) or simply open the `index.html` file in your web browser

2. **Check the boxes** next to players who are present (all players start unchecked by default)

3. Use "Select All" or "Select None" buttons to quickly change selections

4. Click "Randomize Groups" to generate groups from selected players

5. View the generated groups with teams

**Note:** This is a client-side web application that runs entirely in your browser using JavaScript. No server or installation required.

### Python Flask Web App (Mobile Friendly)

1. Ensure Python 3 is installed on your system

2. Install Flask (if not already installed):
   ```bash
   pip install flask
   ```

3. Run the Flask web application:
   ```bash
   python app.py
   ```

4. Open your web browser and go to `http://localhost:5000`

5. Use the mobile-friendly web interface to select players and randomize groups

**Note:** This version runs a local web server and provides the same functionality as the JavaScript version but uses Python for the backend logic.

### Python Command Line Version

1. Ensure Python 3 is installed on your system

2. Run the Python script:
   ```bash
   python main.py
   ```

3. Enter absent players when prompted (comma-separated, or press Enter for none)

4. View the randomized groups in the console

## Features

- **Mobile-Friendly**: Fully responsive design that works great on phones and tablets
- **Touch-Optimized**: Large touch targets for easy interaction on mobile devices
- **Smart Grouping**: Advanced algorithm ensuring fair skill-level distribution
- **Real-time Updates**: Live status updates as you select players
- **Team Formation**: Automatic team splitting within groups
- **Visual Feedback**: Color-coded skill levels and status indicators

## Mobile Features

- **Responsive Layout**: Adapts perfectly to any screen size
- **Large Touch Targets**: Easy-to-tap buttons and checkboxes
- **Optimized Tables**: Compact display on mobile with hidden columns
- **Smooth Scrolling**: Auto-scroll to results on mobile devices
- **PWA Ready**: Includes mobile app meta tags for better mobile experience

- **Fixed Player List**: Uses a predefined list of 19 players
- **Smart Grouping**: Automatically creates valid groups following skill level rules
- **Randomization**: Each run produces different group combinations

## Files

### Python Files
- `player.py` - Represents a player with name and skill level
- `team.py` - Represents a team of 2 players
- `group.py` - Represents a group of 4 players with validation and team splitting
- `badminton_group_randomizer.py` - Contains the randomization logic
- `main.py` - Command-line Python application entry point
- `app.py` - Flask web application for mobile-friendly access

### Web Files
- `index.html` - Client-side web application with responsive design
- `templates/index.html` - Flask web application template
- `README.md` - This documentation file

