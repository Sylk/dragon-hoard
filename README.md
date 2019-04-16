  
![alt](./assets/logo_desc.PNG)  

# Initial Run

On first run this bot will scrape all users from your server and give them all a balance of 1000 credits that are currently only usable on the server that the bot is running on.

# Commands

**`request`**   
The request command allows you to request an amount of credits from a specified user from their own balance to transfer into your balance.
```
!credits request username amountOfCredits
```
---- 
**`give`**  
The give command allows you to give an ammount of credits from your own balance into a specified user balance.
```
!credits give username amountOfCredits
```
---- 

**`destroy`**  
The destroy command permanently deletes credits in your personal balance and reduces the pool of credits on the server.
```
!credits destroy amountOfCredits
```
---- 

**`rob`**  
TODO: description of rob
```
!credits rob username amountOfCredits
```
---- 


# Setup  

**install discord.py**  
Dragon hoard runs on forked version of version of `discord.py` referred to as "the rewrite" which has must have pip installed to use. 

https://pip.pypa.io/en/stable/installing/

Then you can run the following command to get `discord.py`:

```
python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite
```
  
  
**private key**    
In `private_key.py`, find and replace `token` with your discord token. 
  
```
nano private_key.py
```

``` 

private_key 

```

