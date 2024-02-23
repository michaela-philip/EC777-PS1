#### Covered California Data Description ####

There are 3 files:
1) households777.csv - household-year level variables
2) plans777.csv - plan level variables
3) household_plan_year777.csv - household-plan-year level variables

Variables in households777.csv:
household_id
year
rating area - markets numbered 1-19 (see my RAND paper for a geographic map if you'd like)
choice - chosen plan name
previous_hoice - previous chosen plan name (NA if no new enrollee)		
FPL - income as a percentage of the federal poverty level
household_size
subsidy - household's subsidy (cannot make premium negative)
penalty - household's individual mandate penalty for not purchasing insurance
perc_agebin - % of household members in agebin
perc_race - % of household members of indicated race/ethnicity
perc_male - % of household members that are male
language

Variables in plans777.csv:
plan_name - plan id
Insurer - insurer selling plan
Metal_Level - metal tier
AV - actuarial value of plan
HMO - indicates whether plan is an health maintenace organization (1 yes, 0 no)

Variables in household_plan_year777.csv
household_id
plan_name
year
premium - premium before subsidies (household-specific)
AV_CSR - AV of plan after accounting for cost sharing reductions (CSRs); household-specific because it depends on income