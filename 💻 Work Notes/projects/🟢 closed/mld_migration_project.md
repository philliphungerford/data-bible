tags:: #project/doing, [[dataset-mld]], [[peter-moritz]]

- ## Objective
	- Migrate MLD from S drive to database for easier access and control of data
	  collapsed:: true
		- Test Phase
		  collapsed:: true
			- Test against requirements
		- Develop Phase
		  collapsed:: true
			- Build pipeline
		- Design Phase
		  collapsed:: true
			- Create schemas
		- Research Phase
		  collapsed:: true
			- [ ] Easier access via package / functions
			- [ ] Ensure user group has been created
			- [ ] Migrate data to database
			- [ ] Create database
			- [ ] Design database and ingestion procedure
			- [ ] Understand structure, required variables, etc #next
			- [x] Create DB EPI_MASTER_LINKED_DATASET for the epi team, test access to group #sara
			- [x] Get access to current data in S drive to understand structure
			- [x] Create SARA ticket to get access
- ## Shortcuts
	- [SDRIVE](file:///S:/Source Data/Master Linked Data/2020-45-06-CR2022/DataForUse)
	- [ONEDRIVE](https://nswhealth-my.sharepoint.com/:f:/r/personal/phillip_hungerford_health_nsw_gov_au/Documents/3_ACTIVE/2025_24%20MLD%20Migration?csf=1&web=1&e=N0VAqq)
- ## Requirements
	- Working database
- ## Notes
	- The mld is made up of multiple datasets in multiple tables
	  collapsed:: true
		- [mld-2025-sdrive](file:///S:/Source Data/Master Linked Data/2020-45-06-CR2022/DataForUse)
		  collapsed:: true
			- apdc - admitted patient data collection
			  collapsed:: true
				- apdc_jan2015_jun2024_allvar.sas7bdat
				- apdc_jan2015_jun2024_slim.sas7bdat
				- apdc_jul2001_jun2024.sas7bdat
			- orod - radio
			  collapsed:: true
				- artd_jan2009_jul2024.sas7bdat
			- nswcr
			  collapsed:: true
				- nswcr_cd_insi_jan2002_dec2022.sas7bdat
				- nswcr_cd_inva_jan1972_dec2022.sas7bdat
				- nswcr_cd_mult_jan1972_dec2022.sas7bdat
			- ostod - chemo
			  collapsed:: true
				- ostod_diagnosis_2013_2024.sas7bdat
				- ostod_drug_2013_2024.sas7bdat
				- ostod_pttmtcourse_2013_2024.sas7bdat
				- ostod_tnmstaging_2013_2024.sas7bdat
			- emergency department
			  collapsed:: true
				- eddc_jan2005_jun2024.sas7bdat
			- cod - cause of death
			  collapsed:: true
				- cod_jan1985_dec2022.sas7bdat
			- aboriginality - custom calc from ERA algo (key value pair ppn -> aboriginal status)
			  collapsed:: true
				- created in house (from the mld tables)
				- enhanced_aboriginality.sas7bdat
			- eswt - elective surgery waiting times
			  collapsed:: true
				- eswt_all.sas7bdat
				- eswt_onlist.sas7bdat
			- mhamb - mental health
			  collapsed:: true
				- mhamb_jan2001_jun2023.sas7bdat
				- mhamb_jan2015_jun2023.sas7bdat
			- not admitted patients
			  collapsed:: true
				- nap_se_201507_201912.sas7bdat
				- nap_se_202001_202409.sas7bdat
				- nap_service_hero_id.sas7bdat
				- nap_service_type_177_228.sas7bdat
			- ncim - notifiable conditions portal data
			  collapsed:: true
				- ncims_jan1993_apr2024.sas7bdat
			- rbdm - register for births deaths marriages (mostly used for deaths)
			  collapsed:: true
				- rbdm_jan1985_sep2024.sas7bdat
			- prms - patient reported measures
			- clincr - clinical cancer registry
			- pcor - prostate cancer
			- ndi - national death index
			- edward - new
			- ignore ACT
	- ideas
	  collapsed:: true
		- Do we have a dumping ground for tables after George has cleaned them (bronze)?
	- current folder naming system (2020-45 = protocol, 06-service, CR2022 = registry year latest)
		- 2020-45-06-CR2022
- ## Questions
	- What columns are there?
	- What variables are similar? are they all properly formatted? (george)?
	  collapsed:: true
		- PPN is the link between them all.
	- Process - one dump for each year (ok to be manual just save code for each )
	- How to manage history?
	  collapsed:: true
		- Do we just version control by year or release? and have that in the table name? or in the schema? (2025_ostod)
	- Design
		- ✅ ONE DB - SCHEMA PER YEAR
		  collapsed:: true
			- have a schema for each year with related tables underneath
			- example
			  collapsed:: true
				- MLD_2025
				  collapsed:: true
					- ostod
					- chemo
					- radio
				- MLD_2024
				  collapsed:: true
					- ostod
					- chemo
					- radio
		- ONE DB - GIANT TABLE PER YEAR
		  collapsed:: true
			- Simple 1 giant table per release (2024_MLD)
			- all tables merged into one giant one
			- granularity not clear, but a column to say what dataset it belongs to, could have many missing but its simple
			- example
			  collapsed:: true
				- [dbo][MLD_2025]
				- [dbo][MLD_2024]
		- ONE DB - DATA ENGINEERING DESIGN
		  collapsed:: true
			- use the data engineering design that has the staging and analysis ready tables with views
			- example
			  collapsed:: true
				- Bronze Staging table (exact copy of georges cleaned tables put into a schema/db)
				  collapsed:: true
					- [MLD][staging_mld_2025]
					  collapsed:: true
						- [ppn]
						- [ostod]
						- [orod]
					- [MLD][staging_mld_2024]
					  collapsed:: true
						- [ppn]
						- [ostod]
						- [orod]
				- Silver (Normalized, star schema with PPN patient table)
				  collapsed:: true
					- [MLD][tidy_mld_2024]
					  collapsed:: true
						- [ppn]
						- [ostod]
					- [MLD][tidy_mld_2024]
					  collapsed:: true
						- [ppn]
						- [ostod]
				- Gold Analysis ready tables (in a format that the epi team are happy with) (can be an sql view)
				  collapsed:: true
					- [MLD][analysis_mld_2025]
					  collapsed:: true
						- [ppn]
						- [ostod]
					- [MLD][analysis_mld_2024]
					  collapsed:: true
						- [ppn]
						- [ostod]
				- Views
				  collapsed:: true
					- latest <- view that points to the latest mld