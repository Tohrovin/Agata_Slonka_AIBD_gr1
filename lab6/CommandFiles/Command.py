import pandas as pd

# Set path to data
DIR = "../AnalysisData/"

# Read original data
data = pd.read_csv(f"{DIR}slaskie_changed_header.csv", sep=';')
print(data)

data_no_column1 = data[['dni_od_zakupu', 'marka', 'wiek_kupujacego', 'plec_kupujacego', 'ocena']].sort_values(['ocena', 'wiek_kupujacego'])
print(data_no_column1)

brand_ratings = data_no_column1.groupby(["marka"]).ocena.mean().reset_index()


average_rating_f = data_no_column1.loc[(data_no_column1['plec_kupujacego'] == 'K')].groupby(["marka"]).ocena.mean(numeric_only=True).reset_index()
average_rating_m = data_no_column1.loc[(data_no_column1['plec_kupujacego'] == 'M')].groupby(["marka"]).ocena.mean(numeric_only=True).reset_index()

brand_ratings.insert(2, "ocena_K", average_rating_f['ocena'], True)
brand_ratings.insert(3, "ocena_M", average_rating_m['ocena'], True)

average_age = data_no_column1.groupby(["marka"]).wiek_kupujacego.mean(numeric_only=True).reset_index()
brand_ratings.insert(4, "sredni_wiek", average_age['wiek_kupujacego'], True)

average_age_f = data_no_column1.loc[(data_no_column1['plec_kupujacego'] == 'K')].groupby(["marka"]).wiek_kupujacego.mean(numeric_only=True).reset_index()
average_age_m = data_no_column1.loc[(data_no_column1['plec_kupujacego'] == 'M')].groupby(["marka"]).wiek_kupujacego.mean(numeric_only=True).reset_index()

brand_ratings.insert(5, "sredni_wiek_K", average_age_f['wiek_kupujacego'], True)
brand_ratings.insert(6, "sredni_wiek_M", average_age_m['wiek_kupujacego'], True)



average_days = data_no_column1.groupby(["marka"]).dni_od_zakupu.mean(numeric_only=True).reset_index()
brand_ratings.insert(7, "dni_po_zakupie", average_days['dni_od_zakupu'], True)

average_days_f = data_no_column1.loc[(data_no_column1['plec_kupujacego'] == 'K')].groupby(["marka"]).dni_od_zakupu.mean(numeric_only=True).reset_index()
average_days_m = data_no_column1.loc[(data_no_column1['plec_kupujacego'] == 'M')].groupby(["marka"]).dni_od_zakupu.mean(numeric_only=True).reset_index()

brand_ratings.insert(8, "dni_po_zakupie_K", average_days_f['dni_od_zakupu'], True)
brand_ratings.insert(9, "dni_po_zakupie_M", average_days_m['dni_od_zakupu'], True)

print(brand_ratings)

days_after = data[['dni_od_zakupu', 'ocena']].sort_values(['dni_od_zakupu'])
days_rating = days_after.groupby(["dni_od_zakupu"]).ocena.mean().reset_index()
print(days_rating)

days_rating.to_csv(path_or_buf=f"{DIR}days_rating.csv", sep=";")
brand_ratings.to_csv(path_or_buf=f"{DIR}brand_ratings.csv", sep=";")


