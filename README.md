# batch-update-to-work-order-statuses
Updates a set of items to a particular work order status in Alma

##### update_work_orders.py
Takes as arguments
   - Configuration file config.txt 
   - a csv file of item records, produced from the Alma Export Physical Items job.  

Run as `python update_work_orders.py config.txt items.csv`

#### config.txt
Enter in the code for each of the following.  All fields (aside from workorder_status) are mandatory and need to be the code directly from Alma. 
```
[Params]
apikey:  
baseurl: https://api-na.hosted.exlibrisgroup.com
library: {Library code defined in Alma} 
circdesk: {Circ desk code defined in Alma, default is DEFAULT_CIRC_DESK} 
workorder_status: {Work order type status code defined in Alma} 
workorder: {Work order defined in Alma}
```
