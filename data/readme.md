# RV Hackathon HMIS homelessness data set - readme and codebook

The Homeless Management Information System (HMIS) is a local information technology system used to collect client-level data and data on the provision of housing and services to homeless individuals and families and persons at risk of homelessness (House and Urban Development Exchange, 2018).  

The Charlotte HMIS combines data from multiple agencies and organizations (the Continuum of Care) to create a cohesive data source for attending to the needs of people experiencing homelessness. One of the primary goals of the Continuum of Care is to end chronic homelessness. See the definition for chronic homelessness from Housing and Urban Development: [https://www.hudexchange.info/resources/documents/Flowchart-of-HUDs-Definition-of-Chronic-Homelessness.pdf](https://www.hudexchange.info/resources/documents/Flowchart-of-HUDs-Definition-of-Chronic-Homelessness.pdf)

## Prompts
Create a tool, policy, predictive model, or other analysis to help government officials and health professionals more effectively use their time and resources. Using the provided datasets (and supplemental data where possible) explain the value of your work in a 5-minute presentation. Potential problems to solve:  

1. How do rates of homelessness for people of color compare to the general population and the population of people living in deep poverty (<50% of federal poverty rate)? Use HMIS and Census data to assess the scope of racial disparities in experiences of homelessness in Charlotte-Mecklenburg CoC. Assess whether programs are providing equitable services and housing and if housing outcomes are equitable for clients across races and ethnicities.  

2. How do rates of homelessness for older adults (55+) compare to the general population and the population of people living in deep poverty (<50% of federal poverty rate)? Use HMIS and Census data to assess the scope of age disparities in experiences of homelessness in Charlotte-Mecklenburg CoC. Assess whether programs are providing equitable services and housing and if housing outcomes are equitable for clients across age groups.  

**Note:** Everyone deserves the right to housing. Make recommendations based on the following with the aim to improve matching between clients and providers rather than selecting some clients and excluding others. We aim to recognize that the ‘success’ or ‘failure’ of a client does not relate solely to household/demographic characteristics but also may be affected by systems and opportunities over time for each household or by the quality of the program they are participating in. 

3. What person/household characteristics are associated with positive housing exits and/or a return to homelessness post positive housing exit? Do these factors vary between program type? Do these factors vary by race/ethnicity/age?  

4. Develop a scoring tool to assess program effectiveness by evaluating change in client state at program exit.  

5. Evaluate how forms of income change between program entry and exit. These include earned income, disability benefits, SNAP benefits or even health insurance.  
		

## Rubric
**Project Relevance**  Does the project help solve a problem pertinent to homelessness in the Charlotte area?  
**Technical Difficulty**	Does the project use multiple technologies in a novel or innovative way?  
**Design**	Is the project intuitive, usable, and visually appealing to all users?  
**Completion**	Is the project functional? Can a user interact with the project without intervention from the project team?  
**Code Quality**	Is the code well organized, readable, and help provide context on the problem without the help of a presentation?  
**Future Considerations**  Have future iterations of the project been considered? Have lessons learned been communicate in the project either in the documentation, presentation or product?  

## Hackathon timeline, deliverables & other details

6PM Friday - The data will be released.

8AM Saturday - election for judging track due (choose homelessness data open-ended prompt, opioid data open-ended prompt or opioid data prediction prompt)  
10AM Saturday - code submissions due for judged tracks (i.e., not prediction)  
11AM Saturday - presentations due for judged tracks and code due for kaggle track  

**Submissions:**	Final submission consists of: Emailing your Demo OR a link to your demo to <hackathon@redventures.com>. Title/Name of project; a short description of project (<25 words); name of team & team members; data source; code; screen-cast or screenshots describing the project. Team Photograph. All projects must be submitted by the conclusion of the event.	

**Audience:**	Government and non-profit professionals working with people experiencing homelessness; Local policymakers; Homelessness researchers; Data scientists and analysts  

**Datasets:**	Datasets used for the Hackathon need to be public (all participants should have open access to the data). Either data needs to be available for use on public domain and legal to use, or provided data sources by participating companies. Teams must disclose the use of their own data set.			

**Code:**	All code used must be open source and available for review by judges. 

**Equipment:**	Participants will be required to bring their own equipment. There are no specific requirements for operating system or language. All final code submissions must be posted for submission in source control for consideration.

**Presentations:** Presentations will be judged during a poster session/speed round on Saturday where judges will go around and ask teams to present their projects. The top 10 teams (selected by the judges) will then present to all the judges and hackathon participants. Teams will present using their own computers. Time allotted for each presentation is 5 minutes (strictly enforced), plus up to 5 min of Q&A (from the judges only).

## VI-SPDAT

Included in this data set are scores from a questionnaire called the [VI-SPDAT](http://www.cthmis.com/info/detail/vi-spdat/13) (Vulnerability Index - Service Prioritization Decision Assistance Tool). This questionnaire is primarily administered to those experiencing
chronic homelessness to them for permanent housing.
 *Chronic homelessness* means having a disability as well as 12+ continuous months of homelessness, or 4+ incidents of homelessness in 3 years totaling 12 months.
 
There are 3 versions of this questionnaire. _indiv_v1 was the first version and is more comprehensive. _indiv_v2 is shorter and has become the standard more recently. _fam_v2 is a version of the original used to assess family units.


## Tables

### Entry/Exit  
These tables relate to housing programs to which clients were admitted.  

`clients.csv` - basic attributes for clients at housing program entry / exit  

 `entry_exit_provider_program_type_code` - (see attached Data Standards Manual page 13-15 for further definition)  
   [1] "Coordinated Assessment (HUD)"  
   [2] "Emergency Shelter (HUD)" - e.g., overnight shelters  
   [3] "Homelessness Prevention (HUD)"                     
   [4] "Other (HUD)"                                          
   [5] "PH - Housing with services (no disability required for entry) (HUD)"  
   [6] "PH - Permanent Supportive Housing (disability required for entry) (HUD)"  
   [7] "PH - Rapid Re-Housing (HUD)"  
   [8] "Services Only (HUD)"                                            
   [9] "Street Outreach (HUD)"                                                    
   [10] "Transitional housing (HUD)"    
`disability_ent.csv` - Disability statuses at housing program entrance. May be multiple per client. Includes mental and substance abuse issues.  
`disability_ext.csv` - Disability statuses at housing program exit. May be multiple per client. Includes mental and substance abuse issues.  
`ee_reviews.csv`   
`ee_udes.csv` - HUD Universal Data Elements (which are required to be collected to be a participating agency in HMIS). See p. 29 of the data standards manual and get more info on the hot linked pages associated with those elements).  
`entry_exit.csv` - Includes program exit `Destination`, which may be used with some manual coding to describe positive and negative outcomes. See attached HUD Data Standards Manual, pages 48-51 and Housing Destinations document to understand each destination.  
`health_ins_ent.csv` Health insurance coverage at housing program entrance. Often medicaid, SSI (social security insurance) or VA coverage.  
`health_ins_ext.csv`  
`income_ent.csv` - income sources at program entry  
`income_ext.csv` - same as above, at exit  
`noncash_ent.csv` - Noncash benefits at entry  
`noncash_ext.csv` - same as above, at exit  
`vi_spdat_fam_v2.csv` - questionnaire individual responses and total score for VI-SPDAT family questionnaire, v2 (there is no v1)  
`vi_spdat_indiv_v1.csv` - questionnaire individual responses and total score for VI-SPDAT individual questionnaire, v1. There are more questions in v1 than v2. Charlotte service providers have largely switched to using v2.  
`vi_spdat_indiv_v2.csv`  

### Services

These tables relate to services rendered to clients that were not housing programs. See attached documents or advisors for more details.

"client.csv"  
"disability.csv"  
"income.csv"  
"insurance.csv"  
"noncash.csv"  
"vi_spdat_fam_v2.csv"  
"vi_spdat_indiv_v1.csv"  
"vi_spdat_indiv_v2.csv"  

## Columns of note
Many columns are self-explanatory. Included below are some that may need clarification.
Many of these columns occur in multiple tables.

### A note on `client_id`
`client_id` and `client_uid` are the same thing and can be joined throughout the dataset. 
This is a unique identifier for a person experiencing homelessness who was evaluated as part of 
a coordinated assesment, an outreach event (outdoor polling), or while receiving a service
from a non-profit organization or government agency.
While all tables include either `client_id` or `client_uid`, not all tables are unique on this
identifier. Some tables include multiple records per client, and all tables include an unnamed unique identifier column for that table numbering its rows.

`date_added` - the date record was added to HMIS database. Typically this is close to the date a service was rendered or a client was assessed for or admitted to a program.  

`recordset_id` - useful for determining when multiple rows of data related to a client were collected in the same session.

