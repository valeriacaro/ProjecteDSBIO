# Data Science in Bio Informatics Final Project

GCED - Genetic Breakers

# Objectives 

The objective of this project is to proceed to create a synthetic dataset by attempting to model the probability of suffering from a certain disease, which cannot be named at the moment, as the rest of the classmates in the DSBIO course of the GCED degree will have to discover it in a hackathon that will take place on December 14, 2023.

This dataset should include the triggering variables of the disease, as well as other variables not used for the model in order to mislead the classmates, accompanied by the target variable of the probability that the individual described in that row will have of being sick.

# Variables

The dataset contains 21 variables:

* **Sex**: A categorical variable indicating the person's gender. String type.
* **Sleep less than 6h**: A numerical variable indicating whether the person sleeps less than 6 hours on average per day (value of 1) or not (value of 0).
* **Visited tropical countries**: A numerical variable indicating whether the person has visited tropical countries before in their life (value of 1) or not (value of 0).
* **Smoker**: A numerical variable indicating whether the person is or has been a smoker (1 for yes, 0 for no).
* **C9orf72**: A numerical variable indicating whether the person has a mutation in the C9orf72 gene (value of 1) or if their status is normal (value of 0).
* **Age**: A numerical variable indicating the age of the subject.
* **Cholesterol Levels**: A numerical variable of float type providing the person's cholesterol level in their latest analysis.
* **Contact sports**: A numerical variable indicating whether the subject has practiced contact sports at any point in their life (value of 1) or not (value of 0). Contact sports are understood as those involving minimal physical contact between players, such as rugby or boxing, among many others.
* **Adequate Physical Activity**: A numerical variable indicating the patient's level of physical activity. A score of 0 is assigned if the person leads a very sedentary lifestyle, while a score of 1 is assigned if there is some level of physical activity.
* **Result PCR Mycoplasma**: A numerical variable indicating the result of the PCR test for the bacterium Mycoplasma conducted on the patient. A value of 1 denotes a positive result, and 0 indicates a negative result.
* **Professions**: A string variable indicating the person's occupation or the profession to which they have dedicated the majority of their life.
* **Immune Depression**: A numerical variable indicating immune depression, with a value of 1 for a positive case and 0 for a negative case.
* **Military Service**: A numerical variable indicating whether the person has had participation in the military service of any country at some point in their life (1 for yes, 0 for no).
* **BMI**: A numerical variable of float type indicating the patient's body mass index.
* **TARDBP**: A numerical variable indicating whether the person has a mutation in the TARDBP gene (1 for yes, 0 for no).
* **Ethnicity**: A string variable indicating the person's ethnicity.
* **Excessive Alcohol Consumption**: A numerical variable indicating whether the patient is considered to have excessive alcohol consumption (1 for yes, 0 for normal/low).
* **Hypertension**: A boolean variable indicating whether the patient has hypertension.
* **SOD1**: A numerical variable indicating whether the person has a mutation in the SOD1 gene (1 for yes, 0 for no).
* **Sick**: The target variable; a binary variable indicating whereas the patient will develop the disease.
