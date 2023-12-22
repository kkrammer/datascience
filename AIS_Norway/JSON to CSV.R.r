# Install packages and libraries to convert JSON and write to CSV

install.packages("jsonlite")
install.packages("tidyverse")

library(jsonlite)
library(tidyverse)
library(readr)

# Convert saved JSON file to a data.frame called 'df'
  # You only need "file name.json" if the SJON file is saved in your documents folder
  # If a different path you will need to include the path. Example is "C:\\user\\myfiles\\json_twitter.json"

df <- fromJSON("jsontwitter.json")


# Export to CSV with row names, numbers on the left of the data.frame removed - Not cleaned so shows extra lines

write.csv(df, "json_twitter.csv", row.names = FALSE)




# Open JSON file in notepad and search for '\r' and '\n' and make a note of column names you found those 2 in
  # '\r' and '\n' cause return lines in a CSV export so need to be found and replaced with blank first

# check for correct column names by using function names() to see column headers
  # JSON data sometimes will have sub headers and will be below the header names you find in 'df'
  # You can view sub headers by adding a $ and adding the sub column name

names(df) # Prints the column names at the level of the table 'df'
names(df$user) # Prints the column names at the sub level table df called 'users'
names(df$quoted_tweet) # Prints the column names at the sub level table df called 'quoted_tweet'
names(df$quoted_tweet$user) # Prints the column names at the sub level table df and sub level of 'quoted_tweet' called 'user'


# Replace \n and \r found in column data with blank to remove any return lines using gsub

df$quoted_tweet$user$description <- gsub("\n", "", df$quoted_tweet$user$description)
df$user$description <- gsub("\n", "", df$user$description)
df$user$description <- gsub("\r", "", df$user$description)
df$quoted_tweet$full_text <- gsub("\n", "", df$quoted_tweet$full_text)
df$full_text <- gsub("\n", "", df$full_text)


# Export to CSV with row names, numbers on the left of the data.frame, removed

write.csv(df, "json_twitter.csv", row.names = FALSE)
