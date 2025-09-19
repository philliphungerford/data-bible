tags:: #project/doing, [[richard-walton]], [[dataset-epath]], [[epath/db/NSWCREPathStaging]] [[epath/db/EPI_SKIN_MELIGNANCY_REPO]]

- ## Objectives ✅
  background-color:: green
- Update report to include metastasis
- TODO test margin extraction testing
- TODO update report to use mirrored DB from reporting PROD and add metastasis #next
- DONE automation -> get access to database via server -> build a case
- DONE Create login for epi team "ci_epi" #sara to create new super user ticket
	- ci_epi - py/p[+[hvsG*=(5N
- DONE write up procedure and docs for the report and AI component
- DONE Give db access to ci_data_assets
- DONE Inspect data and validate with richard
- DONE finalise the graphing report
- DONE fix issue with sql not connecting
- DONE upload data to database
- DONE Run algorithm
- DONE Build algorithm
- DONE Install conda on windows for easier testing conda envs #sara #cancelled
- ## Shortcuts
  collapsed:: true
	- [ONEDRIVE](https://nswhealth-my.sharepoint.com/:f:/r/personal/phillip_hungerford_health_nsw_gov_au/Documents/3_ACTIVE/2025_20%20ePath%20Lung%20Cancer%20(v1.5.0)?csf=1&web=1&e=vMtlhX)
	- [REPO](https://cinsw.visualstudio.com/Epidemiology%20and%20Biostatistics/_git/ePathMonitoringReport?path=%2F&version=GBv1.5.1&_a=contents)
	- [SHINY APP REVIEW METASTASIS](https://rsconnect-dev.nswhealth.net:3939/content/cfe8f55c-31c4-4267-b204-08c4c63a749a/)
	- [RWORKBENCH](https://rsconnect-dev.nswhealth.net:8787/s/e2976ff4f852263a75736/?launcher=1)
	- [MS PLANNER TICKET](https://teams.microsoft.com/l/entity/com.microsoft.teamspace.tab.planner/mytasks?tenantId=a687a7bf-02db-43df-bcbb-e7a8bda611a2&webUrl=https%3A%2F%2Ftasks.teams.microsoft.com%2Fteamsui%2FpersonalApp%2Falltasklists&context=%7B%22subEntityId%22%3A%22%2Fv1%2Fassignedtome%2Fview%2Fboard%2Ftask%2FxaB1WN0d6UedEsuDFERlK8gAKgS0%22%7D)
- ## Databases
	- Reads from: [[epath/db/NSWCREPathStaging]]
	- Reads to: [[epath/db/EPI_SKIN_MELIGNANCY_REPO]]
- ## Notes
  collapsed:: true
	- finish v1 batch upload to the DB
	- ensure that pipe 1 just copies from STAGING to our accessible DB via local laptop
	- pipe 2 runs from within workbench
	- report runs from within workbench
	- flow goes
		- LOCAL PC         -> 'PREP' EXTRACT data from NSWCR Staging -> DEV server
		  logseq.order-list-type:: number
		- RWORKBENCH -> 'BEGIN pipeline'
		  logseq.order-list-type:: number
		- RWORKBENCH -> 'TIDY'
		  logseq.order-list-type:: number
		- RWORKBENCH -> 'ENRICH'
		  logseq.order-list-type:: number
- https://app.mediaportal.com/isentia/#/playnow/v2?id=R00122932703&channel=ABC%20News&location=Australia&date=2025-07-01T20:33:46&program=ABC%20News%20Tonight&item_id=1211210208&prospect_id=3230446957&is_video=true&keywords=Cancer&keywords=Indigenous&expiry=1782938026&signature=2xb4Pgn3P3gpuX4Jgv~gyabuQFEpdoTJTRsm-xFo9NTxR9EDuRf1DoKAIqFwjkZP7C79LISZSs5hpGSSN4l8mdI7dxawUqQSShUVkiNC~MwTgBoz3SxdMRDiiTzt4asKZhqaCxjoBUdw4MAImtQvA3HYNm4Koac9qu-y566BGgcQeFdrtKEgxIT8yUOZGq9OchMHdGOEN2eIlm8xfnp8mX2JKgc9gXiop2TJ9S2d16V45c~1l0Z1kki11IyuDibuku3IHk8XlRh27yNc66EYu-2uURD3Wzk-3k1sooIvEJu1JWxHCzdFueNOS8jWuFcJcZOfLTO991G8YtOpQ4L9cA__
- ![image.png](../assets/image_1751410360565_0.png)
-