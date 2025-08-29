#Lambda EC2 Auto Shutdown
This will stop all EC2 instances daily after 7:00 PM so we can save on costs during none working hours

CloudFormation Deployment

1. Create a seperate branch with changes (.txt) 
2. Create a pull request to test the beta deployment
3. Merge the pull request to rest the production deployment

Modifying the Python Script

1. Edit the cron expression to change the time 
2. Filter by instance size type like micro, large ect. (Helpfull to target larger instances)

GitHub Actions Trigger

1. Beta deployment will be triggered by making a change and creating a pull request to main, make sure to create a new branch.
2. Production deployment will be triggered was you merge the pull request.

EC2 Stop Verification 

1. Go into your instances after 7:00 PM and they should be in a stopped state
