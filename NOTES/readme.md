## Historic production data

For this project, you are given a dataset containing historic production data, the data is found in `dataset.csv` and consists of:
 - customer: The customer which has placed the demand.
 - product: The product which is requested.
 - week: The week in which the forecasted demand was created.
 - forecasted week: The week for which the forecast is made.
 - demand: The amount of demand we expect in forecasted week.

For example a line with the values `["Fun", "Willy Wonka", 39, 49, 145]` indicates that in week 39, we expected the Fun to order 145 Willy Wonka's in week 49.

The actual demand can be found in the lines where the week is equal to the forecasted week, for example `["Fun", "Willy Wonka", 49, 49, 137]` indicates that in week 49 there was a realized demand of 137 Willy Wonka's at the customer Fun.

We now want to create some alternative views of this dataset. In particular we want to create the tables that can be found in the folder `output`:
 1. `overview_actuals.xlsx`: In this excel file, we create an overview of all the actual demand in the dataset (where week == forecasted week).
 2. `overview_forecasts.xlsx`: In this table, we have in the index the forecasted week and as column names the week in which the forecast was created, with a sheet for each `customer - product` combination.
 3. `overview_weeks_advance.xlsx`: Each column in this dataset corresponds to a specific number of weeks in advance the forecast was created (`forecasted week - week`) and in a single column, we have all data available for this specific number of weeks in advance.
 4. `stats_weeks_advance.xlsx`: Statistics about the data in the columns of `overview_weeks_advance.xlsx`.