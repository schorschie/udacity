# Dataset Ford BayWheels

## by Grzegorz Lippe

<!--
A readme document, in plain text, Markdown, or PDF format, including the
following information:

- Which dataset you chose. If not part of Udacity's dataset options, document
  the source of your data.
- Main findings from the exploratory data analysis, and how you chose the
  results to put in your explanatory analysis.
- If you obtained feedback from others for your explanatory designs, document
  them here.
- List of resources used during the creation of the project. This includes web
  sites, books, forums, blog posts, and GitHub repositories.
-->

## Dataset

I selected the BayWheels Dataset, procided by Udacity. BayWheels provides all
their data for download as a csv format. I chose to limit the Exploration to the
data of 2019.

## Summary of Findings

* The provided data is considerably extensive, so I chose to limit my import to
  some specific columns of the provided data.
* Since a bike ID is provided some bike related data can be gathered.
* Traveled distances are not provided, but an air line distance can be
  calculated from the start and end positions of the rides.
* With these it is also clear, that the company is operating in San Francisco's
  Bay Area only.
* Some data points were cleaned, because the calculated travel duration or
  travel distance was to high.
* Most of the booked trips were shorter than 1 hour, and the distribution of the
  trips is log normal.
* The distributions of the duration of the booked rides and their time s log
  normal distributed, so one can conclude, that they originate from a sequence
  of normal distributed issues.
* There is a change of bike ID distribution within the year, so maybe some of
  the IDs are missing, or there was some internal rearrangement within Ford.
* Looking at the multivariate Exploration there are no clear preferences on
  Weekday or Month. One can only conclude, that the bikes are mainly booked on
  work days, not week ends.

## Key Insights for Presentation

* The distribution of the rides is log normal.
* The travel distance and time switched significantly between the "lower" and
  "higher" IDs.
* The amount of rides is quite stable over the year, with a slightly higher
  demand in July and April
* The weakest days are Saturdays and Sundays, so most of the people use the ride
  service to get to work, or back.
