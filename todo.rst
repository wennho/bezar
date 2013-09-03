To-do List
---------------------

* Create an ad system
    - Create ads 
        - [done] Create basic ads (ads/create)  
        - Add images (up to 5)        
        - [done] Edit & delete ads         
        - allow users to modify ad creation date-time? or just automatically set it?
    - Link ads to users. Only users can edit their respective ads
    - Search for ads
        - [done] Search by title
        - Price filter
    - Price comparison (amazon, ebay, etc)
    - Ad tagging system

* Create a user system
    - [done] User registration 
    - [done] User activation
        - [done] Send activation email
        - [done] Activation confirmation
    - Users access their respective ads
    - Users have a message inbox
    - Users message other users
    - Usernames cannot be email addresses OR login with email but display username
    
* Refine process flow    
    - Ads expire after 30 days, unless reactivated
    - User does not need to explicitly create account? 
        - First post is just verified via email. User account is automatically created. 
        - Subsequent posts are also verified via email. However, editing posts requires logging in to account
        
* Implement Template & CSS for site
    - [done] Implement template inheritance and update current pages
    - Clear extra CSS, html & images

* Other sources of data (scrape) [not using APIs because we become dependent on the company, and it's not generalizable to other sites. Also, speed is not guaranteed]
	- [done] Get Scrapy framework running on craigslist
	- [done] Run Scrapy spider from a Django view call, and display returned items
	- Cover craigslist, with search 
	- cover Amazon, Ebay

* Test deployment to server
