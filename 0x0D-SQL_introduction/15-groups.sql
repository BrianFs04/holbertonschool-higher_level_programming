-- Lists the number of records with the same score in the table second_table
SELECT score, count(*) as number from second_table group by score DESC;
