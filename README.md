# Metis-Project 3: What Government is best for economic development ? Classification Of Countries' Economic Growth
## DOTUN OPASINA


## SCOPE:

China's amazing economic growth without changing it's style of leadership to more western democracy has led to a great debate among scholars about the type of leadership that is soothed for development of developing countries. Many have argued that the lengthy process of decision making in democracy might not be needed for a country whose main objectives is to make quick and nimble decision for it best interests.

This debate led me to ask the question:"Are authoritarian government good for economic growth and what ways can we predict it?"
This question can be used to help current leaders gain insight on what model of leadership to pursue and for young leaders to give them clarity on questions discussed all over the world.


## METHODOLOGY:
1. Download Democracy index of countries and their Economic Data from [Gapminder](https://www.gapminder.org/data/documentation/democracy-index/) and [Yearly GDP data](https://data.worldbank.org/indicator/ny.gdp.mktp.cd)  <br>
2. Clean up data and put them in a postgres database<br>
3. Connect python code to database 
4. Build classification and linear regression models of countries democracy index and gdp data <br>


## DATA SOURCES:
- [Gapminder](https://www.gapminder.org/data/documentation/democracy-index/)  
- [Yearly GDP data](https://data.worldbank.org/indicator/ny.gdp.mktp.cd)

## TARGET
- MVP: Classification of Countries and their economic growth from 2006 - 20018
- Goal: Prediction of countries and their economic growth from 2006- 2018 using Linear regression.
   
## FEATURES TO INCLUDE INTO CLASSIFICATION MODEL
### X
- Country's name
- Year
- Democracy Index
- Electoral Pluralism Index
- Government index
- Political participation index 
- Political culture index
- Civil liberties index 
- Change in democracy index 
- Yearly GDP %

### Y
- Type of GOVERNMENT


## FEATURES TO INCLUDE INTO LINEAR REGRESSION MODEL
### X
- Country's name
- Year
- Democracy Index
- Electoral Pluralism Index
- Government index
- Political participation index 
- Political culture index
- Civil liberties index 
- Change in democracy index 


### Y
- Yearly GDP %

### DATA
- 2144 rows of data
