# Indicator List

## General Overview

#### Country Codes
- https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

#### International Organizations
- UN
	- https://www.un.org/en/about-us/member-states
- EU
	- https://neighbourhood-enlargement.ec.europa.eu/enlargement-policy/6-27-members_en
- EEA
	- https://www.netherlandsworldwide.nl/eu-eea-efta-schengen-countries
- Schegen
	- https://www.netherlandsworldwide.nl/eu-eea-efta-schengen-countries
- EFTA
	- https://www.netherlandsworldwide.nl/eu-eea-efta-schengen-countries
- OECD
	- https://www.oecd.org/about/document/ratification-oecd-convention.htm
- The World Bank
	- https://www.worldbank.org/en/about/leadership/members
- IMF
	- https://www.imf.org/external/np/sec/memdir/memdate.htm
- NATO
	- https://www.nato.int/cps/en/natohq/topics_52044.htm
- BRICS
	- https://en.wikipedia.org/wiki/BRICS
- WTO
	- https://www.wto.org/english/thewto_e/whatis_e/tif_e/org6_e.htm
- The Commonwealth
	- https://thecommonwealth.org/our-member-countries
- African Union
	- https://au.int/en/member_states/countryprofiles2
- Arab League
	- https://www.cfr.org/backgrounder/arab-league
- OPEC
	- https://www.opec.org/opec_web/en/about_us/25.htm
- G7
	- https://en.wikipedia.org/wiki/G7
- G20
	- https://en.wikipedia.org/wiki/G20
- Schengen Area
	- https://en.wikipedia.org/wiki/Schengen_Area
- Pacific Islands Forum
	- https://www.forumsec.org/#

#### Population
- https://population.un.org/wpp/Download/Standard/CSV/
- https://stats.oecd.org/Index.aspx?DataSetCode=EDU_DEM

#### World Bank Country and Lending Groups
- For the current 2024 fiscal year, low-income economies are defined as those with a GNI per capita, calculated using the World Bank Atlas method, of $1,135 or less in 2022; lower middle-income economies are those with a GNI per capita between $1,136 and $4,465; upper middle-income economies are those with a GNI per capita between $4,466 and $13,845; high-income economies are those with a GNI per capita of $13,846 or more.
- https://datahelpdesk.worldbank.org/knowledgebase/articles/906519
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Utilities/Country_Development_Classifications.xlsx

## Macroeconomics

### GDP
- Gross Domestic Product.
- Recession is defined by GDP.
Problems:
- Informal economy & developing nations bias
- Global operations from big firms (S&P 500) do not count for the source country.
	- Relevant for countries that have plenty of natural resources that get exported by foreign companies.
- Does not account for waste.
- Is not a metric that defines the average net worth.
- Does not account for richness distribution.
- When comparing two economies and using exchange rates transform to one currency, the Balassa–Samuelson effect occurs:
	- Balassa–Samuelson effect of Productivity biased purchasing power parity is the tendency for consumer prices of non-tradeables (services) to be systematically higher in more developed countries than in less developed countries, while the tradeable goods stay the same.
- Thus, we need to use Purchase Power Parity
	- We always use PPP-Adjusted Real GDP when comparing economies over time.
	- For example:
		- GDP Mexico (USD): $1,414,187.19
		- GDP PPP Mexico (USD): $2,742,903.11
- The Rice Problem:
	- Many types of rice
- The Croissant Problem:
	- Croissant in Paris is much better vs Washington
- The Cheese Problem:
	- USA consumes tons of cheese vs China. If Cheese is more expensive in China, that does noy mean that they have a lower standard of living. Simply, they do not like Cheese.
- The Health Care Problem:
	- How do we measure prices of goods that are not sold in markets such as a chest X-Ray, heart surgery, Chemo, etc.
- The Welding Equipment Problem:
	- Producer goods
- Some third-world countries have poor data:
	- We can measure Economic Growth from electricity usage (from satellite images)

Gross: Total
Domestic: Within borders
Product: Value of all goods & services produced

Gross Domestic Product: Value of all final goods & services produced within a country's borders in a given year.
- Goods included:
	- Final good: Finished good, goes straight to consumer.
	- Capital goods: Goods that will not be sold again as part of a new good (e.g., machinery used to produce other goods)
- Period included:
	- Only goods produced under the year of study (i.e., no old goods).
- Scope included:
	- Goods produced within a country's borders (i.e., imports add up to the GPD of the source country, and not the country where it was purchased)
- Types of products:
	- Consumer goods
	- Business goods
	- Government goods
	- Net exports (export - import)
Unmeasured channels:
- Informal economy
	- Black market
	- Illegal goods
	- Unreported transactions

Types of GPD:
- Nominal GDP: Measured in current prices
- Real GDP: Measured in constant (unchanging prices). This is Nominal GDP adjusted for inflation. More accurate since inflation can distort value of goods & services.

#### Nominal GDP
- GDP at purchaser's prices is the sum of gross value added by all resident producers in the economy plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources. Data are in current U.S. dollars. Dollar figures for GDP are converted from domestic currencies using single year official exchange rates. For a few countries where the official exchange rate does not reflect the rate effectively applied to actual foreign exchange transactions, an alternative conversion factor is used.
- Includes inflation:
	- 2005 Prices x 2005 Quantities = 2005 GDP in 2005 USD = $12.4
	- 2008 Prices x 2008 Quantities = 2008 GDP in 2008 USD = $7.4
	- Growth of nominal GDP (2005 - 2008) = ((12.4 - 7.4) / 7.4) * 100

#### Real GDP
- Does not include inflation:
	- 2005 Prices x 2008 Quantities = 2005 GDP in 2008 USD = $14.4
	- 2008 Prices x 2008 Quantities = 2005 GDP in 2005 USD = $7.4
	- If inflation is higher in 2008, we get a smaller gap when we calculate Growth Rate

#### GNP
- GNP: Gross National Product
- Accounts for Net Foreign Income
	- If IKEA produces 10 million & returns 5 million to Sweden, only 5 million get considered in GNP.

---
---

## Macroeconomics

### GDP

#### Nominal GDP
- GDP at purchaser's prices is the sum of gross value added by all resident producers in the economy plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources. Data are in current U.S. dollars. Dollar figures for GDP are converted from domestic currencies using single year official exchange rates. For a few countries where the official exchange rate does not reflect the rate effectively applied to actual foreign exchange transactions, an alternative conversion factor is used.
- Includes inflation:
	- 2005 Prices x 2005 Quantities = 2005 GDP in 2005 USD = $12.4
	- 2008 Prices x 2008 Quantities = 2008 GDP in 2008 USD = $7.4
	- Growth of nominal GDP (2005 - 2008) = ((12.4 - 7.4) / 7.4) * 100
- https://data.worldbank.org/indicator/NY.GDP.MKTP.CD
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/GDP_Nominal

#### GDP (PPP)
- This indicator provides values for gross domestic product (GDP) expressed in current international dollars, converted by purchasing power parity (PPP) conversion factor. GDP is the sum of gross value added by all resident producers in the country plus any product taxes and minus any subsidies not included in the value of the products. PPP conversion factor is a spatial price deflator and currency converter that eliminates the effects of the differences in price levels between countries. From April 2020, “GDP: linked series (current LCU)” [NY.GDP.MKTP.CN.AD] is used as underlying GDP in local currency unit so that it’s in line with time series of PPP conversion factors for GDP, which are extrapolated with linked GDP deflators.
- https://data.worldbank.org/indicator/NY.GDP.MKTP.PP.CD
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/GDP_PPP

#### GDP per Capita (PPP) (Current International)
- Country's GDP / Population
- GDP per capita based on purchasing power parity (PPP). PPP GDP is gross domestic product converted to international dollars using purchasing power parity rates. An international dollar has the same purchasing power over GDP as the U.S. dollar has in the United States. GDP at purchaser's prices is the sum of gross value added by all resident producers in the country plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources. Data are in constant 2017 international dollars.
- https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/GDP_Per_Capita

#### GDP Growth Rate
- Annual percentage growth rate of GDP at market prices based on constant local currency. Aggregates are based on constant 2015 prices, expressed in U.S. dollars. GDP is the sum of gross value added by all resident producers in the economy plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources.
- https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/GDP_Growth

#### GDP Per Capita Growth Rate
- Annual percentage growth rate of GDP per capita based on constant local currency. GDP per capita is gross domestic product divided by midyear population. GDP at purchaser's prices is the sum of gross value added by all resident producers in the economy plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources.
- https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/GDP_Per_Capita_Growth

---

### Economic Metrics

#### Informal Employment % of Total Employment
- Used to complement GDP
- Gives developing nations unfavorable metrics
	- Their economy is less formal
- https://www.worldbank.org/en/research/brief/informal-economy-database
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Informal_Employment

#### Consumer Price Index (CPI)
- A statistical estimate of the change in prices for a basket of goods and services purchased by households.
- The main indicator of inflation worldwide.
- Strongly affects policy-making.
- Responsible in the US: Bureau of Labor Statistics (BLS)
- Categories included in Basket:
	- Housing (Important) (Biggest in the US)
		- Rent
		- Mortgage
	- Apparel
	- Transportation (Important)
	- Recreation
	- Medical Care
	- Food / Beverages (Important)
	- Education & Communication
	- Other Goods & Services
- Categories are weighted from importance to people.
	- Based on surveys
- How people feel inflation depends on what's on each person's basket (what matters the most to me)
- Only transitions items in and out of basket each 2 years.
- Inflation can become embedded in the economy to the point of recession (people ask for raises, companies keep increasing prices, and it becomes a circle)
- Some inflation is healthy (signifies economic growth). Too much inflation stagnates economic growth.
- Difficult to make comparison of GDP over long periods of time.
	- Consumption habits change
	- Tech products did not exist 30 years ago
- https://data.imf.org/?sk=4ffb52b2-3653-409a-b471-d47b46d904b5
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Consumer_Price_Index

#### Inflation, Consumer Prices
- Inflation as measured by the consumer price index reflects the annual percentage change in the cost to the average consumer of acquiring a basket of goods and services that may be fixed or changed at specified intervals, such as yearly. The Laspeyres formula is generally used.
- https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Inflation_Consumer_Prices

#### Big Mac Index (Economist)
- Big Mac Index is a Purchase Power Parity metric.
- It is in itself a basket of goods:
	- Bread
	- Beef
	- Cheese
	- Onions
	- Labor required to cook
	- Labor required to deliver
- If we simply use the exchange rate to convert, we see the Balassa–Samuelson, since a Big Mac also includes a labor component which is cheaper in Thailand.
- https://www.economist.com/big-mac-index
- https://github.com/TheEconomist/big-mac-data
- https://github.com/TheEconomist/big-mac-data/blob/master/output-data/big-mac-full-index.csv
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Big_Mac_Index

#### Inclusive Wealth Index (IWI)
- The aggregate value of all capital assets in a given region, including human capital, social capital, public capital, and natural capital.
- The Index calculation is based on estimating stocks of human, natural and produced (manufactured) capital which make up the productive base of an economy
- https://www.unep.org/resources/inclusive-wealth-report-2018

#### Genuine Progress Indicator (GPI)
- Metric used to measure the economic growth of a country. It is often considered an alternative metric to the more well-known gross domestic product (GDP) economic indicator. The GPI indicator takes everything the GDP uses into account but adds other figures that represent the cost of the negative effects related to economic activity, such as the cost of crime, ozone depletion, and the cost of resource depletion, among others.
- https://dnr.maryland.gov/mdgpi/Pages/what-is-the-GPI.aspx

#### Gross National Income (GNI) PPP Per Capita
- This indicator provides per capita values for gross national income (GNI. Formerly GNP) expressed in current international dollars converted by purchasing power parity (PPP) conversion factor. GNI is the sum of value added by all resident producers plus any product taxes (less subsidies) not included in the valuation of output plus net receipts of primary income (compensation of employees and property income) from abroad. PPP conversion factor is a spatial price deflator and currency converter that eliminates the effects of the differences in price levels between countries.
- https://data.worldbank.org/indicator/NY.GNP.PCAP.PP.CD
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/GNI_Per_Capita_PPP

#### Adjusted Net National Income Per Capita (current US$)
- Adjusted net national income is GNI minus consumption of fixed capital and natural resources depletion.
- https://data.worldbank.org/indicator/NY.ADJ.NNTY.PC.CD
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Adjusted_Net_National_Income_Per_Capita



---

### Unemployment & Underemployment

#### Unemployment (% of Total Labor Force) (Modeled ILO Estimate)
- Share of the labor force that is without work but available for and seeking employment.
- Paradoxically, low unemployment rates can disguise substantial poverty in a country, while high unemployment rates can occur in countries with a high level of economic development and low rates of poverty. In countries without unemployment or welfare benefits people eke out a living in vulnerable employment. In countries with well-developed safety nets workers can afford to wait for suitable or desirable jobs.
- https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SL.UEM.TOTL.ZS
- https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Unemployment_ILO_Estimate

#### Youth Unemployment Rate
- The youth unemployment rate is the number of unemployed 15-24 year-olds expressed as a percentage of the youth labour force. Unemployed people are those who report that they are without work, that they are available for work and that they have taken active steps to find work in the last four weeks.
- https://data.oecd.org/unemp/youth-unemployment-rate.htm
- https://data.worldbank.org/indicator/SL.UEM.1524.ZS
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Youth_Unemployment_Rate

#### Underemployment Rate
- Underemployment is a measure of the total number of people in an economy who are unwillingly working in low-skill and low-paying jobs or only part-time because they cannot get full-time jobs that use their skills.
- https://www.investopedia.com/terms/u/underemployment.asp
- https://ilostat.ilo.org/topics/unemployment-and-labour-underutilization/

---

### Debt & Deficit

#### Debt-to-GDP Ratio
- The debt-to-GDP ratio is the metric comparing a country's public debt to its gross domestic product (GDP). By comparing what a country owes with what it produces, the debt-to-GDP ratio reliably indicates that particular country’s ability to pay back its debts. Often expressed as a percentage, this ratio can also be interpreted as the number of years needed to pay back debt if GDP is dedicated entirely to debt repayment.
- https://www.imf.org/external/datamapper/CG_DEBT_GDP@GDD/CHN/FRA/DEU/ITA/JPN/GBR/USA
- https://www.investopedia.com/terms/d/debtgdpratio.asp
- https://worldpopulationreview.com/country-rankings/debt-to-gdp-ratio-by-country
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Debt-to-GDP_Ratio

#### Current Account Balance
- Current account balance compares a country's net trade in goods and services, plus net earnings, and net transfer payments to and from the rest of the world during the period specified. These figures are calculated on an exchange rate basis.
- https://www.cia.gov/the-world-factbook/field/current-account-balance/country-comparison/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Current_Account_Balance

### Income Inequality

#### Gini Coefficient
- The Gini coefficient is based on the comparison of cumulative proportions of the population against cumulative proportions of income they receive, and it ranges between 0 in the case of perfect equality and 1 in the case of perfect inequality.
- https://worldpopulationreview.com/country-rankings/gini-coefficient-by-country
- https://data.oecd.org/inequality/income-inequality.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Gini_Index

#### Shared Prosperity Ratio
- Shared prosperity is the average annual growth rate in income or consumption of the bottom 40 percent of the population in a country.
- https://www.worldbank.org/en/topic/poverty/brief/global-database-of-shared-prosperity
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Shared_Prosperity_Ratio

#### Prosperity Gap
- The Prosperity Gap is a distribution sensitive welfare measure: the gap improves (narrows) when all incomes increase, and it improves faster when incomes of poorer people increase. In 1990, individuals’ incomes globally needed to increase on average almost 11-fold to get everyone to the $25 threshold. Put differently, in 1990 the typical person in the world needed 11 days to earn what a person at the poverty line in rich countries earned in a day.   The last three decades have seen tremendous progress around the world, such that the average factor necessary for everyone to reach the same threshold in 2019 has more than halved to 5-fold. However, the gap remains large – today the typical person in the world would still need 5 days to earn what a person at the poverty line in rich countries earns in a day.
- https://blogs.worldbank.org/opendata/updated-estimates-prosperity-gap
- https://datanalytics.worldbank.org/pg_dashboard/#section-table-of-indicators
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Prosperity_Gap

#### Human Development Index (HDI)
- A statistical composite index of life expectancy, education (mean years of schooling completed and expected years of schooling upon entering the education system), and per capita income indicators, which is used to rank countries into four tiers of human development. A country scores a higher level of HDI when the lifespan is higher, the education level is higher, and the gross national income GNI (PPP) per capita is higher.
- https://hdr.undp.org/data-center/human-development-index#/indicies/HDI
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Human_Development_Index

### Poverty

#### Multidimensional Poverty Index
- Multidimensional Poverty Indices use a range of indicators to calculate a summary poverty figure for a given population, in which a larger figure indicates a higher level of poverty. This figure considers both the proportion of the population that is deemed poor, and the 'breadth' of poverty experienced by these 'poor' households, following the Alkire & Foster 'counting method'. The method was developed following increased criticism of monetary and consumption based poverty measures, seeking to capture the deprivations in non-monetary factors that contribute towards well-being. 
- https://hdr.undp.org/content/2023-global-multidimensional-poverty-index-mpi#/indicies/MPI
- https://ophi.org.uk/multidimensional-poverty-index/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Multidimensional_Poverty_Index

#### Working Poverty Rate
- The employed comprise all persons of working age who, during a specified brief period, were in one of the following categories: a) paid employment (whether at work or with a job but not at work); or b) self-employment (whether at work or with an enterprise but not at work).
- https://ilostat.ilo.org/data/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Working_Poverty_Rate

#### Proportion of Informal Employment
- This indicator conveys the share of informal employment in total employment. Employment comprises all persons of working age who, during a specified brief period, were either in paid employment (whether at work or with a job but not at work) or in self-employment (whether at work or with an enterprise but not at work). Informal employment comprises persons who in their main or secondary jobs were (a) own-account workers, employers and members of producers' cooperatives employed in their own informal sector enterprises; (b) own-account workers engaged in the production of goods exclusively for own final use by their household (e.g. subsistence farming); (c) contributing family workers, regardless of whether they work in formal or informal sector enterprises; or (d) employees holding informal jobs, whether employed by formal sector enterprises, informal sector enterprises, or as paid domestic workers by households. Data disaggregated by economic activity are provided according to the latest version of the International Standard Industrial Classification of All Economic Activities (ISIC) available for that year.
- https://ilostat.ilo.org/data/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Proportion_Of_Informal_Employment

---

### Income Disparities & Wage Gap

#### Median & Mean Net Worth
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Median_and_Mean_Net_Worth

#### Global Gender Gap Index
- The global gender gap index benchmarks national gender gaps on economic, political, education, and health-based criteria.
- https://www.statista.com/statistics/244387/the-global-gender-gap-index/
- https://www.weforum.org/publications/global-gender-gap-report-2023/in-full/benchmarking-gender-gaps-2023/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Gender_Gap_Index

#### Income Distribution
- https://www.oecd.org/social/income-distribution-database.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Income_Distribution

### Currency Value Against USD

#### Exchange Rates Against USD
- Exchange rates are defined as the price of one country's' currency in relation to another country's currency. This indicator is measured in terms of national currency per US dollar.
- https://data.oecd.org/conversion/exchange-rates.htm
- https://www.bis.org/statistics/xrusd.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Exchange_Rates_Against_USD

---

### Minimum Wage

#### Statutory Nominal Gross Monthly Minimum Wage | Annual
-  Data refer to the minimum monthly earnings of all employees as of December 31st of each year. Minimum wages are not reported for countries for which collective bargaining is in place for minimum wages. In cases where a national minimum wage is not mandated, the minimum wage in place in the capital or major city is used. In some cases, an average of multiple regional minimum wages is used. In countries where the minimum wage is set at the sectoral level or occupational level, the minimum wage for manufacturing or unskilled workers is generally applied. This is a harmonized series: (1) data reported as hourly, weekly, and yearly are converted to monthly, using data on average weekly hours if available; and (2) data are converted to U.S. dollars as the common currency, using exchange rates or purchasing power parity (PPP) rates rates for private consumption expenditures. The latter series allows for international comparisons by taking account of the differences in relative prices between countries.
- https://ilostat.ilo.org/topics/wages/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Minimum_Wages

---

### Labor Force Participation

#### Labor Force Participation Rate
- Labour force participation rate by sex and age -- ILO modelled estimates, Nov. 2022 (%) -- Annual
- The labour force participation rate is the labour force as a percent of the working-age population. The labour force is the sum of all persons of working age who are employed and those who are unemployed.
- https://www.ilo.org/shinyapps/bulkexplorer53/?lang=en&segment=indicator&id=EAP_2WAP_SEX_AGE_RT_A
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Labor_Force_Participation_Rate

---

### Household Dynamics

#### Household Disposable Income
- Disposable income is closest to the concept of income as generally understood in economics. Household disposable income is income available to households such as wages and salaries, income from self-employment and unincorporated enterprises, income from pensions and other social benefits, and income from financial investments (less any payments of tax, social insurance contributions and interest on financial liabilities). ‘Gross’ means that depreciation costs are not subtracted. For gross household disposable income per capita, growth rates (percentage change from previous period) are presented; these are ‘real’ growth rates adjusted to remove the effects of price changes. Information is also presented for gross household disposable income including social transfers in kind, such as health or education provided for free or at reduced prices by governments and not-for-profit organizations. This indicator is in US dollars per capita at current prices and PPPs.
- https://data.oecd.org/hha/household-disposable-income.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Household_Disposable_Income

#### Household Spending
- Household spending is the amount of final consumption expenditure made by resident households to meet their everyday needs, such as food, clothing, housing (rent), energy, transport, durable goods (notably cars), health costs, leisure, and miscellaneous services. It is typically around 60% of gross domestic product (GDP) and is therefore an essential variable for economic analysis of demand. Household spending including government transfers (referred to as "actual individual consumption" in national accounts) is equal to households' consumption expenditure plus those expenditures of general government and non-profit institutions serving households (NPISHs) that directly benefit households, such as health care and education. "Housing, water, electricity, gas, and other fuels", one out of the twelve categories distinguished, consist of both actual rentals (for tenants) and imputed rentals (for owner-occupied housing), housing maintenance, as well as costs for water, electricity, gas. Total household spending is measured in million USD (in current prices and Private consumption PPPs), as a percentage of GDP, and in annual growth rates. Household spending including government transfers is measured as a percentage of GDP. Spending in housing is presented as a percentage of household disposable income.
- https://data.oecd.org/hha/household-spending.htm#indicator-chart
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Household_Spending

#### Household Savings
- Net household saving is defined as household net disposable income plus the adjustment for the change in pension entitlements less household final consumption expenditure (households also include non-profit institutions serving households). The adjustment item concerns (mandatory) saving of households, by building up funds in employment-related pension schemes. Household saving is the main domestic source of funds to finance capital investments, a major impetus for long-term economic growth. The net household saving rate represents the total amount of net saving as a percentage of net household disposable income. It thus shows how much households are saving out of current income and also how much income they have added to their net wealth. All OECD countries compile their data according to the 2008 System of National Accounts (SNA).
- https://data.oecd.org/hha/household-savings.htm#indicator-chart
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Household_Savings

#### Household Debt
- Household debt is defined as all liabilities of households (including non-profit institutions serving households) that require payments of interest or principal by households to the creditors at a fixed dates in the future. Debt is calculated as the sum of the following liability categories: loans (primarily mortgage loans and consumer credit) and other accounts payable. The indicator is measured as a percentage of net household disposable income.
- https://data.oecd.org/hha/household-debt.htm#indicator-chart
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Household_Debt

#### Household Net Worth
- Household total net worth represents the total value of assets (financial as well as non-financial) minus the total value of outstanding liabilities of households (including non-profit institutions serving households). Please note that this indicator only takes into account the value of dwellings, and not other types of non-financial assets. The following financial assets and liabilities are included: currency and deposits; debt securities; loans; equity and investment fund shares/units; insurance, pensions and standardised guarantee schemes; financial derivatives and employee stock options; and other accounts receivable/payable. The indicator is measured as a percentage of household net disposable income.
- https://data.oecd.org/hha/household-net-worth.htm#indicator-chart
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Household_Net_Worth

#### Nominal Housing Prices
- Housing prices include housing rent prices indices, real and nominal house prices indices, and ratios of price to rent and price to income. In most cases, the nominal house price index covers the sales of newly-built and existing dwellings, following the recommendations from the RPPI (Residential Property Prices Indices) manual. The real house price index is given by the ratio of the nominal house price index to the consumers’ expenditure deflator in each country from the OECD national accounts database. Both indices are seasonally adjusted. The price to income ratio is the nominal house price index divided by the nominal disposable income per head and can be considered as a measure of affordability. The price to rent ratio is the nominal house price index divided by the housing rent price index and can be considered as a measure of the profitability of house ownership. The price to income and price to rent ratios are indices with base year 2015.
- https://data.oecd.org/price/housing-prices.htm#indicator-chart
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Nominal_Housing_Prices

#### Real Housing Prices
- Housing prices include housing rent prices indices, real and nominal house prices indices, and ratios of price to rent and price to income. In most cases, the nominal house price index covers the sales of newly-built and existing dwellings, following the recommendations from the RPPI (Residential Property Prices Indices) manual. The real house price index is given by the ratio of the nominal house price index to the consumers’ expenditure deflator in each country from the OECD national accounts database. Both indices are seasonally adjusted. The price to income ratio is the nominal house price index divided by the nominal disposable income per head and can be considered as a measure of affordability. The price to rent ratio is the nominal house price index divided by the housing rent price index and can be considered as a measure of the profitability of house ownership. The price to income and price to rent ratios are indices with base year 2015.
- https://data.oecd.org/price/housing-prices.htm#indicator-chart
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Real_Housing_Prices

---

### Non-performing Loans and Solvency

#### Non-Performing Loans Ratio
- Nonperforming loans to total gross loans ratio is calculated by using the value of nonperforming loans (NPLs) as the numerator and the total value of the loan portfolio (including NPLs, and before the deduction of specific loan- loss provisions) as the denominator. It is often used as a proxy for asset quality and is intended to identify problems with asset quality in the loan portfolio.
- https://datahelp.imf.org/knowledgebase/articles/484368-in-financial-soundness-indicators-fsis-what-is
- https://data.imf.org/?sk=51b096fa-2cd2-40c2-8d09-0699cc1764da&sid=1411569045760
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Non-Performing_Loans_Ratio

## Economic Indicators and Investment

### Market and Consumer Indices

#### Producer Price Index (PPI)
- Producer price indices in manufacturing measure the rate of change in prices of products sold as they leave the producer. They exclude any taxes, transport and trade margins that the purchaser may have to pay. PPIs provide measures of average movements of prices received by the producers of various commodities. They are often seen as advanced indicators of price changes throughout the economy, including changes in the prices of consumer goods and services. Manufacturing covers the production of semi-processed goods and other intermediate goods as well as final products such as consumer goods and capital equipment. A variety of price indices may be used to measure inflation in an economy. These include consumer price indices (CPI), price indices relating to specific goods and/or services, GDP deflators and producer price indices (PPI). This indicator is presented for total market and domestic market and is measured in terms of the annual growth rate and in index.
- https://data.oecd.org/price/producer-price-indices-ppi.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Producer_Price_Index

#### Consumer Confidence Index (CCI)
- This consumer confidence indicator provides an indication of future developments of households’ consumption and saving, based upon answers regarding their expected financial situation, their sentiment about the general economic situation, unemployment and capability of savings. An indicator above 100 signals a boost in the consumers’ confidence towards the future economic situation, as a consequence of which they are less prone to save, and more inclined to spend money on major purchases in the next 12 months. Values below 100 indicate a pessimistic attitude towards future developments in the economy, possibly resulting in a tendency to save more and consume less.
- https://data.oecd.org/leadind/consumer-confidence-index-cci.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Consumer_Confidence_Index

#### International Tourist Arrivals
- International inbound tourists (overnight visitors) are the number of tourists who travel to a country other than that in which they have their usual residence, but outside their usual environment, for a period not exceeding 12 months and whose main purpose in visiting is other than an activity remunerated from within the country visited.
- https://data.worldbank.org/indicator/ST.INT.ARVL
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/International_Tourism_Number_of_Arrivals

### Investment Trends

#### Foreign Direct Investment Flows (FDI Flows)
- Foreign Direct Investment (FDI) flows record the value of cross-border transactions related to direct investment during a given period of time, usually a quarter or a year. Financial flows consist of equity transactions, reinvestment of earnings, and intercompany debt transactions. Outward flows represent transactions that increase the investment that investors in the reporting economy have in enterprises in a foreign economy, such as through purchases of equity or reinvestment of earnings, less any transactions that decrease the investment that investors in the reporting economy have in enterprises in a foreign economy, such as sales of equity or borrowing by the resident investor from the foreign enterprise. Inward flows represent transactions that increase the investment that foreign investors have in enterprises resident in the reporting economy less transactions that decrease the investment of foreign investors in resident enterprises. FDI flows are measured in USD and as a share of GDP. FDI creates stable and long-lasting links between economies.
- https://data.oecd.org/fdi/fdi-flows.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Foreign_Direct_Investment_Flows

#### Business Confidence Index
- This business confidence indicator provides information on future developments, based upon opinion surveys on developments in production, orders and stocks of finished goods in the industry sector. It can be used to monitor output growth and to anticipate turning points in economic activity. Numbers above 100 suggest an increased confidence in near future business performance, and numbers below 100 indicate pessimism towards future performance.
- https://data.oecd.org/leadind/business-confidence-index-bci.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Business_Confidence_Index

### Economic Metrics

#### Tourism Contribution to GDP
- Tourism direct GDP corresponds to the part of GDP generated by all industries directly in contact with visitors.
- https://www.unwto.org/tourism-statistics/economic-contribution-SDG
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Tourism_Contribution_to_GDP

## Industrial and Trade

### Trade Patterns

#### Total Exports & Imports
- https://data.imf.org/regular.aspx?key=61013712
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Total_Exports_And_Imports

### Industrial Environmental Impact

#### CO2 Emissions per Capita
- Carbon dioxide emissions are those stemming from the burning of fossil fuels and the manufacture of cement. They include carbon dioxide produced during consumption of solid, liquid, and gas fuels and gas flaring.
- https://data.worldbank.org/indicator/EN.ATM.CO2E.PC
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/CO2_Emissions_Per_Capita

#### Greenhouse Emissions by Industry
- Global greenhouse gas emissions continue to rise, at a time when they need to be rapidly falling.
- To effectively reduce emissions we need to know where they are coming from – which sectors contribute the most? How can we use this understanding to develop effective solutions and mitigation strategies?
- On this page we look at the breakdown of emissions – total greenhouse gases, plus carbon dioxide, methane and nitrous oxide individually – by sector and country.
- https://ourworldindata.org/emissions-by-sector
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Greenhouse_Emissions_By_Sector

#### Methane Emissions per Capita
- Per capita methane emissions are measured in tonnes of carbon dioxide-equivalents per person per year.
- https://ourworldindata.org/grapher/per-capita-methane-emissions?time=latest
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Methane_Emissions_Per_Capita

#### Electricity Production From Coal
- Sources of electricity refer to the inputs used to generate electricity. Coal refers to all coal and brown coal, both primary (including hard coal and lignite-brown coal) and derived fuels (including patent fuel, coke oven coke, gas coke, coke oven gas, and blast furnace gas). Peat is also included in this category.
- https://data.worldbank.org/indicator/EG.ELC.COAL.ZS?most_recent_value_desc=true
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Electricity_Production_From_Coal

### Consumption of Electricity

#### Electric Power Consumption per Capita
- Electric power consumption per capita (kWh ) is the production of power plants and combined heat and power plants less transmission, distribution, and transformation losses and own use by heat and power plants, divided by midyear population. Energy data are compiled by the International Energy Agency (IEA). IEA data for economies that are not members of the Organisation for Economic Co-operation and Development (OECD) are based on national energy data adjusted to conform to annual questionnaires completed by OECD member governments. Electricity consumption is equivalent to production less power plants' own use and transmission, distribution, and transformation losses less exports plus imports.
- https://databank.worldbank.org/source/world-development-indicators/Series/EG.USE.ELEC.KH.PC

---

### Agriculture

#### Arable Land Percentage
- Arable land includes land defined by the FAO as land under temporary crops (double-cropped areas are counted once), temporary meadows for mowing or for pasture, land under market or kitchen gardens, and land temporarily fallow. Land abandoned as a result of shifting cultivation is excluded.
- https://data.worldbank.org/indicator/AG.LND.ARBL.ZS
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Arable_Land_Percentage

---

### Air Quality and Pollution

#### PM 2.5 Concentrations
- Most polluted country and region ranking based on annual average PM2.5 concentration (μg/m³)
- Cities: https://www.iqair.com/world-most-polluted-cities
- Countries: https://www.iqair.com/world-most-polluted-countries
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/PM25_Concentration

### Climate Change Indicators

#### Annual Surface Temperature Change
- Annual estimates of mean surface temperature change measured with respect to a baseline climatology, corresponding to the period 1951-1980.
- https://climatedata.imf.org/datasets/4063314923d74187be9596f10d034914/explore
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Annual_Surface_Temperature_Change

#### CO2 Concentration Levels

#### World Monthly Atmospheric Carbon Dioxide Concentrations
- Monthly atmospheric carbon dioxide concentrations.
- https://climatedata.imf.org/datasets/9c3764c0efcc4c71934ab3988f219e0e/explore
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/World_Monthly_Atmospheric_Carbon_Dioxide_Concentrations

#### Change in Mean Sea Levels
- Change in mean sea levels in regions across the world.
- https://climatedata.imf.org/datasets/b84a7e25159b4c65ba62d3f82c605855/explore
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Change_In_Mean_Sea_Levels

#### Land Cover and Land Cover Altering Indicator
- Changes in land cover over time, grouping land cover into those types that have climate influencing, climate regulating and climate neutral impacts.
- https://climatedata.imf.org/datasets/b1e6c0ea281f47b285addae0cbb28f4b
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Land_Cover_And_Land_Cover_Altering_Indicator

### Extreme Weather Conditions

#### Climate-related Disasters Frequency
- Trend in number of climate related natural disasters.
- https://climatedata.imf.org/datasets/b13b69ee0dde43a99c811f592af4e821
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Climate-Related_Disasters_Frequency

#### Climate Risk Index
- The Global Climate Risk Index identifies the extent to which countries have been affected by extreme weather events. These can be meteorological events such as tropical storms or tornados, hydrological events such as storm surges or flash floods, or climatological events such as wildfires or droughts. The index scores are derived from country’s rankings within the following indicators, and averaged according to their weighting:
	- Number of deaths – Weight: 1/6
	- Number of deaths per 100,000 inhabitants – Weight: 1/3
	- Sum of losses in US$ in purchasing power parity (PPP) – Weight: 1/6
	- Losses per unit of Gross Domestic Product (GDP) – Weight: 1/3 
- Lower index scores indicate countries with higher risk. Countries with high ranks in each category (low numbers) add up to low index values. 
- https://resourcewatch.org/data/explore/soc067rw1-Climate-Risk-Index?section=Discover&selectedCollection=&zoom=3&lat=0&lng=0&pitch=0&bearing=0&basemap=dark&labels=light&layers=%255B%257B%2522dataset%2522%253A%25227e98607d-23d8-42f8-9662-5658f349bf0f%2522%252C%2522opacity%2522%253A1%252C%2522layer%2522%253A%25227d9a6588-ff0c-44b0-942f-e0f6e3bf99dc%2522%257D%255D&aoi=&page=1&sort=most-viewed&sortDirection=-1
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Climate_Risk_Index

### Environmental Sustainability

#### Environmental Performance Index (EPI) Score (2022)
- The 2022 EPI provides a quantitative basis for comparing, analyzing, and understanding environmental performance for 180 countries. We score and rank these countries on their environmental performance using the most recent year of data available and calculate how these scores have changed over the previous decade.
- https://epi.yale.edu/epi-results/2022/component/epi
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Environmental_Performance_Index

#### Global Green Economy Index (GGEI)
- The Global Green Economy Index™ (GGEI) measures the green economy performance of 160 countries across 18 indicators. Our measurement approach accounts for two considerations: the progress on each indicator from 2005 to the present and the distance between each country’s current performance and that required to reach global sustainability targets.
- The GGEI is defined by four key dimensions: climate change & social equity, sector decarbonization, markets & ESG investment, and environmental health. The GGEI was the first green economy index, launched in 2010, and today is the most widely referenced product of its kind internationally, utilized by policymakers, international organizations, ESG investors, and companies to evaluate and understand linkages between country green economy performance and their own commercial or organizational agendas.
- https://dualcitizeninc.com/results-from-the-2022-global-green-economy-index-ggei/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Environmental Substainability/GGEI-Results-Public-Download-1.xlsx

#### Ecological Threat Report (ETR)
- A composite index measuring the impact of ecological threats to countries made up of 5 qualitative indicators each weighed on a scale of 1-5. The higher the score, the more at risk the country.
- https://www.visionofhumanity.org/maps/ecological-threat-report/#/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Ecological_Threat_Report

### Percentage of Renewable Resources

#### Renewable Energy Consumption (% of Total Final Energy Consumption)
- Renewable energy consumption is the share of renewables energy in total final energy consumption.
- https://data.worldbank.org/indicator/EG.FEC.RNEW.ZS
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Renewable_Energy_Consumption

## Political Sociology

### Corruption Overview

#### Corruption Perceptions Index (Transparency Int.)
- The CPI ranks 180 countries and territories around the world by their perceived levels of public sector corruption, scoring on a scale of 0 (highly corrupt) to 100 (very clean).
- https://www.transparency.org/en/cpi/2022
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Corruption_Perception_Index

#### Democracy Index
- The Democracy Index, which began in 2006, provides a snapshot of the state of democracy worldwide in 165 independent states and two territories. This covers almost the entire population of the world and the vast majority of the world’s states (microstates are excluded). The Democracy Index is based on five categories: electoral process and pluralism, functioning of government, political participation, political culture, and civil liberties. Based on its scores on a range of indicators within these categories, each country is then classified as one of four types of regime: “full democracy”, “flawed democracy”, “hybrid regime” or “authoritarian regime”. A full methodology and explanations can be found in the Appendix.
- https://www.eiu.com/n/campaigns/democracy-index-2022/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Democracy_Index

#### Freedom in the World
- Since 1973, Freedom House has assessed the condition of political rights and civil liberties around the world. It is used on a regular basis by policymakers, journalists, academics, activists, and many others.
- The _Freedom in the World_ report is composed of numerical ratings and supporting descriptive texts for 195 countries and 15 territories. External analysts assess 210 countries and territories, using a combination of on-the-ground research, consultations with local contacts, and information from news articles, nongovernmental organizations, governments, and a variety of other sources. Expert advisers and regional specialists then vet the analysts’ conclusions. The final product represents the consensus of the analysts, advisers, and Freedom House staff.
- For each country and territory, _Freedom in the World_ analyzes the electoral process, political pluralism and participation, the functioning of the government, freedom of expression and of belief, associational and organizational rights, the rule of law, and personal autonomy and individual rights.
- https://freedomhouse.org/report/freedom-world#Data
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Freedom_in_the_World

#### Global Peace Index
- A composite index measuring the peacefulness of countries made up of 23 quantitative and qualitative indicators each weighted on a scale of 1-5. The lower the score the more peaceful the country.
- https://www.visionofhumanity.org/maps/#/
- https://www.visionofhumanity.org/
- https://www.economicsandpeace.org/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Peace_Index

#### Positive Peace Index
- Positive Peace is defined as the attitudes, institutions and structures that create and sustain peaceful societies. The Positive Peace Index measures the level of societal resilience of a nation or region according.
- https://www.visionofhumanity.org/maps/positive-peace-index/#/
- https://www.visionofhumanity.org/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Positive_Peace_Index

#### Global Terrorism Index
- GTI is a composite measure made up of four indicators: incidents, fatalities, injuries and hostages. To measure the impact of terrorism, a five-year weighted average is applied.
- https://www.visionofhumanity.org/maps/global-terrorism-index/#/
- https://www.visionofhumanity.org/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Terrorism_Index

#### UCDP/PRIO Armed Conflict Dataset
- A conflict-year dataset with information on armed conflict where at least one party is the government of a state in the time period 1946-2022.
- https://ucdp.uu.se/downloads/index.html#armedconflict
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/UCDPPRIO_Armed_Conflict_Dataset

#### UCDP Dyadic Dataset
- A dyad-year version of the UCDP/PRIO Armed Conflict Dataset. A dyad consists of two opposing actors in an armed conflict where at least one party is the government of a state.
- https://ucdp.uu.se/downloads/index.html#armedconflict
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/UCPD_Dyadic_Dataset

#### UCDP One-sided Violence Dataset
- An actor-year dataset with information of intentional attacks on civilians by governments and formally organized armed groups.
- https://ucdp.uu.se/downloads/index.html#armedconflict
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/UCDP_One-Sided_Violence_Dataset

#### UCDP Non-State Conflict Dataset
- A conflict-year dataset containing information on communal and organized armed conflict where none of the parties is the government of a state.
- https://ucdp.uu.se/downloads/index.html#armedconflict
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/UCDP_Non-State_Conflict_Dataset

#### UCDP Battle-Related Deaths Dataset
- This file contains a dyad-year dataset with information on the number of battle-related deaths in the conflicts from 1989-2021 that appear in the UCDP/PRIO Armed Conflict Dataset.
- https://ucdp.uu.se/downloads/index.html#armedconflict
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/UCDP_Battle-Related_Deaths_Dataset

#### UCDP Violent Political Protest Dataset
- A dyad-year dataset identifying violent political protests, 1989-2019. It presents a new –standalone- category of organized violence, which complements, and is compatible with, UCDP’s three categories of organized violence: one-sided violence, non-state, and state-based conflict.
- https://ucdp.uu.se/downloads/index.html#armedconflict

#### Cities and Armed Conflict Events (CACE)
- The Cities and Armed Conflict Events (CACE) dataset constitutes an extension of the UCDP-GED. CACE provides a systematic coding of whether these armed conflict events took place in cities. To identify which events of armed conflict took place in cities, the data was manually matched to data from the United Nations Statistics Division (see the codebook for more details). The current version is based on UCDP-GED v 18.1.
- https://ucdp.uu.se/downloads/index.html#armedconflict

#### Deadly Electoral Conflict Dataset (DECO)
- A global, georeferenced event dataset, based on UCDP data, identifying electoral violence with lethal outcomes from 1989 to 2017.
- https://ucdp.uu.se/downloads/index.html#armedconflict

### Political Inclinations

#### World Values Survey
- The World Values Survey (WVS) is a global research project that explores people's values and beliefs, how they change over time, and what social and political impact they have. Since 1981 a worldwide network of social scientists have conducted representative national surveys as part of WVS in almost 100 countries.
- The WVS measures, monitors and analyzes: support for democracy, tolerance of foreigners and ethnic minorities, support for gender equality, the role of religion and changing levels of religiosity, the impact of globalization, attitudes toward the environment, work, family, politics, national identity, culture, diversity, insecurity, and subjective well-being. 
- https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/World_Values_Survey

### Democracy and Governance

#### Electoral Integrity Global Report
- The Perceptions of Electoral Integrity (PEI) dataset by the Electoral Integrity Project (EIP) provides a comprehensive analysis of how well countries' electoral processes meet international standards of electoral integrity. Based on a survey that collects the views of election experts, the PEI dataset provides an overall score for each election, ranging from 0 to 100, as well as comparative rankings of countries based on these scores. In PEI 8.5, which is the most recent release, 497 elections in 169 countries that took place between July 1st, 2012 and December 31st, 2021 are evaluated. This data is used in the annual "Year in Election" reports.
- https://www.electoralintegrityproject.com/global-report-2023
- https://www.electoralintegrityproject.com/pei
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Electoral_Integrity_Global_Report

#### Varieties of Democracy (V-Dem) Indices
- V-Dem provides a multidimensional and disaggregated dataset that reflects the complexity of the concept of democracy as a system of rule that goes beyond the simple presence of elections. We distinguish between five high-level principles of democracy: electoral, liberal, participatory, deliberative, and egalitarian, and collect data to measure these principles.
- https://www.v-dem.net/
- https://www.v-dem.net/data/
- https://www.v-dem.net/data/the-v-dem-dataset/

## Health and Well-Being

---

### Health

#### People using at least basic sanitation services
- The percentage of people using at least basic sanitation services, that is, improved sanitation facilities that are not shared with other households. This indicator encompasses both people using basic sanitation services as well as those using safely managed sanitation services. Improved sanitation facilities include flush/pour flush to piped sewer systems, septic tanks or pit latrines; ventilated improved pit latrines, compositing toilets or pit latrines with slabs.
- https://data.worldbank.org/indicator/SH.STA.BASS.ZS

#### Current Health Expenditure per Capita (current US$)
- Current expenditures on health per capita in current US dollars. Estimates of current health expenditures include healthcare goods and services consumed during each year.
- https://data.worldbank.org/indicator/SH.XPD.CHEX.PC.CD

#### Obesity Rate & BMI
- Obesity is most commonly measured using the body mass index (BMI) scale. The World Health Organization define BMI as: "a simple index of weight-for-height that is commonly used to classify underweight, overweight and obesity in adults."
- BMI values are used to define whether an individual is considered to be underweight, healthy, overweight or obese. The WHO defines these categories using the cut-off points: an individual with a BMI between 25.0 and 30.0 is considered to be 'overweight'; a BMI greater than 30.0 is defined as 'obese'.
- https://ourworldindata.org/obesity
- https://ncdrisc.org/data-downloads-adiposity-ado.html
- https://ncdrisc.org/data-downloads-adiposity.html
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/BMI

#### Diabetes Prevalence
- Diabetes prevalence refers to the percentage of people ages 20-79 who have type 1 or type 2 diabetes. It is calculated by adjusting to a standard population age-structure.
- https://data.worldbank.org/indicator/SH.STA.DIAB.ZS

#### World Hearing Index (Mimi + Complements from WHO & WEF)
- Mimi have recently launched the World Hearing Index Report 2021. Based on data generated by the Mimi Hearing Test app, the report analyses 1.5 hearing tests globally. This is one of the largest data-centric pieces of hearing research ever created. This year, we interpreted the findings within the broader lens of the COVID-19 pandemic.
- https://mimi.io/world-hearing-index-2021-preview
- https://www.weforum.org/agenda/2017/03/these-are-the-cities-with-the-worst-noise-pollution/
- https://gateway.euro.who.int/en/indicators/enhis_53-percentage-of-urban-population-exposed-to-noise-level-lnight-50-db/#id=21429
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/World_Hearing_Index

#### Non-Fatal Occupational Injuries
- This indicator conveys the rate of non-fatal occupational injuries per 100'000 workers in the reference group. An occupational injury is defined as any personal injury, disease or death resulting from an occupational accident; an occupational injury is therefore distinct from an occupational disease, which is a disease contracted as a result of an exposure over a period of time to risk factors arising from work activity. An occupational accident is an unexpected and unplanned occurrence, including acts of violence, arising out of or in connection with work which results in one or more workers incurring a personal injury, disease or death. A case of occupational injury is the case of one worker incurring an occupational injury as a result of one occupational accident. An occupational injury could be fatal (as a result of occupational accidents and where death occurred within one year of the day of the accident) or non-fatal with lost work time. The workers in the particular group under consideration and covered by the source of the statistics of occupational injuries are known as the workers in the reference group. In the case of a notification system, it is the number of workers in, for example, the establishments or selected economic activities covered by the system as set out in the relevant legislation or regulations.
- https://ilostat.ilo.org/data/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Non-Fatal_Labour_Injuries

#### Fatal Occupational Injuries
- This indicator conveys the rate of fatal occupational injuries per 100'000 workers in the reference group. An occupational injury is defined as any personal injury, disease or death resulting from an occupational accident; an occupational injury is therefore distinct from an occupational disease, which is a disease contracted as a result of an exposure over a period of time to risk factors arising from work activity. An occupational accident is an unexpected and unplanned occurrence, including acts of violence, arising out of or in connection with work which results in one or more workers incurring a personal injury, disease or death. A case of occupational injury is the case of one worker incurring an occupational injury as a result of one occupational accident. An occupational injury could be fatal (as a result of occupational accidents and where death occurred within one year of the day of the accident) or non-fatal with lost work time. The workers in the particular group under consideration and covered by the source of the statistics of occupational injuries are known as the workers in the reference group. In the case of a notification system, it is the number of workers in, for example, the establishments or selected economic activities covered by the system as set out in the relevant legislation or regulations.
- https://ilostat.ilo.org/data/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Fatal_Labour_Injuries

#### Disability-Adjusted Life Years (DALYs) per 100,000 by Health Condition
- DALYs expressed per 100 000 population. DALYs for a specific cause are calculated as the sum of the years of life lost due to premature mortality (YLLs) from that cause and the years of years of healthy life lost due to disability (YLDs) for people living in states of less than good health resulting from the specific cause.   The YLLs for a cause are calculated as the number of cause-specific deaths multiplied by a loss function specifying the years lost for deaths as a function of the age at which death occurs. The loss function is based on the frontier national life expectancy projected for the year 2050 by the World Population Prospects 2012 (UN Population Division, 2013), with a life expectancy at birth of 92 years.   Prevalence YLDs are used here. Prevalence YLDs are calculated as the prevalence of each non-fatal condition multiplied by its disability weight.
- https://www.who.int/data/gho/indicator-metadata-registry/imr-details/156
- https://vizhub.healthdata.org/gbd-compare/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Burden_of_Disease

#### Prevalence by Health Condition
- Prevalence refers to the total number of individuals in a population who have a disease or health condition at a specific period of time, usually expressed as a percentage of the population.
- https://www.hsph.harvard.edu/obesity-prevention-source/prevalence-incidence/
- https://vizhub.healthdata.org/gbd-compare/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Burden_of_Disease

#### Incidence by Health Condition
- Incidence is the rate of new cases or events over a specified period for the population at risk for the event. In medicine, the incidence is commonly the newly identified cases of a disease or condition per population at risk over a specified timeframe. An example of incidence would be 795,000 new strokes in the United States, annually. Here the incidence is 795,000 new strokes, the population in the United States, and the timeframe is one year.
- https://www.ncbi.nlm.nih.gov/books/NBK430746/
- https://vizhub.healthdata.org/gbd-compare/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Burden_of_Disease

#### Death by Health Condition
- Cause-of-death data are based on the underlying cause of death, which is the disease or condition responsible for initiating the chain of events leading to death.
- https://vizhub.healthdata.org/gbd-compare/#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Burden_of_Disease


---

### Well Being

#### World Happiness Report
- It has been over ten years since the first World Happiness Report was published. And it is exactly ten years since the United Nations General Assembly adopted Resolution 66/281, proclaiming 20 March to be observed annually as International Day of Happiness. Since then, more and more people have come to believe that our success as countries should be judged by the happiness of our people. There is also a growing consensus about how happiness should be measured. This consensus means that national happiness can now become an operational objective for governments.
- https://worldhappiness.report/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/World_Happiness_Report

#### Average Hours Worked by Week
- Combine this with average net income in order to evaluate.

#### Average Paid Vacations


### Mental Health

#### WHO Mental Health Atlas
- The Mental Health Atlas, released every three years, is a compilation of data provided by countries around the world on mental health policies, legislation, financing, human resources, availability and utilization of services and data collection systems. It serves as a guide for countries for the development and planning of mental health services. The Mental Health Atlas 2020 includes information and data on the progress made towards achieving mental health targets for 2020 set by the global health community and included in WHO’s Comprehensive Mental Health Action Plan. It includes data on newly-added indicators on service coverage, mental health integration into primary health care, preparedness for the provision of mental health and psychosocial support in emergencies and research on mental health. It also includes new targets for 2030.
- https://www.who.int/publications/i/item/9789240036703
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/WHO_Mental_Health_Atlas

### Healthcare Access and Disparities

#### UHC Service Coverage Index
- The coverage of essential health services (defined as the average coverage of essential services based on tracer interventions that include reproductive, maternal, newborn and child health, infectious diseases, non-communicable diseases and service capacity and access, among the general and the most disadvantaged population). The indicator is an index reported on a unitless scale of 0 to 100, which is computed as the geometric mean of 14 tracer indicators of health service coverage. The tracer indicators are as follows, organized by four components of service coverage: 1. Reproductive, maternal, newborn and child health 2. Infectious diseases 3. Noncommunicable diseases 4. Service capacity and access.
- https://data.who.int/indicators/i/9A706FD
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/UHC_Service_Coverage_Index


#### Out-of-Pocket Expenditure (% of Current Health Expenditure)
- Share of out-of-pocket payments of total current health expenditures. Out-of-pocket payments are spending on health directly out-of-pocket by households.
- https://data.worldbank.org/indicator/SH.XPD.OOPC.CH.ZS?most_recent_value_desc=true
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Out-of-Pocket_Expenditure









## Transportation

#### Motorization Rate
- https://www.oica.net/category/vehicles-in-use/

#### Passenger Cars - Worldwide
- https://www.statista.com/outlook/mmo/passenger-cars/worldwide

#### Road Accidents
- https://data.oecd.org/transport/road-accidents.htm#indicator-chart

#### Passenger Car Registrations
- https://data.oecd.org/transport/passenger-car-registrations.htm#indicator-chart

#### Infrastructure investment
- https://data.oecd.org/transport/infrastructure-investment.htm#indicator-chart

#### Infrastructure Maintenance
- https://data.oecd.org/transport/infrastructure-maintenance.htm#indicator-chart

#### Car Sizes
- https://www.thezebra.com/resources/driving/average-car-size/

#### Car Sales
- https://www.statista.com/statistics/265891/vehicles-sales-in-selected-countries/
- https://tradingeconomics.com/country-list/total-vehicle-sales

#### Car Popularity by Country
- https://www.visualcapitalist.com/best-selling-vehicles-in-the-world-by-country/
- https://www.iea.org/data-and-statistics/charts/passenger-car-sales-2010-2022


- https://cms.uitp.org/wp/wp-content/uploads/2020/08/UITP_Statistic-Brief_national-PT-stats.pdf
- https://www.mckinsey.com/~/media/mckinsey/business%20functions/operations/our%20insights/building%20a%20transport%20system%20that%20works%20new%20charts%20five%20insights%20from%20our%2025%20city%20report%20new/elements-of-success-urban-transportation-systems-of-25-global-cities-july-2021.pdf


### Infrastructure

#### Global Quality Infrastructure Index
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Quality_Infraestructure_Index


---

## Demographic Trends

---

## Educational Development

### Worldwide Education Trends

#### Education Index
- https://databank.worldbank.org/source/education-statistics-%5E-all-indicators#
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Education Index

---

### Maximum Degree of Studies

#### Adult Education Level
- This indicator looks at adult education level as defined by the highest level of education completed by the 25-64 year-old population. There are three levels: below upper-secondary, upper secondary and tertiary education. Upper secondary education typically follows completion of lower secondary schooling. Lower secondary education completes provision of basic education, usually in a more subject-oriented way and with more specialised teachers. The indicator is measured as a percentage of same age population; for tertiary and upper secondary, data are also broken down by gender.
- https://data.oecd.org/eduatt/adult-education-level.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Adult_Education_Level

#### Population With Tertiary Education
- Population with tertiary education is defined as those having completed the highest level of education, by age group. This includes both theoretical programmes leading to advanced research or high skill professions such as medicine and more vocational programmes leading to the labour market. The measure is percentage of same age population, also available by gender. As globalization and technology continue to re-shape the needs of labour markets worldwide, the demand for individuals with a broader knowledge base and more specialized skills continues to rise.
- https://data.oecd.org/eduatt/population-with-tertiary-education.htm
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Population_With_Tertiary_Education

---

### Immigration and Integration

#### Total Refugees
- https://www.unhcr.org/refugee-statistics/download/?url=O16kkU
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Total_Refugees

### Immigration & Integration

#### Migrant Integration Policy Index
- The Migrant Integration Policy Index (MIPEX) is a unique tool which measures policies to integrate migrants in countries across six continents, including all EU Member States (including the UK), other European countries (Albania, Iceland, North Macedonia, Moldova, Norway, Serbia, Switzerland, Russia, Turkey and Ukraine), Asian countries (China, India, Indonesia, Israel, Japan, Jordan, Saudi Arabia, South Korea, United Arab Emirates), North American countries (Canada, Mexico and US), South American countries (Argentina, Brazil, Chile), South Africa, and Australia and New Zealand in Oceania.
- Policy indicators have been developed to create a rich, multi-dimensional picture of migrants’ opportunities to participate in society. In the fifth edition (MIPEX 2020), we created a core set of indicators that have been updated for the period 2014-2019 (see Methodology). MIPEX now covers the period 2007-2019. The index is a useful tool to evaluate and compare what governments are doing to promote the integration of migrants in all the countries analysed.
- The project informs and engages key policy actors about how to use indicators to improve integration governance and policy effectiveness.
- https://www.mipex.eu/what-is-mipex
- - https://www.mipex.eu/download-pdf
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Migrant_Integration_Policy_Index

---

### Natality Index

#### Birth Rate
- Crude birth rate indicates the number of live births occurring during the year, per 1,000 population estimated at midyear. Subtracting the crude death rate from the crude birth rate provides the rate of natural increase, which is equal to the rate of population change in the absence of migration.
- https://data.worldbank.org/indicator/SP.DYN.CBRT.IN
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Birth_Rate

---

### Life Conditions

#### Life Expectancy
- Life expectancy at birth indicates the number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life.
- https://data.worldbank.org/indicator/SP.DYN.LE00.IN?end=2021&start=1960
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Life_Expectancy_At_Birth

---

### Mortality Index

#### Crude Death Rate
- Crude death rate indicates the number of deaths occurring during the year, per 1,000 population estimated at midyear. Subtracting the crude death rate from the crude birth rate provides the rate of natural increase, which is equal to the rate of population change in the absence of migration.
- https://data.worldbank.org/indicator/SP.DYN.CDRT.IN
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Death_Rate

---

### Total Population

#### Total Population
- Total population is based on the de facto definition of population, which counts all residents regardless of legal status or citizenship. The values shown are midyear estimates.
- https://data.worldbank.org/indicator/SP.POP.TOTL
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Total_Population

---

### Population Density

#### Population Density per Sq Km
- Population density is midyear population divided by land area in square kilometers. Population is based on the de facto definition of population, which counts all residents regardless of legal status or citizenship--except for refugees not permanently settled in the country of asylum, who are generally considered part of the population of their country of origin. Land area is a country's total area, excluding area under inland water bodies, national claims to continental shelf, and exclusive economic zones. In most cases the definition of inland water bodies includes major rivers and lakes.
- https://data.worldbank.org/indicator/EN.POP.DNST
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Population_Density

---

## Social and Humanitarian Issues

---
---

### Violence and Crimes

#### Global Violent Deaths
- The GVD database, updated annually, provides a tool for assessing progress in implementing Target 16.1. It contains data starting from 2004 and includes datasets on direct conflict deaths, homicides, and violent deaths by firearms—including the prevalence of firearms-related killings of women, as well as figures for women victims of lethal violence more generally.
- https://www.smallarmssurvey.org/database/global-violent-deaths-gvd
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Violent_Deaths

#### Civilian Firearms Holdings
- The Small Arms Survey estimates that of the one billion firearms in global circulation as of 2017, 857 million (85 per cent) are in civilian hands, 133 million (13 per cent) are in military arsenals, and 23 million (2 per cent) are owned by law enforcement agencies. Our studies suggest that the global stockpile has increased over the past decade, largely due to civilian holdings, which grew from 650 million in 2006 to 857 million in 2017.
- https://www.smallarmssurvey.org/database/global-firearms-holdings
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Civilian_Firearms_Holdings

#### Detected Human Trafficking Victims
- https://dataunodc.un.org/dp-trafficking-persons
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Human_Trafficking_Victims

#### Persons Convicted for Human Trafficking
- https://dataunodc.un.org/dp-trafficking-persons-convicted
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Human_Trafficking_Convicted

#### Victims of Intentional Homicide
- https://dataunodc.un.org/dp-intentional-homicide-victims
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Intentional_Homicide_Victims

#### Gender-Related Killings of Women and Girls
- https://dataunodc.un.org/dp-femicide
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Intentional_Homicide_Victims_Gender_Specific_Women

---

### Drug-Related Metrics

#### Reported Drug Seizures (Kilogram Equivalent)
- https://dataunodc.un.org/dp-drug-seizures
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Reported_Drug_Seizures

#### Drug-Related Crimes
- https://www.unodc.org/unodc/en/data-and-analysis/wdr2023_annex.html
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Drug-Related_Crimes

#### Clandestine Laboratories
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Clandestine_Laboratories

#### Drug Prices & Purities
- https://dataunodc.un.org/dp-drug-prices
- https://dataunodc.un.org/dp-drug-purity
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Prices_Purities_Drugs

#### Prevalence of Disease by Drug Users
- https://dataunodc.un.org/dp-drug-use-prevalence
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Prevalence_of_Disease_by_Drug_Users

#### Expert Perception of Drug Trends
- https://www.unodc.org/unodc/en/data-and-analysis/wdr2023_annex.html
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Expert_Perception_of_Drug_Trends

---

### Nuclear and Security

#### Nuclear Weapons Count & Status
- https://fas.org/initiative/status-world-nuclear-forces/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Nuclear_Weapons_Count

#### Nuclear Threat Initiative Index
- The NTI Index assesses nuclear and radiological security conditions in 175 countries and Taiwan. The three nuclear security rankings score countries and areas on a scale of 0 to 100, where 100 is the highest possible score.
- https://www.ntiindex.org/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/NTI_Index

#### Inclusiveness Index
- The Othering and Belonging Institute’s “Inclusiveness Index” is a holistic gauge of the degree of inclusivity experienced by marginalized groups across the globe and within the United States. Our index ranks states and countries in absolute and relative terms using a variety of indicators. Our instrument is unique in striving to gauge inclusivity on its own terms rather than as part of a more general assessment of group well-being, wealth or economic conditions.
- We operationalize this definition of “inclusivity” by focusing primarily on the degree of institutional inclusion and protections extended to vulnerable groups across salient social cleavages, such as gender, race, ethnicity, religion, sexual orientation, and (dis)ability. Our index focuses on social groups rather than individuals, emphasizing the kind of marginality that results from social identities and group membership.
- https://belonging.berkeley.edu/inclusiveness-index-indicators
- https://belonging.berkeley.edu/inclusiveness-index
- https://belonging.berkeley.edu/data-resources
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Inclusiveness_Index

#### LGBTQ+ Equality Index
- https://www.equaldex.com/equality-index
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/LGBT_Equality_Index

#### Gender Inequality Index (GII)
- https://hdr.undp.org/data-center/thematic-composite-indices/gender-inequality-index#/indicies/GII
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Gender_Inequality_Index

---

### Child Welfare

#### Child Violence
- https://data.unicef.org/topic/violence/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Child_Violence

#### Sexual Abuse Against Children
- https://data.unicef.org/resources/data_explorer/unicef_f/?ag=UNICEF&df=GLOBAL_DATAFLOW&ver=1.0&dq=.PT_F_15-17_SX-V+PT_M_18-29_SX-V_AGE-18+PT_F_15-17_SX-V_HLP+PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH+PT_M_15-17_SX-V+PT_F_18-29_SX-V_AGE-18+PT_M_15-17_SX-V_HLP..&startPeriod=1970&endPeriod=2023
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Sexual_Abuse_Against_Children

#### Justification of Wife beating Amongst Adolescents
- https://data.unicef.org/topic/violence/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Wife_Beating_Justification_Adolescents

#### Child Labour
- Children around the world are routinely engaged in paid and unpaid forms of work that are not harmful to them. However, they are classified as child labourers when they are either too young to work or are involved in hazardous activities that may compromise their physical, mental, social or educational development. In the least developed countries, slightly more than one in four children (ages 5 to 17) are engaged in labour that is considered detrimental to their health and development.
- The issue of child labour is guided by three main international conventions: the International Labour Organization (ILO) Convention No. 138 concerning minimum age for admission to employment and Recommendation No. 146 (1973); ILO Convention No. 182 concerning the prohibition and immediate action for the elimination of the worst forms of child labour and Recommendation No. 190 (1999); and the United Nations Convention on the Rights of the Child. These conventions frame the concept of child labour and form the basis for child labour legislation enacted by countries that are signatories.
- Indicator: Percentage of children (aged 5-17 years) engaged in child labour (economic activities)
- Unit of measure: %
- https://data.unicef.org/topic/child-protection/child-labour/
- https://data.unicef.org/resources/data_explorer/unicef_f/?ag=UNICEF&df=GLOBAL_DATAFLOW&ver=1.0&dq=.PT_CHLD_5-17_LBR_ECON.&startPeriod=1970&endPeriod=2023
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Child_Labour

---

### Social Injustice and Rights

#### Freedom of Expression Index
- The WPF index calculated the degree of freedom available to journalists in 180 countries by pooling the responses of experts to a questionnaire devised by RSF targeted to media professionals, lawyers and sociologists. This qualitative analysis is combined with quantitative data on abuses and acts of violence against journalists during the period evaluated. The criteria considered in the questionnaire are pluralism, media independence, media environment and self-censorship, legislative framework, transparency, and the quality of the infrastructure that supports the production of news and information.
- https://www.unesco.org/en/world-media-trends/world-press-freedom-index
- https://rsf.org/en/2023-world-press-freedom-index-journalism-threatened-fake-content-industry
- https://rsf.org/en/index?year=2023
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/World_Press_Freedom_Index

#### Human Freedom Index (HFI)
- The Human Freedom Index presents the state of human freedom in the world based on a broad measure that encompasses personal, civil, and economic freedom. Human freedom is a social concept that recognizes the dignity of individuals and is defined here as negative liberty or the absence of coercive constraint. Because freedom is inherently valuable and plays a role in human progress, it is worth measuring carefully. The Human Freedom Index is a resource that can help to more objectively observe relationships between freedom and other social and economic phenomena, as well as the ways in which the various dimensions of freedom interact with one another.
- The report is co​published by the Cato Institute and the Fraser Institute.
- This eighth annual index uses 83 distinct indicators of personal and economic freedom in the following areas:
	- Rule of law
	- Security and safety
	- Movement
	- Religion
	- Association, assembly, and civil society
	- Expression and information
	- Relationships
	- Size of government
	- Legal system and property rights
	- Sound money
	- Freedom to trade internationally
	- Regulation
- https://www.cato.org/human-freedom-index/2022
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Human_Freedom_Index

---

### Food Insecurity

#### Global Hunger Index (GHI)
- The Global Hunger Index (GHI) is a tool designed to comprehensively measure and track hunger at global, regional, and national levels, reflecting multiple dimensions of hunger over time. The GHI is intended to raise awareness and understanding of the struggle against hunger, provide a way to compare levels of hunger between countries and regions, and call attention to those areas of the world where hunger levels are highest and where the need for additional efforts to eliminate hunger is greatest.
- https://www.globalhungerindex.org/
- https://www.globalhungerindex.org/methodology.html
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Hunger_Index

#### FAO State of Food Security and Nutrition Report (SOFI)
- The State of Food Security and Nutrition in the World is an important measure of global progress towards the Sustainable Development Goal of Zero Hunger. It gives an updated estimate of the number of hungry people in the world, including regional and national breakdowns.
- **Cost against Average National Food Expenditures (2020)**: In most countries in the Global South, the cost of a healthy diet exceeds average national food expenditures per capita in 2020/
- **Affordability for the Poor (2020)**: This data shows the affordability of healthy diet for the poor in every region of the world in 2020/
- **Population Unable to Afford Three diets (2020)**: Proportion of people unable to afford the three reference diets by country in 2020 – cost of the diets compared to average national income
- https://data.apps.fao.org/catalog/dataset/sofi-2020
- https://data.apps.fao.org/catalog/dataset/sofi-2020/resource/00027e56-7d88-4193-9543-b53538450c74
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/State_of_Food_Security_and_Nutrition

#### Global Food Security Index (GFSI)
- Food security is defined as the state in which people at all times have physical, social and economic access to sufficient and nutritious food that meets their dietary needs for a healthy and active life.
- Using this definition adapted from the 1996 World Food Summit, the Global Food Security Index considers the core issues of affordability, availability, and quality across a set of 113 countries. The index is a dynamic quantitative and qualitative scoring model, constructed from 28 unique indicators, that measures these drivers of food security across both developing and developed countries. The overall goal of the study is to assess which countries are most and least vulnerable to food insecurity through the categories of Affordability, Availability, and Quality and Safety.
- While food security research is the subject of many organisations worldwide, this effort is distinct for a number of reasons. This index is the first to examine food security comprehensively across the three internationally established dimensions. Moreover, the study looks beyond hunger to the underlying factors affecting food insecurity. Lastly, the EIU has created a number of unique qualitative indicators, many of which relate to government policy, to capture drivers of food security which are not currently measured in any international dataset.
- https://www.unccd.int/resources/knowledge-sharing-system/global-food-security-index
- https://impact.economist.com/sustainability/project/food-security-index/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Food_Security_Index

---

### Organized Crime

#### Global Organized Crime Index
- The [Global Organized Crime Index](http://ocindex.net) is a multi-dimensional tool that assesses the level of criminality and resilience to organized crime for 193 countries along three key pillars – criminal markets, criminal actors, and resilience. Developed over a two-year period, the Index draws from both quantitative and qualitative sources and is underpinned by over 350 expert assessments and evaluations by the GI-TOC’s regional observatories.
- The objective of the Index is to provide metrics-based information that would allow policymakers and continental and regional bodies to prioritize their interventions on the basis of a holistic assessment of where vulnerabilities lie and equip them with the means to measure the efficacy of their responses to mitigate the impact of organized crime.
- https://ocindex.net/
- D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Global_Organized_Crime_Index

#### Travel Advisories
- https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/
  D:/OneDrive/Documents/Professional Projects/A Journey Through Data Science/Blog/data-science/the-state-of-our-world-in-2023/src/inputs/Travel_Advisories

---

## Pendings

- https://ilostat.ilo.org/data/#
- https://www.imf.org/en/Publications/WEO/weo-database/2023/October/download-entire-database
- https://www.imf.org/en/Publications/WEO/weo-database/2023/October
- https://dataunodc.un.org/
- https://www.who.int/data/gho/indicator-metadata-registry/imr-details/356