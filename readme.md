# Readme: TempMonitor to file --> Caner Aydin 2019

I have built this code for,
1) fetching latest temperature data from iStatistica for Mac API (in JSON)
2) converting JSON data to Python Dict
3) Adding a random value into it to make sure that in every iteration it provides a different result (rastgele)
4) Converting Python Dict to JSON again
5) Writing JSON data to macpro_temp.json

Later I am running this code in crontab to make sure that I am receiving this .json file into related folder.

The reason for step #3: I am planning to push this data into Splunk and later convert it into Metrics so we can visualise it. Splunk has a feature to monitor files for changes, and if a change is detected, it is ingesting file input as a log item. The problem here is, temperature data does not change every minute, this means Splunk will not detect a change and will not ingest it into logs. So we need to add a random string into file to make sure that JSON file changes every time we run the script, and Splunk will detect a change and add this item as a log.

!! Make sure that you change the IP on line 11 to your original iStatistica for Mac IP. !!
