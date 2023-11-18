#!/bin/bash

# Define variables
REPO_DIR=$HOME/RiderApp-Backend
GIT_REPO_URL=https://github.com/Wali-Muhammad123/RiderApp-Backend.git
BRANCH=features-1

# Logging
echo "Starting deployment script."

# Navigate to the repository directory
cd $REPO_DIR

# Fetch the latest code from the repository
echo "Pulling latest code from $BRANCH branch of $GIT_REPO_URL."
git pull origin $BRANCH

# (Optional) If you are using a virtual environment for a Python application, for example
# echo "Activating virtual environment."
# source /path/to/your/virtualenv/bin/activate

# (Optional) Install dependencies
# For a Node.js application
# echo "Installing Node.js dependencies."
# npm install

# For a Python application
# echo "Installing Python dependencies."
pip install -r requirements.txt

#(Optional) Run database migrations
echo "Running database migrations."
python3 manage.py migrate  # Django example

# (Optional) Compile assets or run build scripts
# echo "Building the application."
# npm run build  # Node.js example

# (Optional) Restart the web server to load new code
# For example, if using systemd to manage a service
# echo "Restarting the application service."
# systemctl restart your-application-service
python3 manage.py runserver

# Logging
echo "Deployment script executed successfully."

# Exit the script
exit 0
