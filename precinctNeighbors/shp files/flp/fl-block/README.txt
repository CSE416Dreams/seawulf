2020 Citizen Voting Age Population (CVAP) Data for Florida from the 2016-2020 American Community Survey (ACS) 5 Year Estimates at the Block Group level (shapefile)

##Redistricting Data Hub (RDH) Retrieval Date
03/21/22 For CVAP Data 
04/08/22 for Shapefile

##Sources
CVAP Data retrieved from the Census Citizen Voting Age Population by Race and Ethnicity website: https://www.census.gov/programs-surveys/decennial-census/about/voting-rights/cvap.2020.html 
Shapefile retrieved from the Census FTP site at: https://www2.census.gov/geo/tiger/TIGER2020PL/LAYER/

##Fields
    Field Name                                                                                 Description
0        GEOID                                                                           Unique Identifier
1         NAME                                                     Full Geographic Name of the Block Group
2        STATE                                                                           Name of the State
3       COUNTY                                                                          Name of the County
4      C_TOT20                                                                  Citizen Estimate for Total
5      CTOTMOE                                                           Citizen Margin of Error for Total
6      C_NHS20                                                 Citizen Estimate for Not Hispanic or Latino
7      CNHSMOE                                          Citizen Margin of Error for Not Hispanic or Latino
8      C_AIA20               Citizen Estimate for American Indian or Alaska Native Alone or In Combination
9      CAIAMOE        Citizen Margin of Error for American Indian or Alaska Native Alone or In Combination
10     C_ASN20                                          Citizen Estimate for Asian Alone or In Combination
11     CASNMOE                                   Citizen Margin of Error for Asian Alone or In Combination
12     C_BLK20                      Citizen Estimate for Black or African American Alone or In Combination
13     CBLKMOE               Citizen Margin of Error for Black or African American Alone or In Combination
14     C_NHP20                        Citizen Estimate for Native Hawaiian or Other Pacific Islander Alone
15     CNHPMOE                 Citizen Margin of Error for Native Hawaiian or Other Pacific Islander Alone
16     C_WHT20                                                            Citizen Estimate for White Alone
17     CWHTMOE                                                     Citizen Margin of Error for White Alone
18     C_AIW20                             Citizen Estimate for American Indian or Alaska Native and White
19     CAIWMOE                      Citizen Margin of Error for American Indian or Alaska Native and White
20     C_ASW20                                                        Citizen Estimate for Asian and White
21     CASWMOE                                                 Citizen Margin of Error for Asian and White
22     C_BLW20                                    Citizen Estimate for Black or African American and White
23     CBLWMOE                             Citizen Margin of Error for Black or African American and White
24     C_AIB20         Citizen Estimate for American Indian or Alaska Native and Black or African American
25     CAIBMOE  Citizen Margin of Error for American Indian or Alaska Native and Black or African American
26     C_2OM20                                Citizen Estimate for Remainder of Two or More Race Responses
27     C2OMMOE                         Citizen Margin of Error for Remainder of Two or More Race Responses
28     C_HSP20                                                     Citizen Estimate for Hispanic or Latino
29     CHSPMOE                                              Citizen Margin of Error for Hispanic or Latino
30  CVAP_TOT20                                                                     CVAP Estimate for Total
31  CVAPTOTMOE                                                              CVAP Margin of Error for Total
32  CVAP_NHS20                                                    CVAP Estimate for Not Hispanic or Latino
33  CVAPNHSMOE                                             CVAP Margin of Error for Not Hispanic or Latino
34  CVAP_AIA20                  CVAP Estimate for American Indian or Alaska Native Alone or In Combination
35  CVAPAIAMOE           CVAP Margin of Error for American Indian or Alaska Native Alone or In Combination
36  CVAP_ASN20                                             CVAP Estimate for Asian Alone or In Combination
37  CVAPASNMOE                                      CVAP Margin of Error for Asian Alone or In Combination
38  CVAP_BLK20                         CVAP Estimate for Black or African American Alone or In Combination
39  CVAPBLKMOE                  CVAP Margin of Error for Black or African American Alone or In Combination
40  CVAP_NHP20                           CVAP Estimate for Native Hawaiian or Other Pacific Islander Alone
41  CVAPNHPMOE                    CVAP Margin of Error for Native Hawaiian or Other Pacific Islander Alone
42  CVAP_WHT20                                                               CVAP Estimate for White Alone
43  CVAPWHTMOE                                                        CVAP Margin of Error for White Alone
44  CVAP_AIW20                                CVAP Estimate for American Indian or Alaska Native and White
45  CVAPAIWMOE                         CVAP Margin of Error for American Indian or Alaska Native and White
46  CVAP_ASW20                                                           CVAP Estimate for Asian and White
47  CVAPASWMOE                                                    CVAP Margin of Error for Asian and White
48  CVAP_BLW20                                       CVAP Estimate for Black or African American and White
49  CVAPBLWMOE                                CVAP Margin of Error for Black or African American and White
50  CVAP_AIB20            CVAP Estimate for American Indian or Alaska Native and Black or African American
51  CVAPAIBMOE     CVAP Margin of Error for American Indian or Alaska Native and Black or African American
52  CVAP_2OM20                                   CVAP Estimate for Remainder of Two or More Race Responses
53  CVAP2OMMOE                            CVAP Margin of Error for Remainder of Two or More Race Responses
54  CVAP_HSP20                                                        CVAP Estimate for Hispanic or Latino
55  CVAPHSPMOE                                                 CVAP Margin of Error for Hispanic or Latino
56     STATEFP                                                                             State FIPS Code
57    COUNTYFP                                                                            County FIPS Code
58     TRACTCE                                                                                  Tract Code
59    BLKGRPCE                                                                            Block Group Code

##Processing
CVAP data for Florida was retrieved with a Python script from the Census. 
The data is available nationally for the Block Group. 
To extract the data for Florida the national data was grouped by state and then extracted to a new file for each state. 
The data was pivoted from narrow to wide data based on GEOIDs so that one row is one Block Group, and each field represents either an estimate or margin of error for a particular racial/ethnic category. 
The fields were renamed to fit character length requirements. 
The CSV was zipped into a folder with supporting files, ACS documentation, and this README. 
Processing was primarily completed using Python's pandas library.
To improve the usefulness of the data, we have modified three categories to correspond with the Office of Management and Budget (OMB) racial categories. The "Alone" categories for American Indian or Alaska Native (fields with "AIA"), Asian (fields with "ASN"), and Black or African American (fields with "BLK") represent an encompassing racial category that is inclusive of all categories that include that race. For example, CVAP_AIA20 would be the sum of the original "Alone" CVAP_AIA20, CVAP_AIB20, and CVAP_AIW20. For CVAP_BLK20, the field would be the sum of the original CVAP_BLK20, CVAP_AIB20, and CVAP_BLW20. For CVAP_ASN20, the field would be the sum of the original CVAP_ASN20 and CVAP_ASW20 These fields are also noted in the description as being "Alone or In Combination". No other estimate categories were modified.
For the estimates that were modified to fit OMB racial/ethnic categories, we also modified the Margins of Error as well. To create the new MOEs for the derived estimates, we summed the squared values of each MOE for the necessary fields, and then took the square root of the summed value. The fields that are represented with these modified MOEs correspond to the modified racial categories described above. They are rounded to the nearest hundredth.
For more information on OMB racial categories, please see this link: https://obamawhitehouse.archives.gov/omb/bulletins_b00-02/#n_1_
All of the racial estimates provided are Non-Hispanic. Breakdowns for Hispanic/Non-Hispanic by race are not provided in the CVAP special tabulation.
Null values or empty cells in the CSV file retrieved from the Census are assigned the value -999999. 
The processed CVAP data was joined with the shapefile on the GEOID or GEOID20 field using the pandas and geopandas libraries. Only columns from the CVAP data were retained, with the addition of the geometry field.

##Additional Notes
For more information on the ACS CVAP documentation please refer to the ACS link above in Sources as well as the ACS technical documentation included in this folder (also available at this link: https://www2.census.gov/programs-surveys/decennial/rdo/technical-documentation/special-tabulation/CVAP_2016-2020_ACS_documentation.pdf ).
Please note that this dataset is derived from data collected in the five year range of 2016-2020. The Census recommends against using different datasets that contain overlapping years. For more information please see https://www.census.gov/newsroom/blogs/random-samplings/2022/03/period-estimates-american-community-survey.html
Please direct questions related to processing this dataset to info@redistrictingdatahub.org.