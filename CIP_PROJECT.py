import sys
# Introduction and User Input

def welcome():
    print("Welcome to the Bioinformatics Information Space!")
    print("This program is designed to test your knowledge on Bioinformatics and recommend materials to improve your understanding!\n")
    name = input("Please enter your name: ")
    
    consent_to_proceed = input("Type 'OK' to proceed or 'quit' to exit: ").lower()
    if consent_to_proceed != 'ok':
        print("Goodbye!")
        sys.exit()
    else:
        print("Hello, " +name+ "! let's get started with the fun by testing your knowledge ): \n")

       
         

# List of questions and possible answers
questions = [
    "What is bioinformatics?",
    "Which of the following is a primary database in bioinformatics?",
    "What does BLAST stand for?",
    "Which of the following is a common application of bioinformatics?",
    "What is the central dogma of molecular biology?",
    "Which programming language is commonly used in bioinformatics?",
    "What is a sequence alignment?",
    "Which tool is used for multiple sequence alignment?",
    "What is a phylogenetic tree?",
    "Which of the following databases contains protein structure information?"
]

# Dictionary of possible answers
options = {
    0: ["a) The study of living organisms", "b) The use of computers to analyze biological data" , "c) The study of chemical processes in living organisms","d) The use of biological methods for industrial purposes" ],
    1: ["a) PubMed" ,"b) GenBank" ,"c) BLAST" ,"d) RCSB PDB"],
    2: ["a) Basic Local Alignment Search Tool","b) Biological Linkage and Analysis System Tool","c) Biochemical Location and Search Technique","d) Basic Linear Array Sequence Technique"],
    3: ["a) Genome sequencing","b) Quantum computing","c) Chemical synthesis","d) Industrial manufacturing"],
    4: ["a) DNA -> RNA -> Protein","b) RNA -> DNA -> Protein","c) Protein -> RNA -> DNA","d) DNA -> Protein -> RNA"],
    5: ["a) JavaScript","b) Python","c) HTML","d) CSS"],
    6: ["a) The arrangement of DNA sequences in a particular order","b) The matching of DNA sequences to a reference genome","c) The arrangement of amino acids in a protein","d) The process of joining DNA fragments together"],
    7: ["a) ClustalW","b) Excel","c) PowerPoint","d) Photoshop"],
    8: ["a) A diagram showing the evolutionary relationships among species","b) A chart showing the distribution of genes in a genome","c) A graph showing the levels of gene expression","d) A map showing the locations of genes on a chromosome"],
    9: ["a) GenBank","b) PDB (Protein Data Bank)","c) BLAST","d) PubMed"]
}

# Dictionary of correct answers
answers = { 0: "b",1: "b",2: "a",3: "a",4: "a",5: "b",6: "b",7: "a",8: "a",9: "b"}

# Function to run the quiz
def run_quiz():
    score = 0
    for i in range(len(questions)):
        print("Q"+ str(i+1) +":" + questions[i])
        for option in options[i]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect! The correct answer is " + answers[i]+ "\n")
    print("Your final score is " +str(score)+ " out of " +str(len(questions))+".\n" )


def feedback_and_importance():
    print("\nThe Importance of Bioinformatics:")
    print("Bioinformatics is an interdisciplinary field that develops methods and software tools for understanding biological data.\n It combines computer science, statistics, mathematics, and engineering to analyze and interpret biological data. Applications of bioinformatics include molecular medicine, agriculture, and biotechnology, making it a vital area of study in the life sciences.")

#Function putting recommended tutorials and resources in two dictionaries
def recommendations () :
    print("The Recommendations for Bioinformatics Lessons, Reading Materials and other Resources")
    youtube_links = { "Getting Started With Bioinformatics for Beinners 1" : "https://youtube.com/@xiaoleshirleyliu6474?si=ggfhImWkbvU-0IPX",
                    "Getting Started With Bioinformatics for Beginners 2 " : "https://youtube.com/@dannyarends?si=VH3lA3YMdjpzgpg0",
                    "Programming and Bioinformatics": "https://youtube.com/@bigbioinformatics7503?si=04ICh7P_5sAHfued",
                   "Bioinformatics and Computational Biology Techniques and Trends" :"https://youtube.com/@chatomics?si=Z_TyDeYqXSruagM0"
    }
    
    
    textbooks_and_websites= {
        "Learning R Programming Language" : "R For Data Science By Hadley Wickham,Mine Çetinkaya-Rundel & Garrett Grolemund",
        "Bioinformatics Techniques 1" : "A  Primer For Computational Biology",
        "Bioinformatics Techniques 2" :"Bioinformatics Data Skills Reproducible and Robust Research with Open Source Tools by Vince Buffalo",
        "Website For Seeking Help" :"https://www.biostars.org" 

    }
    # Printing out the various recommendations
    print("\nGeneral YouTube links for further learning:")
    for title, link in youtube_links.items():
        print(f"{title}: {link}")

    print("\nGeneral textbook recommendations for further reading:")
    for title, link in textbooks_and_websites.items():
        print(f"{title}: {link}")
# List of follow up questions and answers to test whether the student has improved on what the student has learnt
follow_up_questions = [
    "What is the significance of sequence alignment in bioinformatics?",
    "Which of the following tools is used for sequence alignment?",
    "What is a phylogenetic tree?",
    "Which database is used for storing nucleotide sequences?"
]

follow_up_options = [
    ["a) It helps in understanding evolutionary relationships", "b) It identifies gene functions", "c) It predicts protein structures", "d) All of the above"],
    ["a) BLAST", "b) ClustalW", "c) MUSCLE", "d) All of the above"],
    ["a) A diagram showing the evolutionary interrelations of a group of organisms", "b) A graphical representation of protein structures", "c) A database of gene sequences", "d) None of the above"],
    ["a) GenBank", "b) PDB", "c) UniProt", "d) All of the above"]
]

follow_up_answers = ["d", "d", "a", "a"]

#Function to test students again

def follow_up_assessment():
    score1 = 0
    
    for i in range(len(follow_up_questions)):
        print("Q" + str(i+1) + ": " + follow_up_questions[i])
        
        for option in follow_up_options[i]:
            print(option)
        
        answer = input("Your answer (a/b/c/d): ").lower()
        
        if answer == follow_up_answers[i]:
            print("Correct!\n")
            score1 += 1
        else:
            print("Incorrect! The correct answer is " + follow_up_answers[i] + "\n")
    
    return score1

# Functions incoorperating additional study materials
def additional_resources1():
    resources1 = { "Online Courses Available at Coursera" : "https://www.coursera.org/specializations/bioinformatics ,https://www.coursera.org/specializations/genomic-data-science",
    "NCBI (National Center for Biotechnology Information) Bioinformatics Resources": "https://www.ncbi.nlm.nih.gov/guide/all/",
    "LearnBioinformatics YouTube Tutorial" :"https://www.youtube.com/user/learnbioinformatics"

}
    for title, link in resources1.items():
        print(f"{title}: {link}")

# This function gives the student feed back on the last test and print out the additional recommended materials
def final_feedback(score1):
    print("Your new score is " +str(score1) +" out of " +str(len(follow_up_questions))+ ".")
    print("\nThank you for participating in the Bioinformatics Appreciation Program!")
    print("We hope you have a better understanding of the importance and opportunities in bioinformatics.\n\nHere are some additional resources for further learning:")
    additional_resources1()


# Main program
welcome()
run_quiz()
recommendations ()
print()
proceed = input("Type 'OK' to proceed to the follow-up assessment or 'quit' to exit: ").lower()
if proceed != 'ok':
    print("Goodbye!")
    sys.exit()
else:
    print("Great! Let's continue.\n")
follow_up_score = follow_up_assessment()
final_feedback(follow_up_score)
