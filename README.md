# Election_Analysis

## Overview of Election Audit

### Background

A set of election results is saved in an excel file with over 300,000 rows. The data contains the ballot id, county name, and candidate name.

### Purpose

The purpose of this project is to create a python script that can generate and deliver the following information:
- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote
- Each county and its total vote count
- Each county and its percentage of the total votes
- The county with the largest number of voters

## Election-Audit Results

### How many votes were cast in this congressional election?

The total number of votes that were cast in this congressional election was 369,711.

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

In this precinct, there are three counties: Jefferson, Denver, and Arapahoe. For Jefferson, 38,855 votes were recorded, which is 10.5% of the total valid votes. For Denver, 306,055 votes were recorded, which is 82.8% of the total valid votes. For Arapahoe, 24,801 votes were recorded, which is 6.7% of the total valid votes.

### Which county had the largest number of votes?

Denver has the largest number of votes with a count of 306,055 and 82.8% of the total votes.

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

In this precinct, there are three candidates: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. For Charles Casper Stockham, 85,213 votes were recorded, which is 23.0% of the total valid votes. For Diana DeGette, 272,892 votes were recorded, which is 73.8% of the total valid votes. For Raymon Anthony Doane, 11,606 votes were recorded, which is 3.1% of the total valid votes.

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The winner of this election is Diana DeGette with 272,892 votes which is 73.8% of the total votes.

## Election-Audit Summary

This python script is able to read any election data in CSV format that consists of columns of ballot id, county name, and candidate name. The script can automatically generate summary information regarding votes categorized by county and candidate. With this script, the election commission automatically generates all election results for other precincts, saving both time and resources compared to a traditional method such as count by men. 
