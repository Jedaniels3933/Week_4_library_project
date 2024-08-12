# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

# Step Create a function
# for loop 
# use .count to count the Fs to see meets the condition  
# want to return outages if 2 or more f's

def solution(streets):
    power_status = streets.count("F")
    if power_status >= 2:
        return "Outage"
    else:
        return "Power"
     
        

