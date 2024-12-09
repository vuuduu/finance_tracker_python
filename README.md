# finance_tracker_python

## Description
- A simple python application that allow users to **CREATE, READ, UPDATE, and DELETE** their financial expenses and income
- The application UI is from the terminal that let users view all their **Monthly Expenses & Income**


## Functionality
- crud on monthly tracker(s) data
- crud on expense(s) data
- crud on income(s) data


## Data Info
- `/data/expenses.json` = hold all the expenses info
- `/data/incomes.json`  = hold all the incomes info
- `/data/payoff.json`   = hold all the payoff info
- `/data/trackers.json` = hold all the _date_ and _year_ info

## Data Relationship
- Everytime a new expenses is created, checks it's data and add a new month & year to trackers if not already