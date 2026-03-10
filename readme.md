problem statement:
You are given a file containing system logs in the format: timestamp, user_id, action 
Example: 
10:01,user1,login
10:03,user2,search
10:05,user1,purchase
10:07,user2,search
10:10,user3,login 
Task Write a program to compute: 

     
     The most active user (user with highest number of actions) 
     
     The most common action 

proposed solution:
    my solution maintains two frequency maps, one for user activity count and one for the actions count
    
    for each log update both the frequency maps accordingly
    and also maintain the most frequent user and action in seperate variables

    upadate the most frequent user variable and most frequent action variable accordingly

    finally print the most freuquent user and action