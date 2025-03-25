# Course Digest

This project is meant for merging multiple projects into a single project. Please ensure you have the following installed to run the `merge.py` script. 

- Node.js (v22.9.0)
- Python (>=3.11)
- npm (v10.8.3)
- Unix based system (MacOS or Linux)

  **Note: Need to also install ts-node** `npm install --save-dev ts-node`


## How to the use the script 
1. Clone this repo using `git clone` 
2. `cd` into the directory `cd ./course-digest-merge-projects`
3. Go to [app.argos.education](https://app.argos.education)
4. Download all the projects that is associated with the product you would like to use 
5. Make a folder in the `./course-digest-merge-projects` directory that contains the unzipped projects 
6. Run `python merge.py -f [path/to/directory/with/unzipped/projects]`
7. Follow the prompts 
8. The output project should be in `./course-digest-merge-projects/output`
9. Ingest the project to which ever server you like (i.e. Proton or Tokamak) using V2 ingest 
