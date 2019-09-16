# FantasyOptimizer
Lineup Optimizer for NBA FanDuel DFS. 


The inspiration for this project comes from two academic papers

[Learning to Turn Fantasy Basketball Into Real Money
Introduction to Machine Learning
](https://shreyasskandan.github.io/Old_Website/files/report-ChanHuShivakumar.pdf)

[Machine Learning Applications in Fantasy Basketball](http://cs229.stanford.edu/proj2015/104_report.pdf)

This project implements a liner regression model from the Sklearn library to predict player Field Goals, 3-Points, Free Throws, Offense Rebounds, Defense Rebounds, Assists, Blocks, Steals, and Turnovers for 10 select games in the 2018-2019 Lakers Season. The data used is player box score statistics and team (game by game) statistics rom basketball-reference.com

I have plans to try out other Machine learning models in the future including, Ridge Regression, Rendom Forest Regression,a dn Support Vecotr Regression.


| Game | Date       |     | Opponent | Win/Loss |
|:----:|:----------:|:---:|:--------:|:--------:|
| 29   | 12/15/2018 | @   | CHA      | W        |
| 30   | 12/16/2018 | @   | CHA      | L        |
| 31   | 12/18/2018 | @   | CHA      | L        |
| 32   | 12/21/2018 |     | CHA      | W        |
| 33   | 12/23/2018 |     | CHA      | L        |
| 34   | 12/25/2018 | @   | CHA      | W        |
| 35   | 12/27/2018 | @   | CHA      | L        |
| 36   | 12/28/2018 |     | CHA      | L        |
| 37   | 12/30/2018 |     | CHA      | W        |
| 38   | 1/2/2019   |     | CHA      | L        |

With better ways to retireve and clense data, this model can be applied to each player for each game in and NBA season.
In the future, I have plans to create web-scraping scripts to pull the data I use and store it in a database for every player and every game. I also want to setup a rest-api so that other developers can use this data

The features in this model are:
1. The players statistical performance in the previous game
2. The players average statistical performance across the past 5 games
3. The opposing team defenses average statistical performance across the past 5 games
4. The opposing team defenses average statistical performance across all of the games played in the season thus far.

Each predicted player stat can be used to project their fantasy score (FanDuel, DraftKings, etc.), and by using a Constant Satisfaction Problem, thier fantasy salaries can be assigend to each player to determine an optimal lineup.

An extension of predicting individual player performance in a particular game is predicting the outcome of that game. Given two teams, Team 1 and Team 2, we use the procedure described above to predict the number of points scored by each of the active players on Team 1 and by each of the active players on Team 2. Then if we combine these points, we have a predicted game outcome. 


