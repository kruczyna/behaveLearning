# Requirements- Linux (Chrome):
1. Python3
2. Chrome browser

# Fetch code
git clone git@github.com:kruczyna/behaveLearning.git

# Configuration- behave.ini
1. main_url- main page url (test assumes start in /console/mappings)

# Running tests
* execute always in `features` directory (same level as requirements.txt and chromedriver_update.sh are)
1. one feature:
  * behave -i [name].feature
2. all features, alphabetical order:
  * behave

#Configuration: .feature files
* all string enclosed in double quotes are step parameters and can be changed
* **WARNING**: some of them are selectors, change with caution
