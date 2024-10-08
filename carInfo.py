import pandas as pd;

uniqueLists = {}
headers = ["Price", "Maintenance_Cost",
           "Number_of_doors", "Number_of_passengers",
           "Luggage_capacity", "Safety_rating",
           "Classification_of_vehicle"]
data = pd.read_csv("cars-sample.txt", names=headers)

headerIdx = 0
for header in headers:
    key = f"list_{headers[headerIdx]}"
    uniqueLists[key] = data[header]
    headerIdx += 1

# find the price of med
def advancedSearch(header, searchHeader, searchVal):
    idx = 0
    resultsIdx = 0
    results = {}
    name = f"list_{header}"
    for val in uniqueLists[f"list_{searchHeader}"]:
        if val == searchVal:
            results[resultsIdx] = uniqueLists[name][idx]
            resultsIdx += 1
        idx += 1
    return results

# Find the list index values of each automobile having a “price” rating of "med"
listPriceMed = {}
listIdx = 0
priceIdx = 0
for price in uniqueLists["list_Price"]:
    if price == "med":
        listPriceMed[priceIdx] = listIdx
        priceIdx += 1
    listIdx += 1

# Find the "number of passengers" value for each auto having a "price" value of "med"
passangersPerMedPrice = {}
priceIdx = 0
priceMedIdx = 0
for price in uniqueLists["list_Price"]:
    if price == "med":
        passangersPerMedPrice[priceMedIdx] = uniqueLists["list_Number_of_passengers"][priceIdx]
        priceMedIdx += 1
    priceIdx += 1
# finding every car with a high price that is not low maintenance
pricyNotLowMaint = {}
idx = 0
resultsIdx = 0
for priceVal in uniqueLists["list_Price"]:
    if priceVal == "high":
        if uniqueLists["list_Maintenance_Cost"][idx] != "low":
            pricyNotLowMaint[resultsIdx] = idx
            resultsIdx += 1
    idx += 1

listPriceMedComp = [idx for idx, price in enumerate(uniqueLists["list_Price"]) if price == "med"]
passangersPerMedPriceComp = [uniqueLists["list_Number_of_passengers"][idx] for idx in range(len(uniqueLists["list_Price"])) if uniqueLists["list_Price"][idx] == "med"]

pricyNotLowMaintComp = [idx for idx, (price, maint) in enumerate(zip(uniqueLists["list_Price"], uniqueLists["list_Maintenance_Cost"])) if price == "high" and maint != "low"]

advancedSearchExample = advancedSearch("Number_of_passengers", "Price", "med")

print(listPriceMed)
print(passangersPerMedPrice)
print(pricyNotLowMaint)
print()
print(listPriceMedComp)
print(passangersPerMedPriceComp)
print(pricyNotLowMaintComp)