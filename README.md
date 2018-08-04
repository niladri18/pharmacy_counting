# Pharmacy couting problem 
1. [Problem](README.md#problem)
2. [Method](README.md#method)
3. [Output](README.md#output)

# Problem

This project generates a list of all drugs in descending order based on the total drug cost 
along with the total number of UNIQUE individuals who prescribed the medication.If there is a tie, 
the drug is sorted by it's name. The original dataset was obtained from the Centers for Medicare 
& Medicaid Services. It provides information on prescription drugs prescribed by individual 
physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  
It also describes the specific prescriptions that were dispensed at their direction, listed by 
drug name and the cost of the medication. 



# Method

I have used a binary search tree (BST) to store the drugnames, where the primary key of comparison is 
the total cost. The unique precribers of a particular drug are saved in a python dictionary. 
No additional library is need to run this program. Input file is called `itcont.txt`

# Output 

The output file, `top_cost_drug.txt` is saved in the `output` folder. Sample tests can be found in the 
`insight_testsuite` folder.




