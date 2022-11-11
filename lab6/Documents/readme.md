# Laboratorium 6 - TIER protocol i tidy data

Original data slaskie.csv is available in /OriginalData folder. It contains information about vacuum cleaners' ratings from Śląsk and buyers' data.

The whole script for modyfing the data is in /CommandFiles/Command.py
as is the data for generating graphs for dataAppendix - /CommandFiles/dataAppendix.ipnb

Data after analysis is available in:

- /AnalysisData/slaskie_changed_header.csv - file contains extracted info from slaskie.csv. Only the heders were changed to:
	-column1 - contains enumaration of differen rows
	-dni_od_zakupu - days from the purchase
	-marka - the brand of the vacuum cleaner
	-wiek_kupujacego - buyer's age
	-plec_kupujacego - buyer's gender
	-ocena - buyer's rating

- /AnalysisData/brand_ratings.csv - file contains cumulated information from slaskie_changed_header.csv. Headers of file are:
	-marka - the brand of the vacuum cleaner
	-ocena - average rating
	-ocena_K - average rating by women
	-ocena_M - average rating by men
	-sredni_wiek - average age of the buyers
	-sredni_wiek_K - average age of the female buyers
	-sredni_wiek_M - average age of the male buyers
	-dni_po_zakupie - average time after purchase before rating
	-dni_po_zakupie_K - average time after purchase before rating by woman
	-dni_po_zakupie_M - average time after purchase before rating by man

- /AnalysisData/days_rating.csv - file contains chosen and cumulated information from slaskie_changed_header.csv. Headers of file are:
	-dni_od_zakupu - average time after purchase before rating
	-ocena - average rating writen on x's day after purchase

In /Documents we can find graphs showing informatio extracted from slaskie.csv as well as dataAppendix.ipnb which serves as our final, electronic paper.

Firstly the headers from slaskie.csv were changed into something more in programming standard and converting errors were fixed. The file with changed headers is available in /AnalysisData/slaskie_changed_header.csv. Later we worked on that file, we sorted, cumulated and got the average values of various columns.

The mean values sorted by gender and brand of a vacuum cleaner are saved in 
-  /AnalysisData/brand_ratings.csv while the avereage rating depending on the day after the purchase can be found in -  /AnalysisData/days_rating.csv

All the modifications were made using library pandas, and the graphs used matplotlib. The software, whcich was used for such manipulations was Pycharm.

