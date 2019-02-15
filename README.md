# sb3-project-collection
Collection of scripts to fetch scratch (MIT) projects and their data as complete .json and .csv files
# Usage
In a bash prompt simply run ./project_collector and your files will automatically be created in files/

For the current version, in order to change the user whose projects get downloaded you will need to edit each file in scripts/ and change the desired username. The variable is at the top of each file making this easy.

# What the columns mean

## Title
The name of the project.

## Instructions

Instructions on how to use the project.

## Description

On the scratch website this is actually called "*Notes and Credits*" Its where any credits for inspiration/assets used go.

## Author ID
The unique id assigned to the user who shared the project.

## ID
The unique id assigned to the project. This is the number used on websites like [Phosphorus](https://phosphorus.github.io/) or [Sulfurous](https://sulfurous.aau.at/) to identify projects.
